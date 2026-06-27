# autospec-baselines

Public baseline data, reference outputs, and comparison artifacts for the autospec ecosystem.

This repository works with `berlinguyinca/autospec` by holding reusable baselines outside the implementation repository. Autospec workflows can compare generated outputs, quality measurements, regression evidence, and evaluation results against these stored references.

## Relationship to autospec

- `autospec` implements the automation that produces and validates outputs.
- `autospec-baselines` stores baseline artifacts that should remain easy to inspect, version, and compare.
- Changes here should be reviewable as evidence updates, not hidden inside implementation diffs.

