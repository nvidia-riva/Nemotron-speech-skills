## Description: <br>
Orchestration skill for NVIDIA Nemotron Speech (Riva) / NeMo ASR domain and language adaptation. Given a goal like "improve/fine-tune ASR for my domain or language", it scopes the task, picks the cheapest sufficient path (word boosting → n-gram LM → fine-tuning), delegates each stage to the right sub-skill (data generation, training, evaluation, deployment), and answers cost/time/data questions along the way. <br>

This skill is ready for commercial/non-commercial use. <br>

## Owner
NVIDIA <br>

### License/Terms of Use: <br>
Apache-2.0 <br>
## Use Case: <br>
Developers and engineers who need to customize NVIDIA Nemotron Speech / Riva ASR models for specific domains or languages — improving accuracy, reducing WER, adding a language, or planning a fine-tuning pipeline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Not Specified] <br>
**Credential Type(s):** [None identified] <br>

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Orchestration Workflow](references/workflow.md) <br>
- [Path Selection (Cheapest Sufficient Rung)](references/path-selection.md) <br>
- [Planning Answers (Cost/Time/Data)](references/planning-answers.md) <br>
- [Sub-Skills Registry](references/sub-skills.md) <br>
- [NVIDIA NIM Speech ASR Customization Guide](https://docs.nvidia.com/nim/speech/latest/asr/customization/customization.html) <br>
- [NVIDIA NIM Speech Documentation](https://docs.nvidia.com/nim/speech/latest/index.html) <br>
- [NVIDIA NIM Speech ASR Support Matrix](https://docs.nvidia.com/nim/speech/latest/reference/support-matrix/asr.html) <br>
- [Riva ASR Tutorials](https://github.com/nvidia-riva/tutorials) <br>
- [Tokenizer Extension to New Language + Acoustic Fine-Tune](https://github.com/nvidia-riva/tutorials/blob/main/asr-extend-tokenizer-to-newlang-ft-acoustic-model.ipynb) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Configuration instructions] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Evaluation Agents Used: <br>
- Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`) <br>
- Codex (`openai/openai/gpt-5.5`) <br>



## Evaluation Tasks: <br>
15 evaluation tasks (12 positive, 3 negative), each run with 3 attempts per task in isolated sandbox pods. <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Security: Whether the skill is safe to use — checks for unsafe operations, secret leakage, and unauthorized access. <br>
- Correctness: Whether the answer is correct against the reference answer. <br>
- Discoverability: Whether the right skill was selected, decoys were avoided, and the workflow executed. <br>
- Effectiveness: Whether the skill helped complete the user's goal (50% goal completion + 50% expected workflow adherence). <br>
- Efficiency: Whether the skill avoided wasted tool calls and token usage (50% tool-call productivity + 50% token efficiency). <br>

Underlying evaluation signals used in this run: <br>
- `security`: Unsafe operations, secret leakage, and unauthorized access. <br>
- `skill_execution`: Whether the expected skill was selected, decoys were avoided, and the workflow executed. <br>
- `accuracy`: Final-answer correctness against the reference answer. <br>
- `goal_accuracy`: Whether the user's goal was achieved. <br>
- `behavior_check`: Whether the expected workflow behavior was followed. <br>
- `skill_efficiency`: Tool-call productivity. <br>
- `token_efficiency`: Actual uncached prompt plus completion usage. <br>



## Evaluation Results: <br>
| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | Not available | 80.6% — uplift unavailable |
| Security | Not available | 75.0% → 77.8% (+2.8 points) |
| Correctness | Not available | 64.2% → 85.6% (+21.4 points) |
| Discoverability | Not available | 92.1% — uplift unavailable |
| Effectiveness | Not available | 33.7% → 64.2% (+30.5 points) |
| Efficiency | Not available | 83.5% — uplift unavailable |

## Skill Version(s): <br>
1.2.0 (source: frontmatter) <br>

## Ethical Considerations: <br>
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal team to ensure this skill meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>

(For Release on NVIDIA Platforms Only) <br>
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail). <br>
