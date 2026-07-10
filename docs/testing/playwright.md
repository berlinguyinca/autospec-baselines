# Playwright Baseline Pack

## Purpose

Define expectations for browser-based end-to-end and interaction testing with Playwright.

## When To Apply

Apply this pack when Playwright is used to verify web workflows, visual behavior, accessibility-adjacent interactions, or browser integration.

## Required Capabilities

- Tests for critical user journeys.
- Stable selectors based on user-facing roles, labels, or explicit test IDs.
- Deterministic test data setup and cleanup.
- Trace, screenshot, or video capture for failures.
- No dependence on hidden manual setup.

## Recommended Capabilities

- Cross-browser coverage based on product support matrix.
- Mobile viewport coverage for responsive workflows.
- Accessibility assertions for key pages.
- Network and console error checks.
- Visual comparison for layout-sensitive surfaces.

## Metadata Requirements

- Tested browsers and viewport matrix.
- Base URL and environment assumptions.
- Test data ownership and cleanup policy.
- Flake triage owner.
- Artifact retention expectations.

## Quality Gates

- Critical paths pass in CI or documented release verification.
- Tests fail on user-visible regressions, not implementation churn.
- No persistent test pollution.
- Failure artifacts are sufficient to diagnose the issue.
- Known flaky tests are quarantined or fixed, not ignored silently.

## Testing Expectations

- Prefer role-based locators and visible outcomes.
- Assert navigation, validation, data persistence, and permission outcomes.
- Cover loading and error paths where users rely on them.
- Keep tests independent and parallel-safe where feasible.

## Documentation Expectations

- Document how to install browsers, run tests, debug traces, and update snapshots.
- Document test data and environment prerequisites.
- Document known coverage gaps.

## UI/UX Expectations

- Playwright tests should validate the experience a user actually sees: labels, focus,
  navigation, responsive layout, and recoverable failure states.

## AI Assistant Expectations

- If AI authors Playwright tests, it should inspect the running UI or markup before selecting
  locators and should not mock away the behavior the test is meant to prove.

## Implementation Issue Templates

### Add Playwright Coverage

```markdown
## Goal
Describe the workflow or regression to cover.

## Baseline Packs
- testing/playwright

## Required Evidence
- Playwright test file
- Passing trace or CI result
- Test data setup/cleanup notes

## Acceptance Criteria
- Test follows user-visible behavior
- Test is independent and repeatable
- Failure artifacts are available
```

