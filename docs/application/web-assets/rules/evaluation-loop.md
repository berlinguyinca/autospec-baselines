# Evaluation & Refinement Loop

This is the executable half of "automatically design and refine." The ruleset says
*what* good looks like; `rules.yaml` makes it enumerable; this file defines the loop
that generates against it and judges the result. It is designed to plug into autospec's
generate → validate → evidence → refine flow.

## The loop

```
brief ──▶ generate ──▶ render ──▶ evaluate ──▶ refine ──▶ (render …) ──▶ accept
                                     │  ▲                        │
                                     │  └── independent critic ──┘
                                     └── deterministic gates ─────
```

1. **Brief.** Before generating, pin subject, audience, and the single signature element
   (see ruleset §35). Prefer *asking a clarifying question* over guessing — research shows
   experts strongly prefer a proactive agent here, and it measurably improves output. The
   brief is an artifact and a gate (`direction.brief-pinned`).
2. **Generate.** Produce UI composed from the semantic token layer and headless
   primitives (ruleset §2, §25). Real, on-domain content — never lorem ipsum.
3. **Render.** Build and screenshot each key page and **each container state**
   (loading/empty/error/success) in **each theme** (light/dark), at desktop and a
   mid-tier mobile profile.
4. **Evaluate** — two independent tracks, both required:
   - **Deterministic gates** (`check: auto` in rules.yaml): axe-core, Lighthouse/CWV,
     contrast per theme, token-lint, security headers, Playwright visual-diff and
     keyboard/state assertions. These are hard pass/fail and block acceptance.
   - **Design critique** (`check: vlm`): an independent vision-language critic scores the
     screenshots against the rubric below. Produces scores + written evidence, not a hard
     gate — but a low score routes back to refine.
5. **Refine.** Address failed gates and low-scoring rubric dimensions, then re-render.
6. **Accept** only when all `blocker`/`major` auto gates pass, the rubric is at or above
   threshold, and **no gate regressed** versus the previous iteration.

## The independent-critic guard (important)

Do **not** let the model that generated the UI grade its own work. Evidence is clear that
LLMs are unreliable self-judges — self-critique can *degrade* quality, and vision judges
carry position bias. Mitigations, all required:

- **Separation:** the critic is a different model instance/role than the generator, given
  only the screenshots, the brief, and the rubric — not the generation reasoning.
- **Rubric-anchored:** the critic scores fixed dimensions (below), not an open-ended
  "is this good?", which reduces drift and bias.
- **Non-regression:** track scores and gate results as state across iterations; never
  accept a refinement that lowered any gate or rubric dimension. This turns an unreliable
  judge into a monotonic ratchet.
- **Bias control:** when comparing two variants, randomize/swap presentation order and
  require the critic to justify against evidence in the image, not position.
- **Deterministic wins ties:** where an auto gate and the critic disagree, the auto gate
  is authoritative (a computed contrast failure outranks "looks fine").

## Design-critique rubric (VLM critic)

Score each 1–5 with a one-line justification citing visible evidence. Threshold: no
dimension below 3; mean ≥ 4 to accept.

| Dimension | What "5" looks like |
|---|---|
| Visual hierarchy | One clear focal point; eye path matches importance; a singular, distinct primary action. |
| Spacing discipline | Consistent rhythm; between-group gaps clearly exceed within-group; nothing cramped or arbitrary. |
| Color restraint | Neutrals-first; one accent used for emphasis only; correct and legible in both themes. |
| Typographic craft | Coherent scale; tight display leading/tracking; capped measure; no orphan/widow mess. |
| Alignment & grid | Elements align to a shared grid; intentional grid-breaks read as deliberate, not accidental. |
| State completeness | Loading/empty/error/success all present and considered, not just the happy path. |
| Content realism | Copy is domain-specific and user-side; no placeholder text; labels name what users control. |
| Anti-sameness | Does **not** read as a generic AI-default template (cream+serif+terracotta, black+acid accent, or broadsheet); the signature element is present. |
| Accessibility (visual) | Status not color-only; focus visible; contrast comfortable; text fits containers. |
| Coherence | Reads as one product: consistent components, vocabulary, and motion. |

## Wiring into autospec

- Each `rules.yaml` entry becomes a validation gate or a piece of review evidence.
- `check: auto` → autospec validation gates (block merge).
- `check: vlm` → a critique step producing recorded evidence + scores in the closeout.
- `check: review` → human/agent review checklist items.
- The brief, screenshots (per state/theme), gate results, and rubric scores are the
  **review evidence** attached to the PR. The non-regression state is the memory that
  keeps the refine loop honest across iterations.
