#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Validate, query, and recommend models from the Nemotron Speech catalog."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import uuid
from pathlib import Path
from typing import Any


CATALOG_URL = (
    "https://raw.githubusercontent.com/nvidia-riva/Nemotron-speech-skills/"
    "main/skills/nemotron-speech/references/speech-models.v1.json"
)
LOCAL_CATALOG = Path(__file__).resolve().parent.parent / "references" / "speech-models.v1.json"
ALLOWED_MODALITIES = {"asr", "tts", "nmt"}
ALLOWED_STATUSES = {"active", "transitioning", "deprecated"}
ALLOWED_TRANSPORTS = {"http", "grpc"}
NVCF_REALTIME_WEBSOCKET_URL = (
    "wss://grpc.nvcf.nvidia.com:443/v1/realtime?intent=transcription"
)


class CatalogError(ValueError):
    """Raised when catalog data violates the v1 contract."""


def _require_string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{path} must be a non-empty string")
    return value.strip()


def validate_catalog(catalog: Any) -> dict[str, Any]:
    if not isinstance(catalog, dict):
        raise CatalogError("catalog must be an object")
    if catalog.get("schemaVersion") != 1:
        raise CatalogError("schemaVersion must be 1")
    _require_string(catalog.get("catalogId"), "catalogId")
    _require_string(catalog.get("updatedAt"), "updatedAt")
    if not isinstance(catalog.get("defaults"), dict):
        raise CatalogError("defaults must be an object")
    models = catalog.get("models")
    if not isinstance(models, list) or not models:
        raise CatalogError("models must be a non-empty array")

    seen: set[str] = set()
    for index, model in enumerate(models):
        path = f"models[{index}]"
        if not isinstance(model, dict):
            raise CatalogError(f"{path} must be an object")
        model_id = _require_string(model.get("id"), f"{path}.id")
        if model_id in seen:
            raise CatalogError(f"duplicate model id: {model_id}")
        seen.add(model_id)
        _require_string(model.get("displayName"), f"{path}.displayName")
        if model.get("modality") not in ALLOWED_MODALITIES:
            raise CatalogError(f"{path}.modality is invalid")
        if model.get("status") not in ALLOWED_STATUSES:
            raise CatalogError(f"{path}.status is invalid")
        if not isinstance(model.get("capabilities"), dict):
            raise CatalogError(f"{path}.capabilities must be an object")
        selection = model.get("selection")
        if not isinstance(selection, dict) or not isinstance(selection.get("recommendedFor"), list):
            raise CatalogError(f"{path}.selection.recommendedFor must be an array")
        cloud = model.get("cloud")
        if not isinstance(cloud, dict):
            raise CatalogError(f"{path}.cloud must be an object")
        _require_string(cloud.get("functionName"), f"{path}.cloud.functionName")
        function_id = _require_string(cloud.get("functionId"), f"{path}.cloud.functionId")
        try:
            uuid.UUID(function_id)
        except ValueError:
            raise CatalogError(f"{path}.cloud.functionId must be a UUID")
        if cloud.get("transport") not in ALLOWED_TRANSPORTS:
            raise CatalogError(f"{path}.cloud.transport is invalid")
        if cloud["transport"] == "http":
            base_url = _require_string(cloud.get("baseUrl"), f"{path}.cloud.baseUrl")
            expected_host = f"{function_id}.invocation.api.nvcf.nvidia.com"
            if base_url != f"https://{expected_host}":
                raise CatalogError(f"{path}.cloud.baseUrl must match its NVCF function ID")
        elif cloud.get("server") != "grpc.nvcf.nvidia.com:443":
            raise CatalogError(f"{path}.cloud.server must be grpc.nvcf.nvidia.com:443")
        realtime = cloud.get("realtime")
        if realtime is not None:
            expected_session_url = (
                f"https://{function_id}.invocation.api.nvcf.nvidia.com"
                "/v1/realtime/transcription_sessions"
            )
            if (
                model.get("modality") != "asr"
                or cloud.get("transport") != "grpc"
                or not isinstance(realtime, dict)
                or realtime.get("transport") != "websocket"
                or realtime.get("sessionUrl") != expected_session_url
                or realtime.get("websocketUrl") != NVCF_REALTIME_WEBSOCKET_URL
                or realtime.get("requestStyle") != "nvcf-realtime-transcription"
            ):
                raise CatalogError(f"{path}.cloud.realtime is invalid")

    for modality, choices in catalog["defaults"].items():
        if modality not in ALLOWED_MODALITIES or not isinstance(choices, dict):
            raise CatalogError(f"defaults.{modality} is invalid")
        for use_case, model_id in choices.items():
            if not isinstance(use_case, str) or model_id not in seen:
                raise CatalogError(f"defaults.{modality}.{use_case} references an unknown model")
            model = next(item for item in models if item["id"] == model_id)
            if model["modality"] != modality or model["status"] == "deprecated":
                raise CatalogError(f"defaults.{modality}.{use_case} references an invalid default")
    return catalog


