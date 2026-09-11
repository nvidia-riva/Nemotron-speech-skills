# Skill Benchmark: nemotron-asr-finetune

> ⚠️ **Overall verdict: INCOMPLETE — Required evidence is missing**

One or more required evaluation tiers did not complete, so this benchmark is not publication-complete.

## Evaluation Metadata

- Skill: `nemotron-asr-finetune`
- Evaluation date: 2026-09-11
- Evaluator version: `1.5.6`
- Agents: Claude Code (`aws/anthropic/bedrock-claude-opus-4-8`), Codex (`openai/openai/gpt-5.5`)
- Tasks: 15 evaluation tasks (12 positive, 3 negative)
- Dataset digest: `sha256:1fa62861cda08361f6252d35ad657a861cf406c8680571cfa302f166fa471137` (skill-evaluator-dataset-snapshot/1)
- Attempts per task: 3
- Environment: `k8s-sandbox`
- Tier 2 evidence: required for publication
- Tier 3 evidence: required for publication

Each task attempt ran in its own isolated sandbox pod.

## What This Report Answers

The three-tier evaluation checks whether the skill:

- is safe to use;
- produces correct answers;
- is discovered and activated when needed;
- helps the agent complete the user's goal and expected workflow; and
- avoids wasted skill and tool usage.

## Results at a Glance

| Measure | Claude Code (Baseline → Skill Uplift) | Codex (Baseline → Skill Uplift) |
|---|---:|---:|
| Overall | Not available | 80.6% — baseline ran, but no comparable score was available; uplift unavailable |
| Security | Not available | 75.0% → 77.8% (+2.8 points) |
| Correctness | Not available | 64.2% → 85.6% (+21.4 points) |
| Discoverability | Not available | 92.1% — baseline ran, but no comparable score was available; uplift unavailable |
| Effectiveness | Not available | 33.7% → 64.2% (+30.5 points) |
| Efficiency | Not available | 83.5% — baseline ran, but no comparable score was available; uplift unavailable |

**How to read this table:** baseline is the same task attempted without the target skill. Scores are rounded to one decimal; threshold-adjacent values use additional precision so their displayed band matches the verdict. Uplift is derived from those displayed scores and shown in percentage points.

Example: `47.0% → 92.0% (+45.0 points)` means the skill-assisted run scored 92.0%, 45.0 percentage points above its 47.0% no-skill baseline.

A partial dimension was calculated from only the available configured signals; review the detailed report before relying on it.

## Token Usage

Actual Tier 3 execution usage is reported for every observed agent/case pair and both conditions.

| Agent | Dataset case | With skill | Without skill | Delta | Change | Coverage |
|---|---|---:|---:|---:|---:|---|
| claude-code | All cases | 2,379,250 | 4,714,444 | N/A | N/A | skill 15/15; base 20/45 |
| claude-code | nemotron-asr-orchestrate-envcheck-001 | 105,665 | 121,503 | -15,838 | -13.04% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-envcheck-insist-001 | 288,594 | 29,562 | +259,032 | +876.23% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-escalate-001 | 166,124 | 31,136 | +134,988 | +433.54% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-eval-001 | 109,192 | 91,213 | +17,979 | +19.71% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-lowdata-001 | 103,794 | 31,074 | +72,720 | +234.02% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-negative-deploy-001 | 215,994 | 94,000 | +121,994 | +129.78% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-negative-llm-001 | 162,451 | 2,757,394 | N/A | N/A | skill 1/1; base 2/3 |
| claude-code | nemotron-asr-orchestrate-negative-openai-001 | 63,154 | 97,703 | -34,549 | -35.36% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-path-001 | 101,502 | 30,766 | +70,736 | +229.92% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-planning-001 | 146,190 | 92,548 | +53,642 | +57.96% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-preflight-001 | 290,339 | 193,125 | +97,214 | +50.34% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-preflight-8khz-001 | 165,718 | 31,189 | +134,529 | +431.33% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-scope-001 | 162,126 | 125,280 | +36,846 | +29.41% | skill 1/1; base 1/1 |
| claude-code | nemotron-asr-orchestrate-subskill-reachability-001 | 192,155 | 618,847 | N/A | N/A | skill 1/1; base 3/3 |
| claude-code | nemotron-asr-orchestrate-subskills-001 | 106,252 | 369,104 | N/A | N/A | skill 1/1; base 3/3 |
| codex | All cases | 2,559,110 | 3,195,468 | N/A | N/A | skill 18/18; base 24/24 |
| codex | nemotron-asr-orchestrate-envcheck-001 | 78,544 | 166,486 | N/A | N/A | skill 1/1; base 2/2 |
| codex | nemotron-asr-orchestrate-envcheck-insist-001 | 30,079 | 13,304 | +16,775 | +126.09% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-escalate-001 | 50,034 | 13,965 | +36,069 | +258.28% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-eval-001 | 85,784 | 83,737 | +2,047 | +2.44% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-lowdata-001 | 34,777 | 17,942 | +16,835 | +93.83% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-negative-deploy-001 | 877,906 | 991,912 | -114,006 | -11.49% | skill 3/3; base 3/3 |
| codex | nemotron-asr-orchestrate-negative-llm-001 | 699,850 | 901,330 | N/A | N/A | skill 2/2; base 3/3 |
| codex | nemotron-asr-orchestrate-negative-openai-001 | 41,770 | 77,148 | -35,378 | -45.86% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-path-001 | 60,721 | 18,516 | +42,205 | +227.94% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-planning-001 | 52,806 | 39,629 | +13,177 | +33.25% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-preflight-001 | 134,787 | 344,641 | N/A | N/A | skill 1/1; base 2/2 |
| codex | nemotron-asr-orchestrate-preflight-8khz-001 | 66,790 | 182,691 | N/A | N/A | skill 1/1; base 2/2 |
| codex | nemotron-asr-orchestrate-scope-001 | 34,837 | 32,127 | +2,710 | +8.44% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-subskill-reachability-001 | 261,571 | 115,443 | +146,128 | +126.58% | skill 1/1; base 1/1 |
| codex | nemotron-asr-orchestrate-subskills-001 | 48,854 | 196,597 | N/A | N/A | skill 1/1; base 3/3 |
| ALL AGENTS | Dataset aggregate | 4,938,360 | 7,909,912 | N/A | N/A | skill 33/33; base 44/69 |

