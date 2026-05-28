# Nemotron-speech Skills

A skills/plugin marketplace for deploying and operating **NVIDIA Nemotron Speech** (formerly [NVIDIA Riva](https://docs.nvidia.com/nim/riva/latest/index.html)) Speech NIMs with Claude Code, Codex, and compatible AI coding assistants.

> Disclaimer: AI coding assistants can accelerate setup, deployment, and
> prototyping, but generated commands and code are development starting points.
> Review, test, and security-validate outputs before production use.

## Prerequisites

To use the skill:

- AI coding assistant with skill/plugin support, such as Claude Code, Codex, Cursor, or Windsurf

For running generated Riva/Nemotron Speech commands:

- NVIDIA AI Enterprise entitlement for self-hosted Riva NIMs
- Supported NVIDIA GPU, driver, OS, Docker, and NVIDIA Container Toolkit
- NGC API key for self-hosted registry access, or `NVIDIA_API_KEY` for cloud-hosted build.nvidia.com inference
- `nvidia-riva-client` for Python client examples

## Skill

A single umbrella skill — **`nemotron-speech`** — covers all Speech NIM workflows. The skill body is a routing surface; detailed per-workflow content lives in reference files loaded on demand (progressive disclosure).

| Reference | What it covers |
|---|---|
| `references/setup.md` | Prerequisites: drivers, Docker, NVIDIA Container Toolkit, NGC API key, Riva Python client |
| `references/deployment-readiness-checks.md` | System requirements checks, GPU compatibility, health checks, troubleshooting |
| `references/model-selection.md` | Choose the right ASR / TTS / NMT model for your use case |
| `references/asr.md` | Deploy and run Riva ASR (speech-to-text) NIMs — cloud or self-hosted |
| `references/asr-custom.md` | Deploy a custom NeMo-trained ASR model as a Riva NIM |
| `references/pipelines.md` | Advanced ASR pipeline config: VAD, diarization, language models, chunk size |
| `references/tts.md` | Deploy and run Riva TTS (text-to-speech) NIMs |
| `references/nmt.md` | Deploy and run Riva NMT (neural machine translation) NIMs |

## Example prompts

Things you can ask once the skill is installed:

- *"Which Riva model should I use for real-time call-center transcription with low latency, punctuation, and a path to self-host later?"*
- *"Help me set up a fresh Ubuntu machine for Riva NIMs, including Docker, the NVIDIA Container Toolkit, NGC login, and the Riva Python client."*
- *"Deploy a self-hosted Parakeet Riva ASR NIM and show me how to run a WAV through it with gRPC."*
- *"Use build.nvidia.com Riva ASR from Python to transcribe an audio file with Canary, but do not deploy a local container."*
- *"I need Riva TTS with Magpie. List available voices first, then synthesize text to a WAV file."*
- *"Translate English to German with Riva NMT and keep the product name NVIDIA untranslated using a DNT tag."*
- *"I fine-tuned an ASR model in NeMo and have a .nemo checkpoint. Convert it into a Riva NIM with riva-build and riva-deploy."*
- *"Tune a Riva ASR pipeline with Silero VAD, Sortformer diarization, a KenLM language model, and smaller chunk size for lower latency."*
- *"Can my L4 GPU run the Riva ASR NIM I picked? The container also never reaches ready."*

## Installation

The skill follows the [agentskills.io specification](https://agentskills.io/specification) and lives at the `skills/` path at the repo root — a layout recognized by Claude Code, Cursor, Codex, Windsurf, and other compatible agents. Pick the section below that matches your tool.

### Claude Code

Add this marketplace to `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "nemotron-speech-skills": {
      "source": {
        "source": "git",
        "url": "https://github.com/nvidia-riva/Nemotron-speech-skills.git"
      }
    }
  },
  "enabledPlugins": {
    "nemotron-speech@nemotron-speech-skills": true
  }
}
```

Alternatively, install interactively from a Claude Code session:

```
/plugin marketplace add https://github.com/nvidia-riva/Nemotron-speech-skills.git
/plugin install nemotron-speech@nemotron-speech-skills
```

### Codex (OpenAI CLI)

The repo ships a Codex plugin manifest at `.codex-plugin/plugin.json` and a marketplace at `.agents/plugins/marketplace.json`. Install with:

```bash
codex plugin add https://github.com/nvidia-riva/Nemotron-speech-skills.git
```

Or add the marketplace to your `~/.codex/config.toml`:

```toml
[[marketplaces]]
name = "nemotron-speech-skills"
url  = "https://github.com/nvidia-riva/Nemotron-speech-skills.git"
```

### Cursor

Clone the repo and reference the skill directory from your project's `.cursor/rules/` or via Cursor's settings → Rules → "Add rule from path":

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git ~/agent-skills/nemotron-speech-skills
```

Then in your Cursor project, add a rule pointing at `~/agent-skills/nemotron-speech-skills/skills/nemotron-speech/SKILL.md`, or symlink the skill into your project:

```bash
mkdir -p .cursor/rules
ln -s ~/agent-skills/nemotron-speech-skills/skills/nemotron-speech .cursor/rules/nemotron-speech
```

### Windsurf

Windsurf reads `.windsurfrules` or per-project rules. Clone the repo and reference the skill from your project:

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git ~/agent-skills/nemotron-speech-skills
```

Then add to your project's `.windsurfrules`:

```text
@include ~/agent-skills/nemotron-speech-skills/skills/nemotron-speech/SKILL.md
```

### Other agentskills.io-compatible agents

For any agent that follows the [agentskills.io specification](https://agentskills.io/specification) and auto-discovers skills under `skills/` or `.agents/skills/`, clone the repo into your workspace and the skill will be picked up automatically:

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git
```

The skill activates on trigger phrases listed in `skills/nemotron-speech/SKILL.md` (e.g., "deploy Riva ASR", "Magpie TTS", "Nemotron Speech NIM", etc.) — no per-agent config needed beyond making the repo visible.

### Verifying the skill is loaded

After installation, ask your agent something like:

> "Help me choose a Riva ASR model for low-latency English transcription."

If installed correctly, the agent should respond by routing to the `nemotron-speech` skill and consulting `references/model-selection.md`.

## Third-Party Notices

This repository does not vendor copied third-party source code. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the current notice statement.

## Contributing

This project is currently not accepting contributions.

## License

This project is licensed under [Apache-2.0](LICENSE).

SPDX-License-Identifier: Apache-2.0