def load_catalog(*, remote: bool = False, timeout: float = 3.0) -> tuple[dict[str, Any], str]:
    if remote:
        try:
            request = urllib.request.Request(
                CATALOG_URL,
                headers={"Accept": "application/json", "User-Agent": "nemotron-speech-skill/1"},
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return validate_catalog(json.load(response)), CATALOG_URL
        except (OSError, ValueError, json.JSONDecodeError):
            pass
    with LOCAL_CATALOG.open(encoding="utf-8") as handle:
        return validate_catalog(json.load(handle)), str(LOCAL_CATALOG)


def _active_models(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    return [model for model in catalog["models"] if model["status"] != "deprecated"]


def resolve_model(catalog: dict[str, Any], model_id: str) -> dict[str, Any]:
    for model in catalog["models"]:
        if model["id"] == model_id:
            return model
    raise CatalogError(f"unknown model id: {model_id}")


def recommend_model(
    catalog: dict[str, Any],
    *,
    modality: str,
    language: str | None,
    mode: str | None,
    diarization: bool,
    word_timestamps: bool,
) -> dict[str, Any]:
    candidates = [model for model in _active_models(catalog) if model["modality"] == modality]
    if language:
        requested = language.lower()

        def supports_language(model: dict[str, Any]) -> bool:
            supported = {str(value).lower() for value in model["capabilities"].get("languages", [])}
            if "multi" in supported or requested in supported:
                return True
            if "-" in requested:
                return False
            return any(value.split("-", 1)[0] == requested for value in supported)

        candidates = [
            model
            for model in candidates
            if supports_language(model)
        ]
    if mode:
        candidates = [model for model in candidates if mode in model["capabilities"].get("modes", [])]
    if diarization:
        candidates = [model for model in candidates if model["capabilities"].get("diarization") is True]
    if word_timestamps:
        candidates = [
            model for model in candidates if model["capabilities"].get("wordTimestamps") is True
        ]
    if not candidates:
        raise CatalogError("no active model matches the requested capabilities")

    if modality == "asr":
        if diarization:
            default_key = "diarization"
        elif language and language.lower() not in {"en", "en-us", "en-gb"}:
            default_key = "multilingualStreaming" if mode == "streaming" else "multilingual"
        elif mode == "offline":
            default_key = "englishOffline"
        else:
            default_key = "english"
    else:
        default_key = "multilingual"
    preferred = catalog["defaults"].get(modality, {}).get(default_key)
    return next((model for model in candidates if model["id"] == preferred), candidates[0])


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", action="store_true", help="Try the public catalog first.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--modality", choices=sorted(ALLOWED_MODALITIES))
    resolve_parser = subparsers.add_parser("resolve")
    resolve_parser.add_argument("model_id")
    recommend_parser = subparsers.add_parser("recommend")
    recommend_parser.add_argument("--modality", choices=sorted(ALLOWED_MODALITIES), required=True)
    recommend_parser.add_argument("--language")
    recommend_parser.add_argument("--mode", choices=["streaming", "offline", "online"])
    recommend_parser.add_argument("--diarization", action="store_true")
    recommend_parser.add_argument("--word-timestamps", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        catalog, source = load_catalog(remote=args.remote)
        if args.command == "validate":
            result: Any = {
                "valid": True,
                "schemaVersion": catalog["schemaVersion"],
                "models": len(catalog["models"]),
                "source": source,
            }
        elif args.command == "list":
            result = [
                model
                for model in _active_models(catalog)
                if not args.modality or model["modality"] == args.modality
            ]
        elif args.command == "resolve":
            result = resolve_model(catalog, args.model_id)
        else:
            result = recommend_model(
                catalog,
                modality=args.modality,
                language=args.language,
                mode=args.mode,
                diarization=args.diarization,
                word_timestamps=args.word_timestamps,
            )
        print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
        return 0
    except (CatalogError, OSError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
