# MCP Baseline Pack

## Purpose

Define expectations for systems that expose or consume Model Context Protocol servers, tools, resources, prompts, or connected applications.

## When To Apply

Apply this pack when an AI assistant obtains context, invokes tools, or performs actions through MCP.

## Required Capabilities

- Tool, resource, and prompt contracts with stable names and schemas.
- Authentication and authorization boundaries for side-effectful tools.
- Clear separation between read-only and write-capable operations.
- Input validation and output shape guarantees.
- Auditability for sensitive or mutating tool calls.

## Recommended Capabilities

- Least-privilege tool grouping.
- Dry-run support for risky write operations.
- Versioned MCP contracts.
- Capability discovery tests.
- Human review gates for high-impact actions.

## Metadata Requirements

- MCP server name and ownership.
- Tool list, side-effect classification, and required scopes.
- Resource and prompt exposure policy.
- Authentication method and secret handling.
- Audit and retention expectations.

## Quality Gates

- Mutating tools cannot be invoked without proper authorization.
- Tool schemas reject malformed or unsafe input.
- Tool outputs do not leak secrets or unauthorized data.
- Read-only tools remain side-effect free.
- High-impact actions have confirmation, dry-run, or review controls.

## Testing Expectations

- Contract tests for tool schemas and resource discovery.
- Authorization tests for restricted tools.
- Side-effect tests for mutating tools.
- Failure tests for unavailable upstream dependencies.

## Documentation Expectations

- Document each tool's purpose, inputs, outputs, side effects, and permission needs.
- Document client setup and server configuration.
- Document operational limits and unsafe-use examples.

## UI/UX Expectations

- If MCP actions are exposed in a UI, users should see what the assistant intends to do, which
  tool will be used, and what changed afterward.

## AI Assistant Expectations

- Assistants using MCP must prefer read-only inspection before mutation, use the narrowest
  available tool, validate tool results, and report exactly what actions were taken.

## Implementation Issue Templates

### Add MCP Tool Or Server

```markdown
## Goal
Describe the MCP capability and consumers.

## Baseline Packs
- ai/mcp

## Required Evidence
- Tool/resource contract
- Authorization test
- Side-effect classification
- Audit behavior for mutating tools

## Acceptance Criteria
- Contract is discoverable and documented
- Unauthorized access is blocked
- Tool results are validated and safe to expose
```

