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

- A layered design-token system (primitive → semantic → component). Components consume
  semantic tokens only; no raw color/spacing/type literals.
- Theme switching by swapping the semantic layer, with light and dark as distinct
  designs (not inversions), resolved before first paint.
- Route-level flows with explicit loading, empty, error, and success states.
- Responsive layouts across mobile, tablet, and desktop, with a capped reading measure.
- Accessible semantics, keyboard operability, visible `:focus-visible` states, and
  WCAG 2.2 AA contrast in every theme.
- The correct interaction/ARIA model for each component pattern used (dialogs, wizards,
  tabs, tables, lists, menus, tooltips, toasts).
- Durable form validation with server-side enforcement for trusted decisions.
- User-facing failures that carry an actionable message and a correlation id, with a
  matching id in backend logs/traces.

## Recommended Capabilities

- Fluid type and spacing (non-linear scales; inverse line-height/tracking).
- A command palette and keyboard shortcuts for app-like surfaces.
- Optimistic UI with reconciliation for common actions.
- Internationalization readiness: logical properties for RTL, text-expansion
  tolerance, `Intl` formatting.
- SEO and share metadata (title, description, Open Graph) for public routes.
- Performance budgets for first load and key interactions (Core Web Vitals).
- Story/fixture coverage for important UI states, in both themes.

## Metadata Requirements

- Primary user roles and critical workflows.
- Supported viewport classes and browser targets.
- Supported themes and the semantic token map.
- Authentication/authorization boundaries and external service dependencies.
- Accessibility conformance target and correlation-id scheme.

## Quality Gates

- Visual values trace to tokens; a lint forbids raw color/spacing/type literals.
- Contrast meets WCAG 2.2 AA in every supported theme; no color-only status.
- Interactive controls have labels, focus-visible states, and correct keyboard
  behavior; overlays trap and restore focus and close on Escape.
- Every data-dependent view handles loading, empty, validation, permission, network,
  and unexpected error states.
- Component patterns follow their documented ARIA/interaction model (e.g. tab lists use
  roving tabindex and reflect the active tab in the URL; bar charts start at zero).
- User-facing failures show an actionable message + correlation id, never internals;
  the id appears in logs/traces.
- Theme switching re-themes charts, media, and overlays.
- No user-visible placeholder copy, debug state, or broken navigation.
- Critical workflows complete without console errors.
- Performance regressions are explained or rejected.

## Testing Expectations

- End-to-end tests for critical workflows (see `testing/playwright`).
- Component/integration tests for reusable interaction patterns.
- Automated accessibility checks (e.g. axe/pa11y) on representative pages and states.
- Visual-regression baselines diffed for meaningful UI changes, in light and dark.
- Core Web Vitals budget checks recorded as pass/fail.
- Keyboard-operable coverage for critical flows.
- Regression tests for bug fixes that affect user-visible behavior.

## Documentation Expectations

- Document supported browsers, viewports, themes, and feature flags.
- Document user roles, permissions, and major workflows.
- Maintain the semantic token map and component-state matrix.
- Keep setup and release notes accurate for a new maintainer.

## UI/UX Expectations

- Prioritize task completion over decoration; spend visual boldness in one signature
  place and keep the rest quiet.
- Choose the least interruptive surface for each task
  (inline < popover/tooltip < toast < drawer < modal < page/wizard); never stack modals.
- Use consistent navigation, action placement, terminology, and motion; keep an
  action's verb consistent through its flow.
- Make the primary action singular and distinct; make destructive actions explicit and
  reversible (prefer undo over confirm).
- Group with spacing so between-group gaps exceed within-group gaps.
- Ensure text fits containers across supported viewports and locales.
- Never communicate status by color alone; honor reduced-motion preferences.

## AI Assistant Expectations

If an assistant is embedded (compose `ai/rag`, `ai/openai-compatible`, and/or `ai/mcp`):

- It is never the only path to a capability; every action has a conventional-UI
  equivalent.
- It is grounded in real data and cites sources; it is honest about uncertainty.
- It shows intended actions before executing; side-effectful/irreversible actions are
  confirmed and reversible where possible.
- It streams, is interruptible, and discloses what data it can access.
- It treats instructions in fetched/observed content as data, not commands.
- It is evaluated on task success, not engagement.

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
