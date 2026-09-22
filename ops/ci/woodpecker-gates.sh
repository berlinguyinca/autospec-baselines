#!/bin/bash
# The gate for autospec-baselines: build a throwaway virtualenv, fetch the
# constitution repo, validate every pack against its schema and against the
# real doctrine, and prove the generated pack docs still match their pack JSON.
#
# This is a like-for-like port of the TeamCity build `Autospec_Baselines_Validate`.
# It is the whole of that build; nothing from it was dropped.
#
# RUN IT LOCALLY: `bash ops/ci/woodpecker-gates.sh` from a clean checkout. It
# writes only .ci-venv/ and .constitution/, both of which are gitignored.
set -euo pipefail

CONSTITUTION_REPO="${CONSTITUTION_REPO:-berlinguyinca/autospec-constitution}"
CONSTITUTION_REF="${CONSTITUTION_REF:-refs/heads/main}"

journal=""
for candidate in "${WOODPECKER_JOURNAL_DIR:-}" /home/wohlgemuth/woodpecker/logs; do
  [ -n "$candidate" ] || continue
  if mkdir -p "$candidate" 2>/dev/null && [ -w "$candidate" ]; then
    journal="$candidate/baselines-gates-${CI_COMMIT_SHA:-local}-$(date +%s).log"
    break
  fi
done

# The run goes through a PIPELINE, not `exec > >(tee ...)`.
#
# Process substitution does not make the shell wait for the reader: a script
# that fails in seconds exits before tee drains its pipe, and the agent records
# nothing at all. This gate takes seconds even when it passes, so it lives
# entirely inside that failure window. A pipeline is waited on, so the output
# survives, and PIPESTATUS carries the body's status past tee.
main() {
  echo "commit:  ${CI_COMMIT_SHA:-<local>}"
  step() { echo; echo "=== $* ==="; }

  step "python"
  if ! command -v python3 >/dev/null 2>&1; then
    echo "FATAL: python3 is not on this agent's PATH." >&2
    exit 1
  fi
  python3 --version
  # An exact pin, not a floor, and deliberately so: the point of this check is
  # that a silent interpreter change would quietly alter what the validator
  # exercises, and `>=` cannot catch that. TeamCity pinned 3.12 because its
  # agent image was Ubuntu 24.04; the Woodpecker CI image is Debian trixie and
  # ships 3.13 only, with no 3.12 available, so the pin is re-pointed rather
  # than relaxed. Both validators were verified green under 3.13.5 in that
  # image before this was changed. If a future image bump turns this red, that
  # is the check doing its job -- re-verify the validator, then move the pin.
  python3 -c 'import sys; assert sys.version_info[:2] == (3, 13), sys.version'

  step "virtualenv"
  # Rebuilt from scratch every run: a venv carried over from a previous build
  # on the same node would let a dependency that is no longer installable keep
  # the gate green.
  rm -rf .ci-venv
  python3 -m venv .ci-venv
  .ci-venv/bin/pip install --quiet jsonschema pyyaml

  step "fetch the constitution into .constitution"
  # NO CREDENTIAL IS USED OR NEEDED HERE. Both repositories are public, so the
  # codeload tarball is served over unauthenticated HTTPS. Keep it that way:
  # an authenticated fetch would make this gate silently depend on a token
  # whose absence nothing here would explain.
  rm -rf .constitution constitution.tar.gz
  mkdir -p .constitution
  # Download and extract as two steps, never `curl | tar`. A pipeline reports
  # tar's status, and tar can exit 0 on truncated input, so a network blip
  # would leave a partial .constitution and the validator would pass over an
  # incomplete doctrine. --fail is what makes set -e catch an HTTP error status.
  curl -sSL --fail --retry 3 -o constitution.tar.gz \
    "https://codeload.github.com/${CONSTITUTION_REPO}/tar.gz/${CONSTITUTION_REF}"
  tar xzf constitution.tar.gz --strip-components=1 -C .constitution
  rm -f constitution.tar.gz
  if [ ! -d .constitution/docs ] || [ ! -d .constitution/schemas ]; then
    echo "FATAL: the constitution fetch produced no docs/ or schemas/." >&2
    echo "       Without both, validate-packs.py would skip the cross-repo" >&2
    echo "       reference check and still exit 0." >&2
    exit 1
  fi
  ls .constitution

  step "validate packs, tokens, references, and links"
  .ci-venv/bin/python scripts/validate-packs.py --constitution-dir .constitution

  step "pack docs derived from pack JSON (no duo drift)"
  .ci-venv/bin/python scripts/gen-pack-doc.py --all --check

  echo
  echo "GATES PASSED"
}

if [ -n "$journal" ]; then
  echo "journal: $journal"
  main 2>&1 | tee -a "$journal"
  exit "${PIPESTATUS[0]}"
fi
main
