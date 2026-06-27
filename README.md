# autospec-baselines

Reusable baseline packs for the Autospec ecosystem.

Autospec is the engine. Autospec Constitution is the law. Autospec Baselines are the playbooks.

This repository is documentation-first. It defines policy and delivery playbooks that compose with `berlinguyinca/autospec-constitution`; it does not implement engine logic, runtime orchestration, generators, or validators.

## What This Repository Contains

- Application baseline packs for common product shapes.
- Technology baseline packs for common implementation stacks.
- Testing baseline packs for quality workflows.
- AI baseline packs for assistant, retrieval, local model, hosted model, and MCP systems.
- JSON Schemas that describe baseline pack and profile composition metadata.

## Relationship To Autospec

- `berlinguyinca/autospec` runs planning, implementation, validation, and release workflows.
- `berlinguyinca/autospec-constitution` defines non-negotiable principles, governance, and quality law.
- `berlinguyinca/autospec-baselines` defines reusable playbooks that describe how specific application, technology, testing, and AI contexts should satisfy the constitution.

## Pack Categories

Application packs:

- [Web Application](docs/application/web.md)
- [AI Platform](docs/application/ai-platform.md)
- [Analytics](docs/application/analytics.md)
- [Scientific](docs/application/scientific.md)
- [Internal Tool](docs/application/internal-tool.md)

Technology packs:

- [React](docs/technology/react.md)
- [Python](docs/technology/python.md)
- [Postgres](docs/technology/postgres.md)

Testing packs:

- [Playwright](docs/testing/playwright.md)

AI packs:

- [RAG](docs/ai/rag.md)
- [Ollama](docs/ai/ollama.md)
- [OpenAI-Compatible APIs](docs/ai/openai-compatible.md)
- [MCP](docs/ai/mcp.md)

## Pack Contract

Every baseline pack defines:

- Purpose
- When to apply
- Required capabilities
- Recommended capabilities
- Metadata requirements
- Quality gates
- Testing expectations
- Documentation expectations
- UI/UX expectations, where applicable
- AI assistant expectations, where applicable
- Implementation issue templates

## Schemas

- [Baseline pack schema](schemas/baseline-pack.schema.json)
- [Profile composition schema](schemas/profile-composition.schema.json)

The schemas are contracts for pack authors and downstream tools. They are not an engine implementation.

## Composition Model

Baseline packs are meant to be layered. A web AI product might compose:

```yaml
name: web-ai-product
constitution:
  repository: berlinguyinca/autospec-constitution
baselines:
  application:
    - application/web
    - application/ai-platform
  technology:
    - technology/react
    - technology/python
    - technology/postgres
  testing:
    - testing/playwright
  ai:
    - ai/rag
    - ai/openai-compatible
    - ai/mcp
```

Profiles may use string references for the current baseline version or object references when a version pin is required:

```yaml
baselines:
  technology:
    - id: technology/react
      version: 1.0.0
```

## Precedence Model

The authoritative conflict rule is profile-level resolution:

1. Autospec Constitution remains the highest authority.
2. Baseline packs add domain-specific expectations beneath the constitution.
3. When composed baseline packs conflict, the stricter quality gate wins.
4. A profile may override a baseline conflict only through an explicit, owned, expiring exception.

Pack-level `extends`, `conflictsWith`, and `constitutionReferences` metadata is advisory discovery metadata for authors and tooling. Profile `exceptions` and `conflictResolution` define the binding composition decision.

## AI Pack Ownership

- `application/ai-platform` owns product-level AI behavior: instruction hierarchy, assistant UX, evaluation posture, model/tool governance, and user trust.
- `ai/rag` owns retrieval behavior: corpus provenance, chunking, indexing, access-filtered retrieval, grounding, answerability, and citation expectations.
- `ai/mcp` owns protocol/tool behavior: MCP contracts, tool schemas, side-effect classification, authorization, auditability, and safe tool invocation.

When these packs overlap, apply the most specific pack for the mechanism and `application/ai-platform` for the user-facing product obligation.

## Non-Goals

- No Autospec engine code.
- No generated workflow runner.
- No CI automation beyond future schema/documentation checks.
- No product-specific implementation policy.
- No dependency lock-in unless a pack explicitly describes a chosen technology.
