# Analytics Baseline Pack

## Purpose

Define expectations for systems that collect, transform, analyze, visualize, or report metrics, events, business intelligence, operational telemetry, or product usage data.

## When To Apply

Apply this pack when correctness, freshness, lineage, and interpretability of analytical data are central to the product or decision process.

## Required Capabilities

- A versioned semantic layer: metric names, owners, formulas, grain — every figure traces to a
  definition (no ad-hoc SQL metrics) (seed:
  `analytics-assets/tokens/analytics-semantic-layer.json`).
- Data lineage for sources, transformations, and outputs.
- Freshness, completeness, null-rate, and referential-integrity checks that fail before users
  rely on stale/broken output.
- Statistical honesty in outputs: zero-baseline bars, disclosed sample size and denominators,
  uncertainty on estimates, no color-only encoding.
- The analysis answers the question actually asked; methodology reviewed independently for
  consequential findings.
- Access controls for sensitive or restricted data.
- Backfill and correction procedures.

## Recommended Capabilities

- Data contracts between producers and consumers.
- Anomaly detection on critical metrics.
- Reconciliation against source-of-truth systems.
- Dashboard ownership and usage review.

## Metadata Requirements

- Metric definitions, owners, and dimensionality.
- Source systems, refresh cadence, and lineage.
- Data classification, retention, sampling rules, and known caveats.
- Dataset owners and consumers.

## Quality Gates

- Critical metrics have explicit definitions and tests; the same metric means one thing
  everywhere.
- Pipeline failures and staleness are detectable before users rely on output; dashboards
  disclose freshness and scope.
- Charts obey statistical honesty (zero-baseline bars, n and uncertainty shown, not color-only)
  and re-theme with the app.
- Restricted data is not exposed to unauthorized users; schema changes include downstream impact
  review.
- Consequential analyses record their question, method, and an independent methodology review.

## Testing Expectations

- Unit tests for transformations and metric formulas.
- Data-quality assertions (freshness, nulls, referential integrity, row-count sanity).
- Reconciliation tests against source of truth.
- Regression tests for metric-definition changes.
- Contract tests for source data expectations.
- Permission tests for sensitive datasets and dashboards.

## Documentation Expectations

- Publish the metric catalog / semantic layer.
- Document lineage, caveats, and sampling plainly enough for non-engineers.
- Record the question and method behind consequential analyses.
- Document dashboard purpose, owner, audience, and refresh cadence.

## UI/UX Expectations

- Visualizations must label units, time ranges, filters, and aggregation level.
- Dashboards should highlight stale, incomplete, or partial data.
- Users should be able to trace important numbers back to definitions.
- Avoid chart types that obscure comparison or uncertainty.

## AI Assistant Expectations

- If AI summarizes analytics, it must cite underlying data, preserve caveats, avoid unsupported
  causal claims, and distinguish observed values from inferred interpretations.

## Implementation Issue Templates

### Add Metric or Analysis

```markdown
## Goal
Describe the metric/analysis and the decision it supports.

## Baseline Packs
- application/analytics

## Required Evidence
- Metric definition in the semantic layer
- Data-quality assertions pass
- Statistical-honesty check on any chart
- Permission review
- Independent methodology review for consequential findings

## Acceptance Criteria
- Metric traces to one definition; users can identify formula, grain, and refresh cadence
- Freshness/quality gates pass
- Critical values reconcile with source data
- Dashboard communicates caveats and filters
- Charts honest and re-theme
- Method reviewed
```

### Modify Analytical Pipeline

```markdown
## Change
Describe the source, transformation, or output change.

## Baseline Packs
- application/analytics

## Required Evidence
- Downstream impact review
- Before/after reconciliation
- Backfill or migration plan

## Acceptance Criteria
- Existing consumers are not silently broken
- Historical data handling is documented
- Monitoring covers the changed path
```

---

## Gates Registry

Machine-readable in
[`analytics-assets/rules/analytics.rules.yaml`](analytics-assets/rules/analytics.rules.yaml):
freshness/quality checks, single-definition metrics, reconciliation, statistical honesty, and
the independent methodology-review gate. The semantic-layer seed is
[`analytics-assets/tokens/analytics-semantic-layer.json`](analytics-assets/tokens/analytics-semantic-layer.json).
