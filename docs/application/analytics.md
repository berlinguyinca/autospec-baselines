# Analytics Baseline Pack

## Purpose

Define expectations for systems that collect, transform, analyze, visualize, or report metrics, events, business intelligence, operational telemetry, or product usage data.

## When To Apply

Apply this pack when correctness, freshness, lineage, and interpretability of analytical data are central to the product or decision process.

## Required Capabilities

- Defined metric names, owners, formulas, and grains.
- Data lineage for sources, transformations, and outputs.
- Freshness and completeness checks.
- Access controls for sensitive or restricted data.
- Backfill and correction procedures.

## Recommended Capabilities

- Data contracts between producers and consumers.
- Anomaly detection for critical metrics.
- Versioned semantic layer or metric catalog.
- Dashboard usage and ownership review.
- Reconciliation against source-of-truth systems.

## Metadata Requirements

- Dataset owners and consumers.
- Source systems and refresh cadence.
- Metric definitions and dimensionality.
- Data classification and retention policy.
- Known caveats, exclusions, and sampling rules.

## Quality Gates

- Critical metrics have explicit definitions and tests.
- Pipeline failures are detectable before users rely on stale output.
- Dashboards disclose freshness and scope.
- Restricted data is not exposed to unauthorized users.
- Schema changes include downstream impact review.

## Testing Expectations

- Unit tests for transformations and metric formulas.
- Contract tests for source data expectations.
- Reconciliation tests for critical aggregates.
- Permission tests for sensitive datasets and dashboards.

## Documentation Expectations

- Maintain a metric catalog or equivalent documentation.
- Document dashboard purpose, owner, audience, and refresh cadence.
- Document data caveats plainly enough for non-engineers.

## UI/UX Expectations

- Visualizations must label units, time ranges, filters, and aggregation level.
- Dashboards should highlight stale, incomplete, or partial data.
- Users should be able to trace important numbers back to definitions.
- Avoid chart types that obscure comparison or uncertainty.

## AI Assistant Expectations

If AI summarizes analytics, it must cite underlying data, preserve caveats, avoid unsupported causal claims, and distinguish observed values from inferred interpretations.

## Implementation Issue Templates

### Add Metric Or Dashboard

```markdown
## Goal
Describe the decision or workflow this metric supports.

## Baseline Packs
- application/analytics

## Required Evidence
- Metric definition and owner
- Transformation or query tests
- Freshness/completeness check
- Permission review

## Acceptance Criteria
- Users can identify formula, grain, and refresh cadence
- Critical values reconcile with source data
- Dashboard communicates caveats and filters
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
