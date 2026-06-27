# Ollama Baseline Pack

## Purpose

Define expectations for systems that use Ollama to run local or self-hosted models.

## When To Apply

Apply this pack when project behavior depends on Ollama model serving, local model files, model tags, hardware constraints, or offline AI workflows.

## Required Capabilities

- Explicit model names, tags, and expected context sizes.
- Hardware and runtime requirements.
- Startup, health, and failure handling.
- Prompt and output compatibility tests for selected models.
- Clear fallback or degradation behavior when Ollama is unavailable.

## Recommended Capabilities

- Model checksum or provenance tracking.
- Performance benchmarks for target hardware.
- Separate profiles for development and production-like environments.
- Resource limits and concurrency expectations.
- Local data privacy review.

## Metadata Requirements

- Ollama version range.
- Model tags and source.
- CPU/GPU, memory, and disk requirements.
- Expected latency and throughput.
- Offline and network access assumptions.

## Quality Gates

- The selected model is available before dependent workflows run.
- Output quality is evaluated for the intended task.
- Resource usage does not make the host unstable.
- Failures are visible and recoverable.
- Local model use does not bypass data handling policy.

## Testing Expectations

- Health checks for the Ollama service.
- Smoke tests for model loading and representative prompts.
- Timeout and unavailable-service tests.
- Performance checks for target hardware where release-critical.

## Documentation Expectations

- Document install, pull, run, and troubleshooting steps.
- Document model selection rationale and limitations.
- Document hardware expectations and known performance tradeoffs.

## UI/UX Expectations

- Long local model operations should show progress or pending state.
- Users should know when local model quality or availability is degraded.

## AI Assistant Expectations

Assistants using Ollama must account for model-specific limits, avoid claiming hosted-model capabilities unless verified, and surface uncertainty when local model quality is lower than expected.

## Implementation Issue Templates

### Add Ollama-backed Capability

```markdown
## Goal
Describe the local model workflow.

## Baseline Packs
- ai/ollama

## Required Evidence
- Model tag and runtime requirements
- Health and unavailable-service tests
- Representative prompt evaluation
- Performance notes on target hardware

## Acceptance Criteria
- Workflow degrades clearly when Ollama is unavailable
- Model behavior meets documented expectations
- Setup instructions reproduce the local environment
```
