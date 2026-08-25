## Description: <br>
Routes NVIDIA Nemotron Speech (Riva) NIM tasks — deploys, runs, and tests ASR, TTS, and NMT NIMs on build.nvidia.com or self-hosted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers deploying, testing, and operating NVIDIA Nemotron Speech (Riva) NIMs for ASR, TTS, and NMT workflows via cloud-hosted or self-hosted infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Yes] <br>
**Credential Type(s):** [API key] <br>

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ASR Support Matrix](https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html) <br>
- [TTS Support Matrix](https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/tts.html) <br>
- [NMT Support Matrix](https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/nmt.html) <br>
- [Prerequisites (Driver / GPU / OS)](https://docs.nvidia.com/nim/speech/latest/get-started/prerequisites.html) <br>
- [ASR Pipeline Configuration](https://docs.nvidia.com/nim/speech/latest/asr/customization/pipeline-configuration.html) <br>
- [TTS Custom Deployment](https://docs.nvidia.com/nim/speech/latest/tts/custom-deployment.html) <br>
- [TTS Voices and Emotional Styles](https://docs.nvidia.com/nim/speech/latest/tts/voices.html) <br>
- [TTS Zero-Shot Voice Cloning](https://docs.nvidia.com/nim/speech/latest/tts/voice-cloning.html) <br>
- [NGC Model Catalog](https://catalog.ngc.nvidia.com/models) <br>
- [Model Selection Guide](references/model-selection.md) <br>
- [Speech Models Catalog (v1)](references/speech-models.v1.json) <br>
- [Setup Guide](references/setup.md) <br>
- [Deployment Readiness Checks](references/deployment-readiness-checks.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, API Calls] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`) <br>
- Codex (`openai/openai/gpt-5.5`) <br>



## Evaluation Tasks: <br>
18 evaluation tasks (14 positive, 4 negative) from a versioned skill-evaluator dataset snapshot. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Checks for unsafe operations, secret leakage, and unauthorized access. <br>
- Correctness: Checks final-answer correctness against a reference answer. <br>
- Discoverability: Checks whether the expected skill was found and executed when needed. <br>
- Effectiveness: Checks whether the user’s goal was achieved and expected workflow behavior was followed. <br>
- Efficiency: Checks routing quality, workspace-aware skill reads, and productive tool use. <br>

Underlying evaluation signals used in this run: <br>
- `security`: Detects unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Verifies whether the expected skill was found and executed. <br>
- `skill_efficiency`: Evaluates routing quality, workspace-aware skill reads, and productive tool use. <br>
- `accuracy`: Measures final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Assesses whether the user’s goal was achieved. <br>
- `behavior_check`: Verifies whether the expected workflow behavior was followed. <br>



## Evaluation Results: <br>
| Measure | Claude Code (Baseline → Skill) | Codex (Baseline → Skill) |
|---|---:|---:|
| Overall | 66% → 92% (+26 pts) | 62% → 84% (+23 pts) |
| Security | 89% → 97% (+8 pts) | 69% → 78% (+8 pts) |
| Correctness | 82% → 91% (+9 pts) | 88% → 94% (+7 pts) |
| Discoverability | 57% → 99% (+42 pts) | 57% → 89% (+32 pts) |
| Effectiveness | 56% → 86% (+29 pts) | 63% → 77% (+14 pts) |
| Efficiency | 45% → 88% (+43 pts) | 32% → 83% (+52 pts) |

## Skill Version(s): <br>
1.0.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
