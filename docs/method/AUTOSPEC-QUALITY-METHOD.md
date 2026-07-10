# The Autospec Quality Method (domain-independent)

The web-design rule set was one instance of a reusable engine. Strip away "design" and the
same five-part machine encodes *any* expert domain into policy an autonomous agent can
generate against and be judged on. This document states the engine once; each domain pack and
doctrine below applies it.

## The five parts

1. **A canonical vocabulary ("tokens").** The irreducible definitions, declared once and
   referenced everywhere, never inlined. Design: colors/spacing. Engineering: contracts, error
   taxonomies, module boundaries. Analytics: the semantic layer (metric definitions).
   Data science: the feature/label/dataset registry. Finance: the chart of accounts. The test
   is always the same — *the same name means one thing everywhere, and nothing is redefined
   locally.*
2. **Canonical rules, one home each.** Principles are DRY: stated once, cross-referenced, not
   restated. Bloat dilutes the load-bearing rules.
3. **A machine-readable gate registry** (`*.rules.yaml`) splitting every check into
   `auto` (deterministic, blocks), `judge` (an *independent* model critic scoring a fixed
   rubric), and `review` (human).
4. **A generate -> evaluate -> refine loop** with two safeguards that never bend: the actor
   that produced the work never grades its own work, and refinement is a **non-regression
   ratchet** (never accept a change that lowered any gate or rubric score).
5. **The constitution/baseline seam.** Durable, stack-agnostic law (the constitution)
   separated from concrete per-context playbooks (baselines) that *compose* it — versioned and
   pinned. Baselines never redefine the constitution.

## The unifying principle: verification scales with stakes

The `judge` tier (a model critic) is reliable where quality is structurally legible and
unreliable where it depends on domain truth a model cannot verify — a critic can spot a
misleading chart; it cannot confirm a revenue figure is *correct*, only *plausible*. So:

> **The higher the stakes, the more verification shifts from `judge` toward `auto`
> (deterministic, provable) plus independent `review`, and independence stops being hygiene
> and becomes governance** — segregation of duties in finance, model governance in ML, an
> independent approver in security-sensitive changes.

This is why the same skeleton produces a playful design critic and a segregation-of-duties
control from one method.

## The evaluation loop (all domains)

`brief -> generate (from the vocabulary, real inputs) -> produce evidence for every relevant
state -> evaluate on two required tracks -> refine -> accept`. The two tracks: **deterministic
gates** (hard-block) and an **independent judge** scoring the domain rubric, given only the
artifact + brief + rubric — never the generator judging itself. Deterministic wins ties. The
evidence bundle (brief, artifacts, gate results, rubric scores) is that domain's analog of a
test suite: design screenshots, an audit workpaper, an ML model card + eval report, an
analysis's question-method-review record.

## Domain map

| Domain | Vocabulary | Highest-value gates | Judge rubric catches |
|---|---|---|---|
| Engineering / architecture | contracts, boundaries, error taxonomy | types, tests, coverage, mutation, non-regression | over-engineering, wrong abstraction, boundary violations |
| Analytics | semantic layer (metrics) | freshness, quality, reconciliation, single-definition | misleading charts, wrong method, unstated uncertainty |
| Data science / ML | feature/label/dataset registry | leakage, held-out eval, fairness, calibration, model non-regression | honest evaluation, intended-use clarity |
| Financial | chart of accounts | debits=credits, reconciliation, segregation of duties, immutable trail | disclosure, judgment on material items |
| Product | mission, personas, non-goals | acceptance criteria testable | problem clarity, scope creep |
| Documentation | glossary, doc index | examples-tested, links-valid, staleness | accuracy, findability |
| Security | trust boundaries, ASVS | secrets scan, dependency scan, secure defaults | threat coverage, least privilege |
| Operations / SRE | SLOs, runbooks | structured logs + correlation id, telemetry, health | alert signal quality, runbook actionability |

Each domain ships: constitution doctrine enrichments (principles + gates), a `*.rules.yaml`
registry (with rubric), and — where a concrete product shape exists — a baseline pack and a
vocabulary seed. Design was simply the first domain run through this engine.
