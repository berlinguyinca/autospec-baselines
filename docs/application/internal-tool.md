# Internal Tool Baseline Pack

## Purpose

Define expectations for administrative, operational, support, moderation, back-office, and other tools used by trusted internal users.

## When To Apply

Apply this pack when the interface is not public-facing but can affect customer data, money movement, operational state, compliance, moderation, or production systems.

## Required Capabilities

- Role-based access control for privileged actions.
- Audit logs for sensitive reads and writes.
- Confirmation and recovery paths for destructive operations.
- Clear environment and target-resource indicators.
- Input validation and server-side authorization.

## Recommended Capabilities

- Permission simulation or read-only preview modes.
- Bulk action dry runs.
- Operational runbooks linked from risky workflows.
- Break-glass process with review.
- Change history for important records.

## Metadata Requirements

- Internal user roles and privilege levels.
- Sensitive actions and affected resources.
- Audit retention expectations.
- Escalation owner for failed or risky operations.
- Production versus non-production environment rules.

## Quality Gates

- Unauthorized users cannot access privileged workflows.
- Sensitive actions are audited with actor, target, timestamp, and result.
- Bulk and destructive actions show scope before execution.
- Production-impacting actions cannot be triggered accidentally.
- Error messages help operators recover without leaking secrets.

## Testing Expectations

- Authorization tests for each privileged action.
- Audit-log tests for sensitive actions.
- End-to-end tests for common operational workflows.
- Failure-mode tests for partial success, retries, and validation errors.

## Documentation Expectations

- Document operational purpose, user roles, and risky actions.
- Document rollback or remediation steps.
- Document audit fields and retention policy.
- Keep runbooks close to the workflows they support.

## UI/UX Expectations

- Optimize for accurate repeated work, not marketing presentation.
- Show dense but scannable information for operators.
- Make environment, scope, and consequences unmistakable.
- Provide filters, sorting, and search for large operational datasets.

## AI Assistant Expectations

- If AI is used inside an internal tool, it must not execute privileged actions without explicit
  review, must summarize proposed changes before submission, and must preserve auditability of
  user versus assistant actions.

## Implementation Issue Templates

### Add Internal Workflow

```markdown
## Goal
Describe the operational workflow and user role.

## Baseline Packs
- application/internal-tool

## Required Evidence
- Authorization test
- Audit-log test
- Failure-state test
- Runbook or operational documentation update

## Acceptance Criteria
- Only authorized users can perform the action
- Sensitive actions are auditable
- Operators can see target scope before execution
```

### Add Bulk Or Destructive Action

```markdown
## Action
Describe the bulk or destructive operation.

## Baseline Packs
- application/internal-tool

## Required Evidence
- Dry-run or preview evidence
- Confirmation behavior
- Rollback/remediation notes
- Partial-failure handling test

## Acceptance Criteria
- Scope is visible before execution
- Partial failures are recoverable
- Audit trail records each affected target
```

