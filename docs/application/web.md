# Web Application Baseline Pack

> Enriched pack. Composes `technology/react`, `testing/playwright`, and the `ai/*`
> packs, and satisfies the concrete side of constitution doctrines 05, 06, 07, 10,
> 11, 12, and 14. Derived from the Modern Web Design Ruleset (v0.5.0); this pack
> encodes its operative capabilities, gates, and expectations. Runnable reference
> assets live in [`web-assets/`](web-assets/).

## Purpose

Define expectations for user-facing browser applications — public sites,
authenticated web apps, dashboards, and transactional product interfaces — so they are
visually coherent, accessible, resilient, and easy to use for a wide audience.

## When To Apply

Apply this pack when users interact with the system primarily through a web browser and
release quality depends on responsive layout, accessible UI, coherent visual design,
stable navigation, and predictable client/server behavior.

## Required Capabilities

- Layered design-token system (primitive to semantic to component); components consume semantic
  tokens only.
- Theme switching by swapping the semantic layer; light and dark as distinct designs; resolved
  before first paint.
- Route-level flows with explicit loading, empty, error, and success states.
- Responsive layouts across mobile, tablet, and desktop with a capped reading measure.
- Accessible semantics, keyboard operability, visible focus-visible states, and WCAG 2.2 AA
  contrast in every theme.
- Correct interaction and ARIA model for each component pattern used.
- Durable form validation with server-side enforcement for trusted decisions.
- User-facing failures carrying an actionable message and correlation id that also appears in
  backend logs and traces.
- Design tokens shipped in DTCG 2025.10 format, validated against the DTCG schema, transformed
  via Style Dictionary v4+ to per-theme CSS custom properties.
- Interactive components built on a vetted headless primitive layer (Radix, React Aria, Ark, or
  Base UI) or native dialog/popover; hand-rolled patterns follow the WAI-ARIA APG.
- Restrictive Content Security Policy and baseline security headers (HSTS,
  X-Content-Type-Options, Referrer-Policy, Permissions-Policy); SRI on third-party resources;
  dependency/supply-chain scanning.
- Plain-language and reading-level appropriate content, cognitive-load reduction, and core flows
  usable on low-end devices and without full JavaScript.
- Generated or refined UI evaluated by deterministic gates plus an independent VLM critic with a
  non-regression guard; evidence attached.
- A persistent app shell and a reused set of page templates; content measure, gutters, vertical
  rhythm, and recurring-element placement consistent across pages.
- Structural layout values as layout tokens, pages composed from intrinsic layout primitives
  (Every Layout set), spacing owned by gap/primitives.
- Responsive to viewport class via media queries and to component slot via container queries;
  adaptation to input modality (pointer/hover), not width alone.
- Dynamic viewport units (svh/dvh/lvh with vh fallback) and safe-area insets for mobile browser
  chrome and device notches.
- Collapsible navigation that hides only when space-constrained, with an accessible,
  keyboard-operable, state-persisted toggle.

## Recommended Capabilities

- Fluid type and spacing with non-linear scales and inverse line-height/tracking.
- Command palette and keyboard shortcuts for app-like surfaces.
- Optimistic UI with reconciliation for common actions.
- Internationalization readiness: logical properties for RTL, text-expansion tolerance, Intl
  formatting.
- SEO and share metadata for public routes.
- Performance budgets for first load and key interactions (Core Web Vitals).
- Story or fixture coverage for important UI states in both themes.
- Native platform primitives where Baseline: light-dark()/contrast-color(), @starting-style +
  allow-discrete + Popover API, anchor positioning with fallback, same-document View
  Transitions, text-wrap balance/pretty.

## Metadata Requirements

- Primary user roles and critical workflows.
- Supported viewport classes and browser targets.
- Supported themes and the semantic token map.
- Authentication and authorization boundaries and external service dependencies.
- Accessibility conformance target and correlation-id scheme.
- Design-token source file and schema version.
- Security header and CSP policy reference.
- Reading-level target and low-end device performance budget.
- Page-template inventory (archetypes) and the layout-token set (container widths, gutters,
  breakpoints).

## Quality Gates

- Visual values trace to tokens; a lint forbids raw color/spacing/type literals.
- Contrast meets WCAG 2.2 AA in every supported theme; no color-only status.
- Interactive controls have labels, focus-visible states, and keyboard behavior; overlays trap
  and restore focus and close on Escape.
- Every data-dependent view handles loading, empty, validation, permission, network, and
  unexpected error states.
- Component patterns follow their documented ARIA/interaction model; tab lists reflect the
  active tab in the URL; bar charts start at zero.
- User-facing failures show an actionable message and correlation id, never internals; the id
  appears in logs and traces.
