## Description: <br>
Routes NVIDIA Nemotron Speech (Riva) NIM tasks — deploys, runs, and tests ASR, TTS, and NMT NIMs on build.nvidia.com or self-hosted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
CC-BY-4.0 AND Apache 2.0 <br>
## Use Case: <br>
Developers and engineers deploying, testing, and operating NVIDIA Nemotron Speech (Riva) NIMs for automatic speech recognition, text-to-speech, and neural machine translation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ASR Deployment & Inference](references/asr.md) <br>
- [TTS Deployment & Inference](references/tts.md) <br>
- [NMT Deployment & Inference](references/nmt.md) <br>
- [Custom ASR Model Deployment](references/asr-custom.md) <br>
- [Custom TTS Model Deployment](references/tts-custom.md) <br>
- [TTS Pipeline Configuration](references/tts-pipelines.md) <br>
- [TTS Pronunciation](references/tts-pronunciation.md) <br>
- [ASR Pipeline Configuration](references/pipelines.md) <br>
- [Model Selection Guide](references/model-selection.md) <br>
- [Environment Setup](references/setup.md) <br>
- [Deployment Readiness Checks](references/deployment-readiness-checks.md) <br>
- [NVIDIA NIM Speech Documentation](https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html) <br>
- [NGC Model Catalog](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/models) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, API Calls] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Evaluation Agents Used: <br>
- Claude Code (`claude-code`) <br>
- Codex (`codex`) <br>



## Evaluation Tasks: <br>
18 evaluation tasks (14 positive skill-activation, 4 negative) in astra-sandbox environment using NVSkills-Eval external profile. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Checks whether skill-assisted execution avoids unsafe behavior such as secret leakage, destructive commands, or unauthorized access. <br>
- Correctness: Checks whether the agent follows the expected workflow and produces the correct final output. <br>
- Discoverability: Checks whether the agent loads the skill when relevant and avoids using it when irrelevant. <br>
- Effectiveness: Checks whether the agent performs measurably better with the skill than without it. <br>
- Efficiency: Checks whether the agent uses fewer tokens and avoids redundant work. <br>

Underlying evaluation signals used in this run: <br>
- `security`: Checks for unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Verifies that the agent loaded the expected skill and workflow. <br>
- `skill_efficiency`: Checks routing quality, decoy avoidance, and redundant tool usage. <br>
- `accuracy`: Grades final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Checks whether the overall user task completed successfully. <br>
- `behavior_check`: Verifies expected behavior steps, including safety expectations. <br>
- `token_efficiency`: Compares token usage with and without the skill. <br>



## Evaluation Results: <br>
| Dimension | Num | `claude-code` | `codex` |
|---|---:|---:|---:|
| Security | 8 | 100% (+6%) | 92% (+14%) |
| Correctness | 8 | 92% (+34%) | 86% (+16%) |
| Discoverability | 8 | 99% (+62%) | 64% (+15%) |
| Effectiveness | 8 | 81% (+24%) | 77% (+16%) |
| Efficiency | 8 | 91% (+47%) | 53% (+8%) |

## Skill Version(s): <br>
1.0.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
