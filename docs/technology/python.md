# Python Baseline Pack

## Purpose

Define expectations for Python services, libraries, scripts, data workflows, CLIs, and automation used in Autospec-managed projects.

## When To Apply

Apply this pack when Python is used for product code, backend services, data processing, scientific work, automation, or tests.

## Required Capabilities

- Explicit runtime version and dependency management.
- Clear module boundaries and import structure.
- Typed interfaces for important data structures and public functions.
- Structured error handling for external IO and user inputs.
- Repeatable test execution.

## Recommended Capabilities

- Static type checking for production modules.
- Formatting and linting conventions.
- Dependency vulnerability review.
- CLI entry points for operational scripts.
- Structured logging for services and long-running jobs.

## Metadata Requirements

- Supported Python versions.
- Package manager and lockfile policy.
- Runtime environment assumptions.
- Public module/API ownership.
- External service and data dependencies.

## Quality Gates

- Tests pass from a clean checkout.
- Dependency changes are justified and minimal.
- Public functions validate inputs or document preconditions.
- Long-running tasks handle interruption and retryable failure.
- Secrets are not read from source-controlled files.

## Testing Expectations

- Unit tests for pure logic.
- Integration tests for external boundaries where feasible.
- Regression tests for bug fixes.
- Fixture strategy for data-heavy tests.

## Documentation Expectations

- Document setup, test, and run commands.
- Document configuration and environment variables.
- Document public APIs, CLI usage, or operational jobs.

## UI/UX Expectations

- For Python CLIs, show clear help text, input validation errors, progress for long operations,
  and non-zero exits for failure.

## AI Assistant Expectations

- If AI modifies Python code, it should preserve existing project tooling, avoid unrequested
  dependencies, and run the narrowest meaningful verification before broader checks.

## Implementation Issue Templates

### Add Python Capability

```markdown
## Goal
Describe the Python module, service, script, or workflow.

## Baseline Packs
- technology/python

## Required Evidence
- Unit or integration tests
- Type or lint result when configured
- Setup/run documentation update

## Acceptance Criteria
- Behavior is covered by tests
- Dependencies are documented and justified
- Errors are handled at external boundaries
```

