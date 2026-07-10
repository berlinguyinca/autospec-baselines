# Data Engineering Baseline Pack

> Composes the Architecture (03), Engineering (04), and Analytics (10) doctrines and the shared quality method ([`../method/AUTOSPEC-QUALITY-METHOD.md`](../method/AUTOSPEC-QUALITY-METHOD.md)); extends `application/analytics`, `technology/python`, and `technology/postgres`.

## Purpose

Expectations for systems that move and transform data through pipelines, so jobs are correct,
replayable, contract-bound, and observable.

## When To Apply

When the system ingests, transforms, or moves data through batch or streaming pipelines and
downstream analytics/models/reports depend on it.

## Required Capabilities

- Jobs are idempotent and replayable: re-running a step yields the same result and does not
  double-count.
- Data contracts between producers and consumers, with enforced schemas at boundaries.
- Schema evolution is backward-compatible or explicitly versioned; consumers are not broken
  silently.
- Backfills are bounded, idempotent, and reconcile to expected totals.
- Row-count and quality assertions catch silent data loss before downstream use.
- Lineage recorded from source through transform to output.

## Recommended Capabilities

- Orchestration with retries, backfill windows, and dependency-aware scheduling.
- Data-contract tests in CI between producers and consumers.
- Late-arriving and out-of-order data handling for streams.
- Partitioning and incremental processing for large volumes.

## Metadata Requirements

- Pipeline/DAG inventory with owners and SLAs.
- Data contracts and schemas at each boundary.
- Lineage graph.
- Data classification and retention for moved data.

## Quality Gates

- Jobs are idempotent and replayable; a re-run does not change the result.
- Schema changes are backward-compatible or versioned; a contract test proves consumers still
  parse.
- Backfills reconcile to expected totals; no silent row loss (quality assertions pass).
- Pipeline SLAs are monitored; late or failed runs alert before users rely on stale output.
- Moved PII is classified and handled per policy.

## Testing Expectations

- Idempotency/replay tests (run twice, assert equal).
- Contract tests between producers and consumers.
- Data-quality assertions (row counts, nulls, referential integrity).
- Backfill reconciliation tests.

## Documentation Expectations

- Publish the DAG inventory, contracts, and lineage.
- Document backfill and replay procedures.
- Document SLAs and on-call ownership.

## Implementation Issue Templates

### Add or Change a Pipeline

```markdown
## Goal
Describe source, transform, and consumers.

## Baseline Packs
- application/data-engineering

## Required Evidence
- Idempotency/replay test
- Contract test with consumers
- Data-quality assertions
- Backfill reconciliation (if applicable)

## Acceptance Criteria
- Re-run is a no-op on results
- Consumers unbroken
- No silent data loss
- SLA/alerting wired
```

---

## Vocabulary

Data contracts are the canonical agreement at each boundary (seed:
[`data-engineering-assets/tokens/data-contracts.json`](data-engineering-assets/tokens/data-contracts.json))
— producers and consumers reference a schema, not an ad-hoc shape per job.

## Gates Registry

Machine-readable in
[`data-engineering-assets/rules/data-engineering.rules.yaml`](data-engineering-assets/rules/data-engineering.rules.yaml):
idempotent/replayable jobs, enforced contracts, backward-compatible schema evolution,
reconciling backfills, quality assertions against silent loss, freshness SLAs, and lineage.
Judge rubric: correctness, reproducibility, contract stability, observability.