- Theme switching re-themes charts, media, and overlays.
- No user-visible placeholder copy, debug state, or broken navigation.
- Critical workflows complete without console errors.
- Performance regressions are explained or rejected.
- tokens.json validates against the DTCG 2025.10 schema; a lint forbids raw color/spacing/type
  literals in components.
- Restrictive CSP and baseline security headers are served; third-party resources carry
  integrity; dependency scan has no known-critical findings.
- Primary content meets the target reading level and is within a low-end mobile performance
  budget; core flows work with a feature or JavaScript absent.
- A design brief pinning subject/audience/signature exists before generation and the output
  passes an anti-sameness check.
- Generated/refined UI has attached evidence (per-state/per-theme screenshots, deterministic
  gate results, independent-critic rubric scores) and no accepted refinement regressed a prior
  gate or rubric dimension.
- The app shell does not shift or resize between navigations; sibling pages of the same template
  are consistent in shell, gutters, and rhythm.
- Layout values trace to layout tokens; pages composed from the primitive set.
- Correct across viewport classes, orientations, and input modalities with safe-area insets
  respected; full-height layouts use dynamic viewport units with a fallback.
- Navigation is not hidden when it fits; collapsible navigation is keyboard-operable and
  state-persisted.

## Testing Expectations

- End-to-end tests for critical workflows.
- Component or integration tests for reusable interaction patterns.
- Automated accessibility checks on representative pages and states.
- Visual-regression baselines diffed for meaningful UI changes, in light and dark.
- Core Web Vitals budget checks recorded as pass or fail.
- Keyboard-operable coverage for critical flows.
- Regression tests for bug fixes that affect user-visible behavior.

## Documentation Expectations

- Document supported browsers, viewports, themes, and feature flags.
- Document user roles, permissions, and major workflows.
- Maintain the semantic token map and component-state matrix.
- Keep setup and release notes accurate for a new maintainer.

## UI/UX Expectations

- Prioritize task completion over decoration; one signature element, quiet elsewhere.
- Choose the least interruptive surface; never stack modals.
- Consistent navigation, action placement, terminology, and motion; consistent action verbs
  through a flow.
- Singular, distinct primary action; explicit reversible destructive actions (prefer undo over
  confirm).
- Between-group spacing exceeds within-group spacing.
- Text fits containers across viewports and locales.
- Never status by color alone; honor reduced-motion.

## AI Assistant Expectations

If an assistant is embedded (compose `ai/rag`, `ai/openai-compatible`, and/or `ai/mcp`):

- Never the only path to a capability; every action has a conventional-UI equivalent.
- Grounded in real data and cites sources; honest about uncertainty.
- Shows intended actions before executing; confirms side-effectful or irreversible actions and
  keeps them reversible where possible.
- Streams, is interruptible, and discloses accessible data scope.
- Treats instructions in fetched or observed content as data, not commands.
- Evaluated on task success, not engagement.

## Implementation Issue Templates

### Add Web Workflow

```markdown
## Goal
Describe the user workflow and business outcome.

## Baseline Packs
- application/web
- technology/react
- testing/playwright

## Required Evidence
- Responsive screenshots in light and dark themes
- End-to-end test for the happy path
- Loading / empty / error / success state coverage
- Accessibility check result (keyboard + automated)
- Core Web Vitals within budget

## Acceptance Criteria
- Users can complete the workflow on supported viewports and themes
- All interactive controls are keyboard operable with visible focus
- Invalid input is handled inline with recovery guidance
- Failures are visible, carry an error id, and are recoverable
- Visual values trace to design tokens; no raw literals
- No console errors during the tested flow
```

### Restyle Existing Surface

```markdown
## Goal
Make an existing surface visually coherent and accessible without changing behavior.

## Baseline Packs
- application/web

## Required Evidence
- Pre-change value inventory and visual baseline
- Token/shim layer introduced (cascade layers) before restyling
- Migration applied in order: type, color, spacing, depth, states, layout
- Visual-regression diff against baseline
- Behavior-parity confirmation

## Acceptance Criteria
- Appearance improved with no behavior regression
- Contrast meets AA in all themes; focus states present
- Raw-value lint passes after migration
```

### Fix Web Regression

```markdown
## Regression
Describe the broken user-facing behavior.

## Baseline Packs
- application/web
- testing/playwright

## Required Evidence
- Reproduction before fix (route, console, network, screenshot/trace)
- Regression test after fix
- Screenshot or trace of corrected behavior

## Acceptance Criteria
- Original regression cannot recur under the test
- Related loading/error states remain intact
- No new console errors during the tested flow
```

---