Prompt tokens include cached reads, so total tokens are `prompt + completion` (cached is not added twice). The Efficiency score uses `(prompt - cached) + completion`. N/A means the relevant trajectory counters were not available; coverage is never estimated.

## Tier Status

| Tier | Purpose | Status | Evidence |
|---|---|---|---|
| Tier 1 | Static validation | **PASSED WITH OBSERVATIONS** | 1 validator(s); 4 finding(s) |
| Tier 2 | Semantic deduplication | **NOT RUN** | No result was recorded |
| Tier 3 | Live agent evaluation | **PASS** | 2 agent(s); 15 task(s) |

## Findings and Observations

<details>
<summary>Show detailed findings and successful checks</summary>

- **MEDIUM** SCHEMA/frontmatter_field_placement: Root field 'version' is ignored; use 'metadata.version' (`skills/nemotron-asr-finetune/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Instructions' (`skills/nemotron-asr-finetune/SKILL.md`)
- **MEDIUM** SCHEMA/body_recommended_section: Missing recommended section: '## Examples' (`skills/nemotron-asr-finetune/SKILL.md`)
- **LOW** SCHEMA/author_format: Author must be of the form 'Name <email@host>' (`skills/nemotron-asr-finetune/SKILL.md`)

</details>

## Scoring Methodology

<details>
<summary>Show dimension definitions, source signals, and thresholds</summary>

| Dimension | Question | Scored signals |
|---|---|---|
| Security | Is it safe to use? | `security` (100%) |
| Correctness | Is the answer correct? | `accuracy` (100%) |
| Discoverability | Was the right skill loaded when needed? | `skill_execution` (100%) |
| Effectiveness | Did the skill help complete the task? | `goal_accuracy` (50%) + `behavior_check` (50%) |
| Efficiency | Did it avoid wasted tool calls and token usage? | `skill_efficiency` (50%) + `token_efficiency` (50%) |

- Dimension bands: PASS at 50% or above; NEUTRAL from 40% to below 50%; FAIL below 40%.
- Overall Tier 3 lift: PASS at +5 points or more; FAIL at -10 points or less; values between those bands are NEUTRAL.
- Overall verdict: PASS only when every configured dimension passes for at least one supported agent. Lift is reported as diagnostic evidence and does not override this gate.
- The 50% attempt pass threshold is a separate per-task gate; it is not the dimension pass threshold.
- Effectiveness is the equal-weight mean of goal completion (`goal_accuracy`) and expected workflow adherence (`behavior_check`).
- Efficiency is 50% tool-call productivity (the backward-compatible `skill_efficiency` wire id) and 50% `token_efficiency`. Positive-case skill routing is scored under Discoverability, not Efficiency; a negative case without a routing target is N/A. N/A sources are omitted, remaining weights are renormalized, and the dimension is marked partial.

Signals present in this run:

- `security` (Security): unsafe operations, secret leakage, and unauthorized access.
- `skill_execution` (Skill Execution): whether the expected skill was selected, decoys were avoided, and the workflow executed.
- `skill_efficiency` (Tool Productivity): tool-call productivity (legacy wire id; routing is scored under Discoverability).
- `accuracy` (Accuracy): final-answer correctness against the reference answer.
- `goal_accuracy` (Goal Accuracy): whether the user's goal was achieved.
- `behavior_check` (Behavior Check): whether the expected workflow behavior was followed.
- `token_efficiency` (Token Efficiency): actual uncached prompt plus completion usage (50% of Efficiency).

</details>

## Freshness

Regenerate this benchmark when the skill, evaluation dataset, target agent/model, evaluator version, environment, or scoring policy changes.
