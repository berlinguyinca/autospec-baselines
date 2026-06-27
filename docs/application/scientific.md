# Scientific Baseline Pack

## Purpose

Define expectations for software used in scientific, research, modeling, simulation, laboratory, or reproducibility-sensitive contexts.

## When To Apply

Apply this pack when results may inform scientific conclusions, experiments, publications, clinical or environmental decisions, or reproducible research artifacts.

## Required Capabilities

- Reproducible environment and dependency specification.
- Versioned input data, parameters, and result artifacts.
- Explicit units, assumptions, and numerical tolerances.
- Validation against known examples, fixtures, or reference outputs.
- Provenance records for generated results.

## Recommended Capabilities

- Deterministic execution mode where feasible.
- Independent reference implementation or benchmark comparison for critical algorithms.
- Notebook-to-script promotion path for production analysis.
- Peer review checklist for methodology-sensitive changes.
- Artifact manifests for published outputs.

## Metadata Requirements

- Scientific domain and intended use.
- Dataset provenance, licenses, and transformations.
- Algorithm references and assumptions.
- Numerical precision, tolerances, and units.
- Reproducibility instructions.

## Quality Gates

- Results can be reproduced from documented inputs.
- Unit conversions and tolerances are tested.
- Randomness is seeded or documented.
- Methodological changes identify affected prior outputs.
- Claims do not exceed validated evidence.

## Testing Expectations

- Tests for core formulas, algorithms, and boundary cases.
- Regression tests against reference outputs.
- Sensitivity checks for important parameters.
- Reproduction test for at least one representative workflow.

## Documentation Expectations

- Document scientific assumptions and limitations.
- Document data provenance and licensing.
- Document exact reproduction steps.
- Document how to interpret result artifacts.

## UI/UX Expectations

- Interfaces must display units, confidence, uncertainty, and warning states where relevant.
- Users should be prevented from mixing incompatible units or invalid parameter ranges silently.
- Result exports should include provenance metadata.

## AI Assistant Expectations

If AI assists scientific work, it must distinguish literature-backed statements from speculation, cite sources when used, expose uncertainty, and avoid fabricating references, measurements, or conclusions.

## Implementation Issue Templates

### Add Scientific Workflow

```markdown
## Goal
Describe the scientific workflow and intended use.

## Baseline Packs
- application/scientific

## Required Evidence
- Reproduction steps
- Reference output or benchmark comparison
- Units and tolerance tests
- Data provenance notes

## Acceptance Criteria
- Representative results are reproducible
- Assumptions and limitations are documented
- Invalid parameters are rejected or clearly warned
```

### Change Model Or Algorithm

```markdown
## Change
Describe the methodological change.

## Baseline Packs
- application/scientific

## Required Evidence
- Before/after output comparison
- Affected artifact review
- Peer or methodology review notes

## Acceptance Criteria
- Differences are explained
- Prior results affected by the change are identified
- Tests cover boundary and reference cases
```
