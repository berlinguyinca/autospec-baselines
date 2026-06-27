# Vision

Autospec Baselines exists to make high-quality delivery repeatable without making every project rediscover its operating model.

Autospec is the engine: it plans, executes, verifies, and records work.

Autospec Constitution is the law: it defines the principles, constraints, and non-negotiable quality expectations that every Autospec workflow must respect.

Autospec Baselines are the playbooks: they translate those laws into reusable expectations for common application types, technology stacks, testing approaches, and AI systems.

## Goals

- Provide composable, readable baseline packs for common project contexts.
- Give implementers clear expectations before work starts.
- Give reviewers concrete quality gates after work lands.
- Keep policy separate from engine logic.
- Let teams combine packs into profiles without copying entire process documents.

## Design Principles

- Documentation first: humans should understand the pack without a tool.
- Schema backed: tools should be able to validate pack structure.
- Composable: packs should layer cleanly across application, technology, testing, and AI domains.
- Strict where risk is high: data integrity, security, privacy, user trust, and scientific correctness get explicit gates.
- Minimal where possible: packs describe expectations, not implementation recipes.

## Success Criteria

- A new project can select baseline packs and immediately know the expected quality bar.
- Autospec workflows can reference packs as planning and review context.
- Reviewers can identify missing evidence without debating unstated assumptions.
- The repository remains policy/playbook-only.

## Boundaries

This repository does not run Autospec. It does not generate code, migrate databases, call models, execute tests, or enforce policy at runtime. Those responsibilities belong to the engine and downstream repositories.
