## Description: <br>
Routes NVIDIA Nemotron Speech (Riva) NIM tasks — deploys, runs, and tests ASR, TTS, and NMT NIMs on build.nvidia.com or self-hosted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers deploying, testing, and operating NVIDIA Nemotron Speech (Riva) NIM services for speech-to-text, text-to-speech, and translation workflows. <br>

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
- [TTS Customization](https://docs.nvidia.com/nim/speech/latest/tts/customization.html) <br>
- [TTS Zero-Shot Voice Cloning](https://docs.nvidia.com/nim/speech/latest/tts/voice-cloning.html) <br>
- [Cloud Model Catalog](references/speech-models.v1.json) <br>
- [Model Selection Guide](references/model-selection.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Code] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`) <br>
- Codex (`openai/openai/gpt-5.5`) <br>



## Evaluation Tasks: <br>
18 evaluation tasks (14 positive, 4 negative) evaluated against the nemotron-speech skill. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Checks whether the skill avoids unsafe operations, secret leakage, and unauthorized access. <br>
- Correctness: Checks whether the final answer is correct against the reference answer. <br>
- Discoverability: Checks whether the expected skill was found and executed when needed. <br>
- Effectiveness: Checks whether the skill helps complete the user's goal and follows expected workflow behavior. <br>
- Efficiency: Checks routing quality, workspace-aware skill reads, and productive tool use. <br>

Underlying evaluation signals used in this run: <br>
- `security`: Detects unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Verifies the expected skill was found and executed. <br>
- `skill_efficiency`: Measures routing quality, workspace-aware skill reads, and productive tool use. <br>
- `accuracy`: Verifies final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Verifies whether the user's goal was achieved. <br>
- `behavior_check`: Verifies whether the expected workflow behavior was followed. <br>



## Evaluation Results: <br>
| Measure | Claude Code (Baseline → Skill) | Codex (Baseline → Skill) |
|---|---:|---:|
| Overall | 63% → 93% (+30 pts) | 64% → 82% (+17 pts) |
| Security | 67% → 92% (+25 pts) | 78% → 67% (-11 pts) |
| Correctness | 89% → 100% (+11 pts) | 89% → 91% (+2 pts) |
| Discoverability | 57% → 100% (+43 pts) | 57% → 88% (+31 pts) |
| Effectiveness | 58% → 85% (+27 pts) | 64% → 83% (+19 pts) |
| Efficiency | 46% → 90% (+43 pts) | 33% → 80% (+46 pts) |

## Skill Version(s): <br>
1.0.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
