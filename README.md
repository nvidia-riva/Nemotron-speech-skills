# Nemotron Speech Skills

A growing collection of skills and plugins for customizing, deploying, and operating **[NVIDIA Nemotron Speech](https://docs.nvidia.com/nim/speech/latest/index.html)** (formerly NVIDIA Riva) Speech NIMs with Claude Code, Codex, and compatible AI coding assistants.

> Disclaimer: AI coding assistants can accelerate setup, deployment, and
> prototyping, but generated commands and code are development starting points.
> Review, test, and security-validate outputs before production use.

## Prerequisites

To use the skills for planning and guidance:

- AI coding assistant with skill/plugin support, such as Claude Code, Cursor, or Codex

Additional requirements depend on the workflow. Running self-hosted Riva/Nemotron Speech commands may require:

- NVIDIA AI Enterprise entitlement for self-hosted Riva NIMs
- Supported NVIDIA GPU, driver, OS, Docker, and NVIDIA Container Toolkit
- NGC API key for self-hosted registry access, or `NVIDIA_API_KEY` for cloud-hosted build.nvidia.com inference
- `nvidia-riva-client` for Python client examples

Executing an ASR fine-tuning plan also requires suitable transcribed audio, a supported NeMo training environment, and GPU capacity. A GPU or API key is not required to use the orchestration skill for planning.

Skill-specific requirements are documented in each skill and may expand as new workflows are added.

## Available skills

Each top-level directory under `skills/` is an independently discoverable skill. The catalog below lists the skills currently included in this repository; new skills can be added without changing the repository-level installation model.

| Skill | What it covers |
|---|---|
| [`nemotron-speech`](skills/nemotron-speech/SKILL.md) | Select, deploy, run, customize, and troubleshoot ASR, TTS, and NMT Speech NIMs |
| [`nemotron-asr-finetune`](skills/nemotron-asr-finetune/SKILL.md) | Plan ASR domain or language adaptation and route work through the cheapest sufficient customization path |

### `nemotron-speech`

The **`nemotron-speech`** skill covers Speech NIM deployment and operation. Its body is a routing surface; detailed per-workflow content lives in reference files loaded on demand.

| Reference | What it covers |
|---|---|
| `references/setup.md` | Prerequisites: drivers, Docker, NVIDIA Container Toolkit, NGC API key, Riva Python client |
| `references/deployment-readiness-checks.md` | System requirements checks, GPU compatibility, health checks, troubleshooting |
| `references/model-selection.md` | Choose the right ASR / TTS / NMT model for your use case |
| `references/speech-models.v1.json` | Versioned cloud model IDs, capabilities, and current NVCF routing |
| `references/asr.md` | Deploy and run Riva ASR (speech-to-text) NIMs — cloud or self-hosted |
| `references/asr-custom.md` | Deploy a custom NeMo-trained ASR model as a Riva NIM |
| `references/pipelines.md` | Advanced ASR pipeline config: VAD, diarization, language models, chunk size |
| `references/tts.md` | Deploy and run Riva TTS (text-to-speech) NIMs |
| `references/tts-custom.md` | Deploy a custom or fine-tuned NeMo TTS model as a Riva NIM |
| `references/tts-pipelines.md` | Advanced TTS synthesis config: SSML, zero-shot voice cloning, audio encoding, sample rate |
| `references/tts-pronunciation.md` | Discover, test, and apply IPA pronunciations for specific words or phrases |
| `references/nmt.md` | Deploy and run Riva NMT (neural machine translation) NIMs |
| `scripts/model_catalog.py` | Validate, resolve, or recommend entries from the cloud model catalog |

### `nemotron-asr-finetune`

The **`nemotron-asr-finetune`** skill is a high-level orchestrator for improving ASR accuracy in a domain or language. It scopes the data, quality target, latency, hardware, and deployment constraints; establishes a measured baseline; and chooses the cheapest sufficient path:

1. Word boosting or custom vocabulary for a bounded set of terms
2. An n-gram language model for domain phrasing when text is available
3. NeMo fine-tuning for acoustic gaps such as accents, noise, or channel conditions
4. Cross-language transfer or training from scratch as a last resort

For a fine-tuning path, it coordinates data preparation, NeMo training, normalized WER evaluation with a general-domain forgetting check, and Riva deployment. It delegates execution to specialized skills and provides interim guidance when a required sub-skill is not yet available.

| Reference | What it covers |
|---|---|
| [`references/workflow.md`](skills/nemotron-asr-finetune/references/workflow.md) | End-to-end orchestration stages and branch-specific workflows |
| [`references/path-selection.md`](skills/nemotron-asr-finetune/references/path-selection.md) | Cheapest-sufficient customization ladder and escalation rules |
| [`references/planning-answers.md`](skills/nemotron-asr-finetune/references/planning-answers.md) | Data volume, synthetic data, cost, training time, and GPU guidance |
| [`references/sub-skills.md`](skills/nemotron-asr-finetune/references/sub-skills.md) | Delegation registry and handoff contracts for training, data, evaluation, and deployment |

## Example prompts

Things you can ask once the skills are installed:

- *"Which Riva model should I use for real-time call-center transcription with low latency, punctuation, and a path to self-host later?"*
- *"Help me set up a fresh Ubuntu machine for Riva NIMs, including Docker, the NVIDIA Container Toolkit, NGC login, and the Riva Python client."*
- *"Deploy a self-hosted Parakeet Riva ASR NIM and show me how to run a WAV through it with gRPC."*
- *"Use build.nvidia.com Riva ASR from Python to transcribe an audio file with Canary, but do not deploy a local container."*
- *"I need Riva TTS with Magpie. List available voices first, then synthesize text to a WAV file."*
- *"Translate English to German with Riva NMT and keep the product name NVIDIA untranslated using a DNT tag."*
- *"I fine-tuned an ASR model in NeMo and have a .nemo checkpoint. Convert it into a Riva NIM with riva-build and riva-deploy."*
- *"Tune a Riva ASR pipeline with Silero VAD, Sortformer diarization, a KenLM language model, and smaller chunk size for lower latency."*
- *"Can my L4 GPU run the Riva ASR NIM I picked? The container also never reaches ready."*
- *"My call-center ASR gets product names wrong. What is the cheapest way to improve it?"*
- *"How much transcribed audio and GPU time do I need to fine-tune ASR for Indian English?"*
- *"Help me reduce domain WER without causing catastrophic forgetting on general speech."*
- *"Should I use word boosting, a KenLM language model, or fine-tuning for medical terminology?"*

## Installation

The repository follows the [agentskills.io specification](https://agentskills.io/specification). Every skill lives in its own directory under `skills/`, allowing compatible agents to discover the current catalog and future additions from the same installation. Pick the section below that matches your tool.

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

Clone the repository, then register its skill directories from your project's `.cursor/rules/` or via Cursor's settings → Rules → "Add rule from path":

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git ~/agent-skills/nemotron-speech-skills
```

The following discovers every current skill instead of naming them individually:

```bash
mkdir -p .cursor/rules
for skill_dir in ~/agent-skills/nemotron-speech-skills/skills/*; do
  skill_name=$(basename "$skill_dir")
  test -e ".cursor/rules/$skill_name" || ln -s "$skill_dir" ".cursor/rules/$skill_name"
done
```

After pulling repository updates, rerun the loop to register newly added skills.

### Windsurf

Windsurf reads `.windsurfrules` or per-project rules. Clone the repository and add one include for each skill you want to enable:

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git ~/agent-skills/nemotron-speech-skills
```

For example, the current catalog can be included with:

```text
@include ~/agent-skills/nemotron-speech-skills/skills/nemotron-speech/SKILL.md
@include ~/agent-skills/nemotron-speech-skills/skills/nemotron-asr-finetune/SKILL.md
```

Repeat the include pattern for any skills added later.

### Other agentskills.io-compatible agents

For any agent that follows the [agentskills.io specification](https://agentskills.io/specification) and auto-discovers skills under `skills/` or `.agents/skills/`, clone the repository into your workspace. Every current or future skill under `skills/` will be discovered automatically:

```bash
git clone https://github.com/nvidia-riva/Nemotron-speech-skills.git
```

Each skill activates on the trigger phrases in its `SKILL.md`. For example, deployment prompts such as "deploy Riva ASR" route to `nemotron-speech`, while requests such as "improve ASR accuracy for my domain" route to `nemotron-asr-finetune`. No per-agent configuration is needed beyond making the repo visible.

### Verifying skill discovery

After installation, test representative prompts from the current catalog:

> "Help me choose a Riva ASR model for low-latency English transcription."

This should route to `nemotron-speech` and consult its model-selection guidance.

> "My ASR gets domain jargon wrong. Help me choose the cheapest way to improve its accuracy."

This should route to `nemotron-asr-finetune`, scope the problem, establish a baseline, and compare word boosting, language-model adaptation, and fine-tuning before recommending a path.

As new skills are added, verify each one with a prompt matching the triggers documented in its `SKILL.md`.

## Third-Party Notices

This repository does not vendor copied third-party source code. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the current notice statement.

## Contributing

This project is currently not accepting contributions.

## License

This project is licensed under [Apache-2.0](LICENSE).

SPDX-License-Identifier: Apache-2.0
