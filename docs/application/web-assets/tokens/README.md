# Design Tokens (DTCG seed)

`tokens.json` is a seed design-token file in the **W3C Design Tokens Community Group
(DTCG) format, version 2025.10** — the first stable version of the standard, consumed
by Figma, Tokens Studio, Style Dictionary, Terrazzo, Penpot, and others. It validates
against `https://www.designtokens.org/schemas/2025.10/format.json`.

Why the standard format matters here: a well-shaped token file is the contract that
makes generated UI look like *your product* instead of a generic default. It is the
highest-leverage artifact in the whole system.

## Structure (three tiers)

- **Tier 1 — primitives** (`color`, `space`, `radius`, `duration`): raw values in OKLCH
  and `{value, unit}` dimensions. Theme-agnostic. **Never referenced by components.**
- **Tier 2 — semantic** (`theme.light`, `theme.dark`): role-based tokens
  (`bg-canvas`, `text-primary`, `accent`, `border-subtle`, …) that reference primitives
  via `{color.gray.12}` aliases. **This is the only layer components consume.**
- Tier 3 — component tokens: add per-component overridable hooks in code as needed,
  referencing the semantic layer only.

Light and dark are **distinct designs**, not inversions — each is authored explicitly.

## Build

```bash
npm i -D style-dictionary        # v4+ has first-class DTCG support
node style-dictionary.config.mjs
```

Outputs:
- `build/css/theme-light.css` — `:root, [data-theme="light"] { --color-accent: … }`
- `build/css/theme-dark.css` — `[data-theme="dark"] { … }`
- `build/ts/tokens.ts`, `build/tailwind/tokens.tailwind.cjs`

Set the active theme before first paint with `document.documentElement.dataset.theme`,
seeded from `prefers-color-scheme` and an explicit stored choice. In modern browsers you
can additionally use `light-dark()` and `contrast-color()` directly (Baseline as of 2026;
transpile for older browsers).

## Guardrails

- A lint should forbid raw color/spacing/type literals in component code; every visual
  value traces to a semantic token.
- Renaming a semantic token is a breaking change — treat token releases with semver.
- Verify `text-muted` contrast against its background in **both** themes before shipping;
  the seed value is a starting point, not a guarantee.
