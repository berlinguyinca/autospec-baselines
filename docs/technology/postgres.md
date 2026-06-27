# Postgres Baseline Pack

## Purpose

Define expectations for projects using PostgreSQL for transactional storage, analytical storage, queues, search, or operational metadata.

## When To Apply

Apply this pack when PostgreSQL schema, queries, migrations, permissions, backup/restore, or performance characteristics affect the product.

## Required Capabilities

- Versioned schema migrations.
- Primary keys, foreign keys, constraints, and indexes for important access patterns.
- Transaction boundaries for multi-step writes.
- Least-privilege database roles.
- Backup, restore, and migration rollback expectations.

## Recommended Capabilities

- Query plans for high-volume or latency-sensitive queries.
- Seed data or fixtures for development and tests.
- Row-level security where tenant or user boundaries require it.
- Migration rehearsal for large tables.
- Data retention and archival strategy.

## Metadata Requirements

- PostgreSQL version target.
- Database ownership and operational contact.
- Schema ownership and migration tool.
- Data classification and retention expectations.
- Critical query paths and expected scale.

## Quality Gates

- Migrations are reversible or have a documented recovery path.
- Constraints enforce data integrity where application bugs would be costly.
- Sensitive tables have appropriate permissions.
- High-risk queries are reviewed for indexes and execution plan.
- Schema changes account for existing production data.

## Testing Expectations

- Migration tests against realistic schema state.
- Integration tests for repository or query behavior.
- Permission tests for sensitive data paths.
- Regression tests for data integrity bugs.

## Documentation Expectations

- Document schema ownership and migration commands.
- Document operational procedures for backup, restore, and rollback.
- Document data retention and privacy-sensitive tables.

## UI/UX Expectations

Database-backed UI should show truthful states for pending writes, conflicts, stale reads, and partial failures.

## AI Assistant Expectations

If AI proposes SQL or migrations, it must explain data impact, identify locking and rollback considerations, and avoid destructive migration steps without explicit justification.

## Implementation Issue Templates

### Add Or Change Schema

```markdown
## Goal
Describe the data model or query behavior.

## Baseline Packs
- technology/postgres

## Required Evidence
- Migration and rollback/recovery notes
- Constraint/index review
- Integration or migration test
- Data impact assessment

## Acceptance Criteria
- Existing data is handled safely
- Integrity rules are enforced by the database where appropriate
- Sensitive access respects role boundaries
```
