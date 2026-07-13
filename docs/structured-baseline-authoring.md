# Structured Baseline Authoring

Autospec Baselines are playbooks. The Constitution defines law; baseline packs describe how a specific product, technology, AI, or governance context should satisfy that law.

Structured baseline packs make those playbooks consumable by Autospec without relying on prose inference.

## Pack Structure

Each pack lives under `packs/` and includes:

- `id`
- `title`
- `version`
- `type`
- `summary`
- `applies_when`
- `inherits`
- `requires`
- `conflicts_with`
- `capabilities`
- `metadata_required`
- `rules`
- `quality_gates`
- `issue_templates`

The Markdown files under `docs/` remain the human explanation. The YAML files are the machine-readable contract.

## Constitution vs Baselines

- Constitution rules are universal expectations and governance.
- Baseline packs are contextual playbooks for application types, technologies, AI mechanisms, and governance regimes.
- When they overlap, the Constitution remains authoritative and the stricter quality gate should win unless an owned, expiring waiver exists.

## Inheritance, Dependencies, And Conflicts

- `inherits` means a pack extends another pack's posture.
- `requires` means another pack must be present for the pack to be complete.
- `conflicts_with` documents incompatible assumptions.

Keep these references stable and use pack IDs from `manifests/baselines.yml`.

## Capabilities

Capabilities describe what the repository or product should be able to do. Use human-readable entries for required and recommended capabilities, then add structured rules for the capabilities that Autospec can evaluate.

## Rules

Rules follow the same shape as Constitution structured rules, including:

- `id` and `rule_id`
- `source`
- `category`
- `severity`
- `maturity`
- `applies_when`
- `check`
- `evidence_required`
- `acceptance_criteria`
- `metadata_required`
- `quality_gates`
- `remediation`
- `risk`

Use baseline-prefixed IDs such as:

- `baseline.web.in_app_docs.required`
- `baseline.rag.citations.required`
- `baseline.enterprise.audit_logs.required`

## Quality Gates

Quality gates are human-review expectations that should be visible in issue drafts, verifier reports, and PR evidence.

## Issue Templates

Issue templates are starter backlog shapes. They are not GitHub issue creation logic. Autospec may use them later to draft local backlog items.

## Validation

Run:

```bash
bash scripts/validate-baselines.sh
```

The validator checks manifests, pack files, required fields, unique pack IDs, dependency/conflict references, unique rule IDs, known pack categories, severity values, maturity values, and JSON schema validity.

## Examples

See:

- `examples/profile-composition-web-ai-analytics.yml`
- `examples/profile-composition-scientific-ai.yml`
