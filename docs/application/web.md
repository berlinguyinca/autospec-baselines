# Web Application Baseline Pack

## Purpose

Define expectations for user-facing browser applications, including public sites, authenticated web apps, dashboards, and transactional product interfaces.

## When To Apply

Apply this pack when users interact with the system primarily through a web browser and the release quality depends on responsive layout, accessible UI, stable navigation, and predictable client/server behavior.

## Required Capabilities

- Route-level product flows with clear loading, empty, error, and success states.
- Responsive layouts for mobile, tablet, and desktop viewports.
- Accessible keyboard navigation and semantic structure.
- Durable form validation with server-side enforcement for trusted decisions.
- Observable user-facing failures with actionable diagnostics.

## Recommended Capabilities

- Design tokens for color, spacing, typography, and focus states.
- Story or fixture coverage for important UI states.
- Progressive enhancement for critical workflows.
- Performance budgets for first load and key interactions.
- Browser compatibility matrix based on the product audience.

## Metadata Requirements

- Primary user roles and critical workflows.
- Supported viewport classes and browser targets.
- Authentication and authorization boundaries.
- External service dependencies visible to users.
- Accessibility conformance target.

## Quality Gates

- Critical workflows complete without console errors.
- UI handles loading, empty, validation, permission, network, and unexpected error states.
- Interactive controls have labels, focus states, and keyboard behavior.
- No user-visible placeholder copy, debug state, or broken navigation.
- Performance regressions are explained or rejected.

## Testing Expectations

- End-to-end tests for critical workflows.
- Component or integration tests for reusable interaction patterns.
- Accessibility checks for representative pages.
- Regression tests for bug fixes that affect user-visible behavior.

## Documentation Expectations

- Document supported browsers, environments, and feature flags.
- Document user roles, permissions, and major workflows.
- Keep setup and release notes accurate enough for a new maintainer.

## UI/UX Expectations

- Prioritize task completion over decorative layout.
- Use consistent navigation, action placement, and terminology.
- Make destructive actions explicit and reversible where possible.
- Ensure text fits containers across supported viewports.
- Avoid inaccessible color-only status communication.

## AI Assistant Expectations

If an assistant is embedded in the UI, it must disclose limits, preserve user context safely, support interruption or correction, and avoid making irreversible changes without clear confirmation.

## Implementation Issue Templates

### Add Web Workflow

```markdown
## Goal
Describe the user workflow and business outcome.

## Baseline Packs
- application/web

## Required Evidence
- Responsive screenshots or visual verification
- End-to-end test for the happy path
- Error/empty/loading state coverage
- Accessibility check result

## Acceptance Criteria
- Users can complete the workflow on supported viewports
- Invalid input is handled clearly
- Failures are visible and recoverable
- No console errors during the tested flow
```

### Fix Web Regression

```markdown
## Regression
Describe the broken user-facing behavior.

## Baseline Packs
- application/web

## Required Evidence
- Reproduction before fix
- Regression test after fix
- Screenshot or trace of corrected behavior

## Acceptance Criteria
- Original regression cannot recur under the test
- Related loading/error states remain intact
```
