#!/usr/bin/env python3
"""Derive the shared list sections of a pack's .md from its .pack.json.

The .pack.json is the source of truth for the enumerable contract (capabilities,
metadata requirements, gates, expectations, issue templates). This tool rewrites
those bullet-list sections of the markdown twin from the JSON, so the two files
cannot drift. Hand-written prose is preserved: the header blockquote, Purpose /
When To Apply, any lead-in lines before a section's first bullet, and everything
after the first `---` horizontal rule (the versioned playbook addenda).

Usage:
  gen-pack-doc.py docs/application/web.pack.json           # rewrite the .md twin
  gen-pack-doc.py --check docs/application/web.pack.json   # exit 1 if .md is stale
  gen-pack-doc.py --all [--check]                          # every pack with a twin
"""

import argparse
import glob
import json
import os
import re
import sys
import textwrap

SECTION_FIELDS = [
    ("Required Capabilities", "requiredCapabilities"),
    ("Recommended Capabilities", "recommendedCapabilities"),
    ("Metadata Requirements", "metadataRequirements"),
    ("Quality Gates", "qualityGates"),
    ("Testing Expectations", "testingExpectations"),
    ("Documentation Expectations", "documentationExpectations"),
    ("UI/UX Expectations", "uiUxExpectations"),
    ("AI Assistant Expectations", "aiAssistantExpectations"),
]
TEMPLATES_SECTION = "Implementation Issue Templates"
WIDTH = 96


def bullets(items):
    out = []
    for item in items:
        wrapped = textwrap.wrap(f"- {item}", width=WIDTH, subsequent_indent="  ",
                                break_long_words=False, break_on_hyphens=False)
        out.extend(wrapped)
    return "\n".join(out)


def replace_section(body, header, new_list):
    """Replace the bullet list of `## <header>`, keeping lead-in prose lines."""
    rx = re.compile(rf"(^## {re.escape(header)}\n)(.*?)(?=^## |^---$|\Z)",
                    re.M | re.S)
    m = rx.search(body)
    if not m:
        return body, False
    section = m.group(2)
    lines = section.splitlines()
    first_bullet = next((i for i, l in enumerate(lines) if l.startswith("- ")), None)
    lead = "\n".join(lines[:first_bullet]) if first_bullet is not None else section
    return body[:m.start()] + m.group(1) + _assemble(lead, new_list) + body[m.end():], True


def _assemble(lead, new_list):
    chunks = []
    lead = lead.strip("\n")
    if lead.strip():
        chunks.append(lead)
    chunks.append(new_list)
    return "\n" + "\n\n".join(c for c in chunks if c.strip("\n")) + "\n\n"


def replace_templates(body, templates):
    rx = re.compile(rf"(^## {re.escape(TEMPLATES_SECTION)}\n)(.*?)(?=^---$|\Z)", re.M | re.S)
    m = rx.search(body)
    if not m:
        return body, False
    rendered = []
    for tpl in templates:
        rendered.append(f"### {tpl['name']}\n\n```markdown\n{tpl['template']}\n```")
    return body[:m.start()] + m.group(1) + "\n" + "\n\n".join(rendered) + "\n\n" + body[m.end():], True


def derive(pack_path, check):
    md_path = pack_path[: -len(".pack.json")] + ".md"
    if not os.path.isfile(md_path):
        print(f"gen-pack-doc: no markdown twin for {pack_path}", file=sys.stderr)
        return 2
    with open(pack_path) as fh:
        pack = json.load(fh)
    with open(md_path) as fh:
        original = fh.read()

    body = original
    for header, field in SECTION_FIELDS:
        items = pack.get(field) or []
        if not items:
            continue
        body, hit = replace_section(body, header, bullets(items))
        if not hit:
            print(f"gen-pack-doc: WARN section '## {header}' not found in {md_path}")
    templates = pack.get("implementationIssueTemplates") or []
    if templates:
        body, hit = replace_templates(body, templates)
        if not hit:
            print(f"gen-pack-doc: WARN section '## {TEMPLATES_SECTION}' not found in {md_path}")
    body = re.sub(r"\n{3,}", "\n\n", body)

    if body == original:
        print(f"gen-pack-doc: up to date: {md_path}")
        return 0
    if check:
        print(f"gen-pack-doc: STALE: {md_path} does not match {os.path.basename(pack_path)}; "
              f"run scripts/gen-pack-doc.py {os.path.relpath(pack_path)}")
        return 1
    with open(md_path, "w") as fh:
        fh.write(body)
    print(f"gen-pack-doc: rewrote {md_path}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pack", nargs="?", help="path to a .pack.json")
    ap.add_argument("--all", action="store_true", help="process every docs/**/*.pack.json")
    ap.add_argument("--check", action="store_true", help="fail instead of rewriting")
    args = ap.parse_args()

    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if args.all:
        targets = sorted(glob.glob(os.path.join(repo, "docs", "**", "*.pack.json"), recursive=True))
    elif args.pack:
        targets = [os.path.abspath(args.pack)]
    else:
        ap.error("pass a .pack.json path or --all")
    worst = 0
    for t in targets:
        worst = max(worst, derive(t, args.check))
    return worst


if __name__ == "__main__":
    sys.exit(main())
