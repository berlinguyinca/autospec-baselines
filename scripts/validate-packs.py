#!/usr/bin/env python3
"""Validate baseline pack metadata and composition contracts.

Checks, for every docs/**/*.pack.json:
  1. JSON Schema validity against schemas/baseline-pack.schema.json (draft 2020-12).
  2. The pack id matches its file location (docs/<id>.pack.json).
  3. Every `extends` id resolves to a real pack doc (docs/<id>.md) in this repo.
  4. Every `constitutionReferences` id resolves to docs/<id>.md in the
     constitution repo (pass --constitution-dir; omitted -> skipped with a note).

Also validates every docs/**/web-assets/**/tokens.json against the vendored
DTCG schema (schemas/dtcg-format-2025.10.json), every docs/**/*.rules.yaml gate
registry (parses; every rule has an id and a check in auto|judge|vlm|review),
and that relative links inside pack docs resolve.

Exit 0 = all good; 1 = findings; 2 = environment/usage error.
"""

import argparse
import glob
import json
import os
import re
import sys

try:
    import jsonschema
except ImportError:
    print("validate-packs: the python 'jsonschema' package is required", file=sys.stderr)
    sys.exit(2)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
findings = []


def find(msg):
    findings.append(msg)
    print(f"FINDING: {msg}")


def load(path):
    with open(path) as fh:
        return json.load(fh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--constitution-dir", default="",
                    help="checkout of berlinguyinca/autospec-constitution for cross-repo checks")
    args = ap.parse_args()

    pack_schema = load(os.path.join(REPO, "schemas", "baseline-pack.schema.json"))
    pack_validator = jsonschema.Draft202012Validator(pack_schema)

    dtcg_path = os.path.join(REPO, "schemas", "dtcg-format-2025.10.json")
    dtcg_validator = None
    if os.path.isfile(dtcg_path):
        dtcg_validator = jsonschema.Draft7Validator(load(dtcg_path))

    packs = sorted(glob.glob(os.path.join(REPO, "docs", "**", "*.pack.json"), recursive=True))
    if not packs:
        print("validate-packs: no *.pack.json files found (nothing to validate)")
    for pack_path in packs:
        rel = os.path.relpath(pack_path, REPO)
        try:
            pack = load(pack_path)
        except json.JSONDecodeError as exc:
            find(f"{rel}: invalid JSON: {exc}")
            continue
        for err in sorted(pack_validator.iter_errors(pack), key=str):
            find(f"{rel}: schema violation at {'/'.join(map(str, err.path)) or '<root>'}: {err.message}")
        pack_id = pack.get("id", "")
        expected = os.path.join("docs", f"{pack_id}.pack.json")
        if rel != expected:
            find(f"{rel}: pack id '{pack_id}' does not match file location (expected {expected})")
        md_twin = os.path.join(REPO, "docs", f"{pack_id}.md")
        if pack_id and not os.path.isfile(md_twin):
            find(f"{rel}: missing markdown twin docs/{pack_id}.md")
        for ext in pack.get("extends", []):
            if not os.path.isfile(os.path.join(REPO, "docs", f"{ext}.md")):
                find(f"{rel}: extends '{ext}' does not resolve to docs/{ext}.md")
        refs = pack.get("constitutionReferences", [])
        if args.constitution_dir:
            for ref in refs:
                if not os.path.isfile(os.path.join(args.constitution_dir, "docs", f"{ref}.md")):
                    find(f"{rel}: constitutionReferences '{ref}' does not resolve in {args.constitution_dir}/docs")
        elif refs:
            print(f"note: {rel}: skipping {len(refs)} constitutionReferences checks "
                  "(pass --constitution-dir to enable)")
        print(f"ok: {rel}")

    tokens = sorted(glob.glob(os.path.join(REPO, "docs", "**", "web-assets", "**", "tokens.json"),
                              recursive=True))
    for tok_path in tokens:
        rel = os.path.relpath(tok_path, REPO)
        if dtcg_validator is None:
            find(f"{rel}: schemas/dtcg-format-2025.10.json is missing; cannot validate DTCG tokens")
            continue
        try:
            doc = load(tok_path)
        except json.JSONDecodeError as exc:
            find(f"{rel}: invalid JSON: {exc}")
            continue
        errs = sorted(dtcg_validator.iter_errors(doc), key=str)
        for err in errs[:10]:
            find(f"{rel}: DTCG violation at {'/'.join(map(str, err.path)) or '<root>'}: {err.message}")
        if not errs:
            print(f"ok: {rel}")

    registries = sorted(glob.glob(os.path.join(REPO, "docs", "**", "*.rules.yaml"),
                                  recursive=True))
    if registries:
        try:
            import yaml
        except ImportError:
            find("*.rules.yaml present but the python 'pyyaml' package is not installed")
            yaml = None
        if yaml is not None:
            for reg_path in registries:
                rel = os.path.relpath(reg_path, REPO)
                try:
                    with open(reg_path) as fh:
                        reg = yaml.safe_load(fh)
                except yaml.YAMLError as exc:
                    find(f"{rel}: invalid YAML: {exc}")
                    continue
                rules = (reg or {}).get("rules")
                if not isinstance(rules, list) or not rules:
                    find(f"{rel}: no rules[] list")
                    continue
                before = len(findings)
                refs = (reg or {}).get("doctrine_refs") or []
                if refs and not args.constitution_dir:
                    print(f"note: {rel}: skipping {len(refs)} doctrine_refs checks "
                          "(pass --constitution-dir to enable)")
                for ref in refs:
                    if args.constitution_dir and not os.path.isfile(
                            os.path.join(args.constitution_dir, "docs", f"{ref}.md")):
                        find(f"{rel}: doctrine_refs '{ref}' does not resolve in {args.constitution_dir}/docs")
                for r in rules:
                    if not isinstance(r, dict) or not r.get("id") or r.get("check") not in ("auto", "judge", "vlm", "review"):
                        find(f"{rel}: rule {r.get('id') if isinstance(r, dict) else r!r} needs an id and check in auto|judge|vlm|review")
                if len(findings) == before:
                    print(f"ok: {rel}")

    link_rx = re.compile(r"\]\(([^)#:]+)\)")
    for md_path in sorted(glob.glob(os.path.join(REPO, "docs", "**", "*.md"), recursive=True)):
        rel = os.path.relpath(md_path, REPO)
        base = os.path.dirname(md_path)
        with open(md_path) as fh:
            body = fh.read()
        for target in link_rx.findall(body):
            if target.startswith(("http", "mailto", "/")):
                continue
            if not os.path.exists(os.path.join(base, target)):
                find(f"{rel}: relative link '{target}' does not resolve")

    if findings:
        print(f"validate-packs: FAIL ({len(findings)} findings)")
        return 1
    print("validate-packs: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
