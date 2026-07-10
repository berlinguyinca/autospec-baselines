# Data Science & ML Baseline Pack

> Composes the AI Platform (07), Testing (05), Analytics (10), and Security & Privacy (11) doctrines and the shared quality method ([`../method/AUTOSPEC-QUALITY-METHOD.md`](../method/AUTOSPEC-QUALITY-METHOD.md)); extends `application/scientific`, `technology/python`, and `ai/openai-compatible`.

## Purpose

Expectations for systems built around trained models and experiments, so results are
reproducible, honestly evaluated, fair, and governed.

## When To Apply

When the system trains, evaluates, or serves ML models, or produces results from experiments,
and decisions depend on those outputs.

## Required Capabilities

- A versioned registry of features, labels, and datasets with provenance; definitions traced,
  not ad-hoc.
- Train/validation/test separation with automated leakage detection.
- Held-out evaluation by a fixed harness the model did not train against; the model does not
  grade itself.
- Reproducibility: pinned data versions, fixed seeds, recorded environment; results
  re-derivable.
- Fairness/bias metrics across relevant subgroups; calibration reported for probabilistic
  outputs.
- A model card recording data, metrics, intended use, and limitations; honest about uncertainty.

## Recommended Capabilities

- Drift and performance monitoring in production with alerting.
- Baseline/challenger comparison with a non-regression gate before promotion.
- Experiment tracking with parameters and artifacts.
- Notebook-to-pipeline promotion path.

## Metadata Requirements

- Feature/label/dataset registry with versions and provenance.
- Evaluation harness, metrics, and thresholds.
- Subgroup definitions for fairness analysis.
- Model registry with cards and lineage.

## Quality Gates

- No train/test leakage; splits documented and enforced.
- Evaluation uses a held-out set the model did not see; reported metrics reproduce from pinned
  inputs.
- Fairness metrics computed across defined subgroups; unexplained disparities block promotion.
- Probabilistic outputs are calibrated or the miscalibration is disclosed.
- A new model does not regress any gated metric (slice accuracy, fairness, latency) versus the
  incumbent.
- A model card exists and states intended use, data, metrics, and limitations.

## Testing Expectations

- Deterministic reproduction test from versioned inputs and seed.
- Leakage checks and split-integrity tests.
- Subgroup and calibration evaluation in the harness.
- Non-regression comparison against the incumbent before promotion.

## Documentation Expectations

- Publish a model card per released model.
- Document data provenance, assumptions, and known failure modes.
- Document the evaluation harness and thresholds.

## AI Assistant Expectations

- Assistants and generated analysis cite data and are honest about uncertainty.
- No model self-certifies: promotion requires the independent harness and the non-regression
  gate.

## Implementation Issue Templates

### Train/Evaluate Model

```markdown
## Goal
Describe the prediction task and the decision it supports.

## Baseline Packs
- application/data-science

## Required Evidence
- Leakage check + documented splits
- Held-out metrics reproduced from pinned inputs
- Subgroup fairness + calibration report
- Non-regression vs incumbent
- Model card

## Acceptance Criteria
- No leakage; reproducible metrics
- No unexplained subgroup disparity
- No regression on gated metrics
- Model card complete
```

---

## Vocabulary

Features, labels, and datasets are versioned, provenance-bearing definitions (seed:
[`data-science-assets/tokens/ml-registry.json`](data-science-assets/tokens/ml-registry.json))
— referenced, never redefined per notebook.

## Gates Registry

Machine-readable in
[`data-science-assets/rules/data-science.rules.yaml`](data-science-assets/rules/data-science.rules.yaml):
no leakage, held-out evaluation by an independent harness, reproducible metrics, subgroup
fairness, calibration, model non-regression versus the incumbent, and a model card. The model
never grades itself; promotion is a non-regression ratchet. The independent judge scores
leakage, honest evaluation, fairness, calibration, reproducibility, and intended-use clarity.

## Evidence

The model card plus the evaluation report is the evidence bundle.
