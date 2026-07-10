# API Contract Baseline Pack

> Composes the Architecture (03), Testing (05), and Documentation (09) doctrines and the shared quality method ([`../method/AUTOSPEC-QUALITY-METHOD.md`](../method/AUTOSPEC-QUALITY-METHOD.md)); extends `technology/python`.

## Purpose

Expectations for designing and evolving APIs as products, so contracts are stable, versioned,
and safe for consumers.

## When To Apply

When a change defines or modifies an API consumed by other services or external clients, and
backward compatibility affects consumers you do not control.

## Required Capabilities

- A machine-readable spec (OpenAPI / protobuf / GraphQL SDL) is the source of truth for the
  contract.
- Backward compatibility: no breaking change ships without a major-version bump.
- Automated breaking-change detection on the spec diff.
- Consumer-driven contract tests gate changes.
- A documented, consistent error contract.
- A deprecation policy: announced changes, timelines, and sunsets.

## Recommended Capabilities

- Spec-first workflow with generated clients/servers.
- Compatibility gates in CI against published consumers.
- Versioned, published changelog for the API.
- Pagination, idempotency keys, and rate-limit semantics defined.

## Metadata Requirements

- API registry with surfaces, versions, and deprecation status.
- Published spec artifacts.
- Known consumers and their contracts.

## Quality Gates

- The spec is the source of truth and validates.
- A spec diff runs breaking-change detection; breaking changes require a major version.
- Consumer-driven contract tests pass.
- Version reflects the change type (semver); deprecations follow the policy.
- Error shapes are documented and consistent.

## Testing Expectations

- Spec validation in CI.
- Breaking-change detection on every spec change.
- Consumer-driven contract tests.
- Backward-compatibility tests against the prior version.

## Documentation Expectations

- Publish the spec and a versioned changelog.
- Document the error contract and deprecation timelines.
- Provide client usage examples that are tested.

## Implementation Issue Templates

### Define or Evolve an API

```markdown
## Goal
Describe the endpoint/message and its consumers.

## Baseline Packs
- technology/api

## Required Evidence
- Updated spec (source of truth)
- Breaking-change detection result
- Consumer-driven contract tests
- Semver/deprecation applied

## Acceptance Criteria
- No breaking change without a major bump
- Consumers unbroken
- Error contract consistent
- Changelog updated
```

---

## Vocabulary

The API registry is the canonical surface (seed:
[`api-assets/tokens/api-registry.json`](api-assets/tokens/api-registry.json)): versions and
deprecation status live in one place. The spec (OpenAPI/proto/SDL) is the contract's source
of truth.

## Gates Registry

Machine-readable in
[`api-assets/rules/api-contract.rules.yaml`](api-assets/rules/api-contract.rules.yaml):
spec-as-source-of-truth, breaking-change detection, backward compatibility, consumer-driven
contract tests, semver, deprecation policy, consistent error contract. Judge rubric:
compatibility, spec fidelity, versioning correctness, consumer safety.
