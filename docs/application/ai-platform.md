# AI Platform Baseline Pack

## Purpose

Define expectations for products that expose AI capabilities as a primary feature, including assistants, agent systems, model gateways, prompt tooling, evaluation platforms, and AI workflow builders.

## When To Apply

Apply this pack when model behavior, prompt configuration, retrieval, tool use, evaluation, or AI safety materially affects user outcomes.

## Required Capabilities

- Clear separation between system policy, developer instructions, user input, retrieved context, and tool results.
- Prompt and model configuration versioning.
- Evaluation coverage for core tasks and known failure modes.
- Audit trail for model calls that affect important decisions.
- Abuse, injection, and data leakage mitigations.

## Recommended Capabilities

- Offline replay of representative AI interactions.
- Golden datasets for regression comparison.
- Red-team scenarios for prompt injection, refusal bypass, and unsafe tool use.
- Cost, latency, and quality dashboards.
- Model fallback strategy with documented tradeoffs.

## Metadata Requirements

- Supported models and providers.
- Prompt ownership and version identifiers.
- Tool access boundaries.
- Data retention, privacy, and logging policy.
- Evaluation datasets and acceptance thresholds.

## Quality Gates

- System instructions cannot be overridden by ordinary user or retrieved content.
- Tool calls require explicit schemas and least-privilege permissions.
- Sensitive data is not included in prompts unless justified and documented.
- Model outputs that drive actions are validated before execution.
- Quality, latency, and cost expectations are measured for release-critical paths.

## Testing Expectations

- Regression evaluations for canonical tasks.
- Safety tests for injection and data exfiltration attempts.
- Tool-use tests covering allowed, denied, malformed, and failing calls.
- Human review for high-impact assistant behavior changes.

## Documentation Expectations

- Document model/provider choices and fallback behavior.
- Document prompt and tool contracts.
- Document evaluation methodology and known limitations.
- Document user-facing AI limitations without overstating reliability.

## UI/UX Expectations

- Show AI-generated content as generated, not authoritative by default.
- Give users a way to correct, retry, stop, or inspect assistant work.
- Make long-running AI work observable.
- Preserve citations, provenance, or reasoning summaries when the workflow depends on source material.

## AI Assistant Expectations

- Follow a stable instruction hierarchy.
- Ask for clarification when ambiguity could cause harmful or irreversible outcomes.
- Use tools only when needed and only within documented boundaries.
- Report uncertainty and known gaps.
- Avoid fabricating citations, actions, or verification evidence.

## Implementation Issue Templates

### Add AI Capability

```markdown
## Goal
Describe the AI capability and user outcome.

## Baseline Packs
- application/ai-platform

## Required Evidence
- Prompt/model configuration diff
- Evaluation results for canonical tasks
- Safety test results
- Tool access review, if tools are used

## Acceptance Criteria
- Core task quality meets the documented threshold
- Unsafe or unauthorized tool behavior is blocked
- Data handling matches the documented policy
- Known limitations are documented
```

### Change Prompt Or Model

```markdown
## Change
Describe the prompt, provider, model, or parameter change.

## Baseline Packs
- application/ai-platform

## Required Evidence
- Before/after evaluation comparison
- Cost and latency impact
- Review of safety-sensitive scenarios

## Acceptance Criteria
- Quality does not regress on required evaluations
- Tradeoffs are documented
- Rollback path is clear
```
