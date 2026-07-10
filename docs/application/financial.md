# Financial Integrity Baseline Pack

> Composes the Financial Integrity Doctrine (18), the Security & Privacy (11), Operations (12), and Analytics (10) doctrines, and the shared quality method ([`../method/AUTOSPEC-QUALITY-METHOD.md`](../method/AUTOSPEC-QUALITY-METHOD.md)); extends `technology/python` and `technology/postgres`.

## Purpose

Expectations for systems that record, calculate, reconcile, or report financial results, so
numbers are correct, controlled, auditable, and reproducible.

## When To Apply

When the system posts, calculates, reconciles, or reports monetary amounts, balances, or
financial metrics, and their correctness, controls, and auditability affect decisions,
filings, or obligations.

## Required Capabilities

- A canonical chart of accounts, entity, and currency vocabulary; every figure traces to a
  defined account/metric (no ad-hoc amounts).
- The accounting identity holds (debits equal credits) and reconciliations tie to a source of
  truth.
- Segregation of duties: the actor that records or generates a figure is never the actor that
  approves it.
- An immutable, timestamped audit trail (who/what/when) for every posting and adjustment,
  distinct from debug logs.
- Deterministic recomputation from inputs; results reproducible from versioned inputs and
  formulas.
- Materiality and judgment items routed to human review with recorded rationale.

## Recommended Capabilities

- Variance analysis against budget/prior period with explained drivers.
- Automated reconciliation with categorized reconciling items.
- Period-close checklist with dependency sequencing.
- Point-in-time restatement/roll-forward support.

## Metadata Requirements

- Chart of accounts, entities, and currencies.
- Source-of-truth systems and reconciliation mappings.
- Approval matrix (who may approve what) and materiality thresholds.
- Retention and access policy for financial records and audit trail.

## Quality Gates

- Debits equal credits on every entry; trial balance nets to zero.
- Reconciliations tie out or reconciling items are itemized and explained.
- No posting is approved by its creator (segregation of duties enforced).
- The audit trail is complete, immutable, and free of secrets/PII beyond what the record
  requires.
- Figures recompute deterministically from versioned inputs; a restatement is reproducible.
- Amounts above materiality carry a human-reviewed rationale.

## Testing Expectations

- Unit tests for every formula and posting rule with known-answer fixtures.
- Reconciliation tests against source-of-truth snapshots.
- Property tests for identities (balances net to zero; roll-forward continuity).
- Regression tests guarding prior periods against silent change.

## Documentation Expectations

- Document accounting treatments, formulas, and their sources.
- Document the approval matrix, materiality thresholds, and reconciliation procedures.
- Keep an audit-ready workpaper trail for generated figures.

## AI Assistant Expectations

- An assistant may draft entries, analyses, or explanations but must never post, approve, or
  alter financial records without an independent human approver.
- Deterministic checks outrank model judgment on any figure; the assistant surfaces the check
  result, not a guess.

## Implementation Issue Templates

### Add Financial Calculation

```markdown
## Goal
Describe the figure, its accounts, and the decision it supports.

## Baseline Packs
- application/financial

## Required Evidence
- Known-answer unit tests
- Reconciliation to a source of truth
- Segregation of duties: creator != approver
- Deterministic recomputation from versioned inputs

## Acceptance Criteria
- Debits=credits / balances net to zero
- Ties to source of truth or reconciling items explained
- Immutable audit-trail entry created
- Material amounts carry reviewed rationale
```

### Month-End Reconciliation

```markdown
## Goal
Reconcile <account> to <source>.

## Baseline Packs
- application/financial

## Required Evidence
- Tie-out or itemized reconciling items with cause
- Independent reviewer sign-off

## Acceptance Criteria
- Balance ties or is fully explained
- Reconciling items categorized
```

---

## Vocabulary

The chart of accounts, entities, and currencies are the canonical vocabulary (seed:
[`financial-assets/tokens/financial-coa.json`](financial-assets/tokens/financial-coa.json)).
Every figure references an account; no ad-hoc amounts.

## Gates Registry

Machine-readable in
[`financial-assets/rules/financial.rules.yaml`](financial-assets/rules/financial.rules.yaml):
balanced entries, reconciliation tie-out, segregation of duties (approver != creator),
immutable audit trail, deterministic recompute, no PII in the trail, and materiality review.
Deterministic checks outrank model judgment; the independent judge scores accuracy, controls,
auditability, reproducibility, and disclosure.

## Evidence

The audit workpaper is this domain's evidence bundle: the figure, its accounts and inputs,
the tie-out, the approver, and the recomputation.
