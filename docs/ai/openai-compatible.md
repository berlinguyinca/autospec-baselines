# OpenAI-Compatible API Baseline Pack

## Purpose

Define expectations for systems that integrate with OpenAI-compatible chat, responses, embeddings, image, audio, or tool-calling APIs across hosted or self-hosted providers.

## When To Apply

Apply this pack when code targets an OpenAI-style API contract, including official OpenAI services or providers exposing compatible endpoints.

## Required Capabilities

- Provider, endpoint, model, and API version metadata.
- Request and response schema handling.
- Timeout, retry, and rate-limit behavior.
- Secret management outside source control.
- Evaluation coverage for provider or model changes.

## Recommended Capabilities

- Provider abstraction only when multiple providers are actually required.
- Cost and token usage tracking.
- Structured output validation.
- Idempotency strategy for retried action-producing requests.
- Canary tests for model upgrades.

## Metadata Requirements

- Provider name and compatibility scope.
- Model identifiers and default parameters.
- Authentication and secret storage method.
- Rate limits, quotas, and expected cost envelope.
- Data retention and privacy terms relevant to the provider.

## Quality Gates

- Requests do not log secrets or unnecessary sensitive content.
- Responses are validated before downstream use.
- Retries do not duplicate irreversible actions.
- Provider-specific behavior is documented where compatibility differs.
- Model changes include quality, cost, and latency comparison.

## Testing Expectations

- Contract tests using recorded or test-provider responses where appropriate.
- Failure tests for timeouts, malformed responses, and rate limits.
- Evaluation tests for task quality.
- Secret-leak checks in logs and fixtures.

## Documentation Expectations

- Document configuration, required environment variables, and provider assumptions.
- Document model selection and upgrade procedure.
- Document known compatibility gaps.

## UI/UX Expectations

- User-facing flows should show pending, retry, failure, and degraded states for provider issues.
- Costly or long-running actions should communicate progress and limits.

## AI Assistant Expectations

The assistant must respect provider limitations, validate structured outputs, avoid fabricating tool results, and clearly separate model-generated content from verified data.

## Implementation Issue Templates

### Add OpenAI-Compatible Integration

```markdown
## Goal
Describe the model-powered workflow and provider.

## Baseline Packs
- ai/openai-compatible

## Required Evidence
- Provider/model configuration
- Failure and rate-limit handling tests
- Evaluation results for representative tasks
- Secret handling review

## Acceptance Criteria
- Provider behavior is documented
- Responses are validated before use
- Cost, latency, and quality tradeoffs are known
```
