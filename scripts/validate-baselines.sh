#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 - "$ROOT" <<'PY'
import json
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover - local operator dependency check
    print(f"ERROR: PyYAML is required for local validation: {exc}", file=sys.stderr)
    sys.exit(1)

root = Path(sys.argv[1])
errors = []

manifest_path = root / "manifests/baselines.yml"
profiles_path = root / "manifests/profiles.yml"
categories_path = root / "manifests/pack-categories.yml"

for path in [manifest_path, profiles_path, categories_path]:
    if not path.exists():
        errors.append(f"missing manifest: {path.relative_to(root)}")

for rel in ["schemas/baseline-pack.schema.json", "schemas/profile-composition.schema.json"]:
    path = root / rel
    if not path.exists():
        errors.append(f"missing schema: {rel}")
        continue
    try:
        json.loads(path.read_text())
    except Exception as exc:
        errors.append(f"invalid JSON schema {rel}: {exc}")

def load_yaml(path, default):
    if not path.exists():
        return default
    try:
        with path.open() as fh:
            return yaml.safe_load(fh) or default
    except Exception as exc:
        errors.append(f"invalid YAML {path.relative_to(root)}: {exc}")
        return default

manifest = load_yaml(manifest_path, {})
profiles = load_yaml(profiles_path, {})
categories = set((load_yaml(categories_path, {}) or {}).get("categories", []))
required_pack_fields = [
    "id",
    "title",
    "version",
    "type",
    "summary",
    "applies_when",
    "capabilities",
    "metadata_required",
    "rules",
    "quality_gates",
    "issue_templates",
]
severity_values = {"required", "recommended", "optional", "forbidden"}
maturity_values = {"prototype", "production", "enterprise", "autonomous"}
pack_ids = {}
rule_ids = {}

for pack in manifest.get("packs", []):
    pid = pack.get("id")
    rel = pack.get("file")
    if not pid or not rel:
        errors.append(f"baseline manifest entry missing id/file: {pack}")
        continue
    path = root / rel
    if not path.exists():
        errors.append(f"manifest pack {pid} points to missing file: {rel}")
        continue
    data = load_yaml(path, {})
    missing = [field for field in required_pack_fields if field not in data]
    if missing:
        errors.append(f"pack {pid} missing fields: {', '.join(missing)}")
    if data.get("id") != pid:
        errors.append(f"pack id mismatch for {rel}: manifest={pid} file={data.get('id')}")
    if pid in pack_ids:
        errors.append(f"duplicate pack id {pid}: {rel} and {pack_ids[pid]}")
    else:
        pack_ids[pid] = rel
    if data.get("type") not in categories:
        errors.append(f"pack {pid} uses unknown type {data.get('type')}")
    for dep in data.get("requires", []) or []:
        if dep not in [p.get("id") for p in manifest.get("packs", [])]:
            errors.append(f"pack {pid} requires unknown pack {dep}")
    for conflict in data.get("conflicts_with", []) or []:
        if conflict not in [p.get("id") for p in manifest.get("packs", [])]:
            errors.append(f"pack {pid} conflicts with unknown pack {conflict}")
    capabilities = data.get("capabilities") or {}
    if not capabilities.get("required"):
        errors.append(f"pack {pid} must define required capabilities")
    for rule in data.get("rules", []):
        rid = rule.get("rule_id") or rule.get("id")
        if not rid:
            errors.append(f"pack {pid} has rule without id")
            continue
        if rid in rule_ids:
            errors.append(f"duplicate rule id {rid}: {pid} and {rule_ids[rid]}")
        else:
            rule_ids[rid] = pid
        for field in ["title", "summary", "source", "category", "severity", "maturity", "check", "evidence_required", "acceptance_criteria", "remediation", "risk"]:
            if not rule.get(field):
                errors.append(f"rule {rid} missing {field}")
        if rule.get("severity") not in severity_values:
            errors.append(f"rule {rid} uses invalid severity {rule.get('severity')}")
        if (rule.get("maturity") or {}).get("level") not in maturity_values:
            errors.append(f"rule {rid} uses invalid maturity level {(rule.get('maturity') or {}).get('level')}")

for profile in profiles.get("profiles", []):
    for pack_id in profile.get("packs", []):
        if pack_id not in pack_ids:
            errors.append(f"profile {profile.get('id')} references unknown pack {pack_id}")

if not pack_ids:
    errors.append("no structured packs found")
if not rule_ids:
    errors.append("no structured baseline rules found")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)

print(f"Baseline validation passed: {len(pack_ids)} packs, {len(rule_ids)} rules")
PY
