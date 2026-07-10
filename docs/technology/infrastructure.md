# Infrastructure / IaC Baseline Pack

> Composes the Operations (12), Security & Privacy (11), and Architecture (03) doctrines and the shared quality method ([`../method/AUTOSPEC-QUALITY-METHOD.md`](../method/AUTOSPEC-QUALITY-METHOD.md)).

## Purpose

Expectations for provisioning infrastructure as code, so applies are reproducible,
least-privilege, policy-compliant, and blast-radius-controlled.

## When To Apply

When a change provisions or modifies infrastructure via code (Terraform, Pulumi,
CloudFormation, Kubernetes) or affects IAM, networking, or stateful resources.

## Required Capabilities

- Reproducible, idempotent apply: plan is reviewed and applied without manual drift.
- Drift detection between declared and actual state, with alerting.
- Least-privilege IAM: no wildcard admin; scoped roles and policies.
- Policy-as-code checks (e.g. OPA/Conftest) enforce guardrails before apply.
- No hardcoded secrets in IaC; secrets sourced from a manager.
- Remote, locked, versioned state.

## Recommended Capabilities

- Environment parity via modules.
- Cost tagging for attribution.
- Automated plan on PR with human approval to apply.
- Blast-radius limits (per-environment isolation, staged rollout).

## Metadata Requirements

- Resource inventory with owners and environments.
- IAM policy inventory.
- State backend and locking configuration.
- Cost/ownership tags.

## Quality Gates

- Apply is reproducible and idempotent; a re-plan shows no unexpected drift.
- Policy-as-code checks pass; no wildcard-admin IAM.
- No secrets are hardcoded (scanner passes).
- State is remote, locked, and versioned.
- Resources are tagged for ownership and cost; a destroy/rollback path is known.

## Testing Expectations

- Plan review and policy checks in CI.
- Drift detection on a schedule.
- Secret scanning on IaC.
- Environment smoke checks after apply.

## Documentation Expectations

- Document the resource inventory, IAM model, and state backend.
- Document apply/rollback runbooks.
- Document environment topology and blast-radius boundaries.

## Implementation Issue Templates

### Provision or Change Infrastructure

```markdown
## Goal
Describe the resource change and environments affected.

## Baseline Packs
- technology/infrastructure

## Required Evidence
- Reviewed plan; policy-as-code pass
- Least-privilege IAM diff
- Secret scan clean
- Rollback/destroy path

## Acceptance Criteria
- Reproducible apply, no unexpected drift
- Policies pass; no wildcard admin
- State remote/locked; tagged
```

---

## Gates Registry

Machine-readable in
[`infrastructure-assets/rules/infrastructure.rules.yaml`](infrastructure-assets/rules/infrastructure.rules.yaml):
reproducible/idempotent apply, drift detection, least-privilege IAM, policy-as-code, no
hardcoded secrets, managed state, tagging and a known rollback. Judge rubric:
reproducibility, least privilege, policy compliance, blast-radius control.