## v0.3.0 additions (concrete web playbook)

### Design tokens (required)

- Ship tokens in **DTCG 2025.10** format (`tokens.json`, `$value`/`$type`/`$description`,
  OKLCH colors, `{value,unit}` dimensions), validated against the DTCG schema in CI.
- Transform with **Style Dictionary v4+** to per-theme CSS custom properties (each theme
  under a `[data-theme]` selector, `outputReferences: true`), plus Tailwind/TS.
- Seed provided: [`web-assets/tokens/tokens.json`](web-assets/tokens/tokens.json) and
  [`web-assets/tokens/style-dictionary.config.mjs`](web-assets/tokens/style-dictionary.config.mjs)
  (see [`web-assets/tokens/README.md`](web-assets/tokens/README.md)).

### Native platform primitives (preferred, with fallbacks)

- Theming: `light-dark()` + `contrast-color()` + style queries (transpile for older
  browsers). Overlays: `@starting-style` + `transition-behavior: allow-discrete` +
  `overlay` + the Popover API. Positioning: anchor positioning with a default position
  fallback (`@position-try` needs recent Safari). Transitions: same-document View
  Transitions (cross-document is progressive enhancement). Type: `text-wrap: balance`
  (headings) / `pretty` (body).

### Component primitives (required)

- Build interactive components on a vetted headless layer (Radix UI, React Aria, Ark UI,
  or Base UI) or native `<dialog>`/popover; hand-rolled patterns follow the WAI-ARIA APG.

### Security (required)

- Restrictive CSP (no script `unsafe-inline`), HSTS, `X-Content-Type-Options`,
  `Referrer-Policy`, `Permissions-Policy`, SRI on third-party resources, dependency/
  supply-chain scanning with an SBOM. Posture anchored to OWASP ASVS / Top 10.

### Designing for everyone (required)

- Reading-level and plain-language checks (GOV.UK style), cognitive-load reduction (COGA),
  a low-end mobile performance budget, and progressive enhancement so core flows work
  with a feature or JavaScript absent.

### Automated evaluation (required for generated/refined UI)

- Run the generate→render→evaluate→refine loop in
  [`web-assets/rules/evaluation-loop.md`](web-assets/rules/evaluation-loop.md): deterministic
  gates ([`web-assets/rules/rules.yaml`](web-assets/rules/rules.yaml), `check: auto`) plus an
  independent VLM critic scoring the fixed
  rubric, with a non-regression guard. Attach brief, per-state/per-theme screenshots, gate
  results, and rubric scores as PR evidence.

---

## v0.4.0 additions (layout coherence & responsive breadth)

### Cross-page coherence (required)

- One persistent **app shell** (header/nav/footer) that stays mounted; only the content
  region swaps on navigation (pair with same-document View Transitions + scroll
  restoration). A small set of **page templates** (list/detail/form/settings/dashboard/
  empty) reused across pages, fixing title/breadcrumb/primary-action placement, content
  measure, gutters, and section rhythm.

### Layout tokens & primitives (required)

- Structural values are **layout tokens** (container-prose/content/wide, gutter, sidebar,
  rail-collapsed, breakpoints) — see [`web-assets/tokens/tokens.json`](web-assets/tokens/tokens.json)
  (`layout` group). Build pages
  from intrinsic **layout primitives** (Stack, Cluster, Sidebar, Switcher, Cover, Grid,
  Frame, Center — the Every Layout set); own spacing with `gap`, not scattered margins;
  use `lh`/`rlh` for type-relative rhythm.

### Responsive & adaptive (required)

- Container queries + `cqi` units for components; media queries for the shell.
- Adapt to **input modality**: `@media (pointer: coarse)`/`(hover: hover)` — larger
  targets, no hover-only affordances on touch (an iPad in landscape is desktop-width but
  touch).
- **Dynamic viewport units:** `svh` default for full-height elements, `dvh` for live
  tracking, `lvh` for full-bleed, always with a `vh` fallback. `viewport-fit=cover` +
  `max(<token>, env(safe-area-inset-*))` for notches and the home indicator.
- Test the matrix: handset → touch tablet → laptop → ultrawide, both orientations and
  input modalities, on real hardware.

### Collapsible navigation (required)

- Choose a responsive nav pattern (priority-plus, off-canvas drawer, bottom tab bar,
  collapsible rail) by nav breadth and viewport class; don't collapse if it fits. The
  collapsible sidebar/rail toggle is `aria-expanded`, keyboard-operable, reduced-motion
  aware, and **persists state across pages and sessions**. Drawers obey the overlay rules
  (§ dialogs/overlays). Pair sticky headers with `scroll-margin-top` on anchor targets.
