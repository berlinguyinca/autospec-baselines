# React Baseline Pack

## Purpose

Define expectations for projects using React for UI composition, stateful interactions, and client-side or hybrid rendering.

## When To Apply

Apply this pack when React components, hooks, context, routing, or React-based frameworks are part of the implementation surface.

## Required Capabilities

- Component boundaries that separate rendering, state, data access, and side effects.
- Accessible markup for interactive components.
- Stable state management appropriate to the scope of the feature.
- Error boundaries or equivalent recovery for risky UI regions.
- Tests for behavior, not implementation details.

## Recommended Capabilities

- Shared design primitives or component library.
- Story coverage for reusable components and important states.
- Server/client boundary documentation for hybrid frameworks.
- Performance profiling for large lists or expensive interactions.

## Metadata Requirements

- React version and framework, if any.
- Rendering mode for important routes.
- State management approach.
- Component ownership and reuse expectations.
- Supported browser targets inherited from application packs.

## Quality Gates

- No invalid hook usage.
- Components do not depend on hidden global state without documentation.
- Forms and interactive controls remain accessible.
- Loading, error, empty, and disabled states are represented.
- Large renders avoid avoidable re-render or hydration failures.

## Testing Expectations

- Unit or component tests for reusable components.
- Integration tests for stateful workflows.
- End-to-end tests for critical user journeys.
- Accessibility assertions for custom controls.

## Documentation Expectations

- Document reusable components, props, and important constraints.
- Document state ownership for complex flows.
- Document framework-specific conventions used by the project.

## UI/UX Expectations

- React abstractions should preserve predictable UI behavior.
- Client transitions must communicate pending work.
- Hydration, suspense, and optimistic updates must not create misleading state.

## AI Assistant Expectations

If AI writes or modifies React code, it should preserve existing component patterns, avoid introducing unnecessary state libraries, and verify behavior through user-visible tests.

## Implementation Issue Templates

### Add React Component Or Flow

```markdown
## Goal
Describe the UI behavior and user outcome.

## Baseline Packs
- technology/react

## Required Evidence
- Component or integration test
- Accessibility check for interactive controls
- Loading/error/empty state coverage

## Acceptance Criteria
- Component state is predictable
- UI remains accessible
- Existing design patterns are reused
```
