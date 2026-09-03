# ArcKit AI Agent Architecture: Governed Design for Autonomous Systems

**`arckit-agent-architecture` gives autonomous agent programmes the same
governance discipline ArcKit already brings to requirements, risks, decisions,
assurance, and delivery. It ships six commands and the `agent-architecture`
build recipe for agent inventory, design, governance, integration, security,
and maturity.**

---

## Agents are architecture now

The first wave of AI agent work often starts as experimentation: a prompt, a
tool loop, a memory store, a queue, a model choice, and a few permissions that
make a workflow useful.

That is fine for discovery. It is not enough for production.

An agent that can inspect repositories, call tools, move data, draft
recommendations, trigger workflows, or coordinate with other agents is an
architecture component. It has ownership, interfaces, dependencies, failure
modes, security posture, audit requirements, and human oversight needs. If it
uses memory, acts through tools, or shares state with other agents, those are
design decisions, not incidental implementation details.

`arckit-agent-architecture` exists for that moment: when an agent programme
needs to become explicit enough to govern.

## What the overlay adds

The plugin adds six slash commands:

- `/arckit:agent-inventory` creates an agent register, capability matrix,
  dependency map, lifecycle view, risk posture, and oversight classification.
- `/arckit:agent-design` defines the agent architecture: purpose, autonomy
  boundary, memory model, tool access, failure handling, and design decisions.
- `/arckit:agent-governance` sets out the oversight model, approval workflow,
  audit trail, operating controls, and human intervention points.
- `/arckit:agent-integration` defines agent-to-agent contracts,
  orchestration, shared state, message protocols, and failure isolation.
- `/arckit:agent-security` covers sandboxing, permissions, data access,
  threat paths, isolation, and hardening controls.
- `/arckit:agent-maturity` assesses the maturity of the agent programme and
  produces an improvement roadmap.

The new ArcKit document codes are `AAGI`, `AAGR`, `AAOV`, `AAIN`, `AASE`, and
`AAMT`. That means agent architecture output lives in the same project
structure as every other governed artefact:

```text
projects/003-agent-programme/
  ARC-003-AAGI-v1.0.md   # Agent inventory
  ARC-003-AAGR-v1.0.md   # Agent architecture specification
  ARC-003-AAOV-v1.0.md   # Agent governance framework
  ARC-003-AAIN-v1.0.md   # Agent integration patterns
  ARC-003-AASE-v1.0.md   # Agent security architecture
  ARC-003-AAMT-v1.0.md   # Agent maturity assessment
```

## Inventory before design

The foundational command is `/arckit:agent-inventory`.

That is deliberate. Agent programmes become risky when nobody can answer basic
questions:

- Which agents exist?
- Who owns each one?
- What tools can they call?
- What data can they see?
- Which model or model family do they use?
- Are they production, staging, development, planned, deprecated, or retired?
- Which ones require human-in-the-loop or human-on-the-loop oversight?
- Which agents depend on each other?

The inventory command turns those questions into a governed artefact. It can
read existing ArcKit context such as principles, ADM preliminary work,
application inventory, previous agent designs, governance outputs, and
security evaluations. The result is not a static asset list. It is the
starting point for design, security, integration, governance, and maturity
work.

## Design, integration, governance, and security

Once the inventory exists, the other commands make the agent programme
reviewable.

`/arckit:agent-design` turns agent intent into architecture. It records what
the agent is for, what autonomy it has, what it can and cannot do, how it uses
memory, what tools it can invoke, what failures look like, and which design
decisions need to be traceable.

`/arckit:agent-integration` handles the point most teams under-specify:
agent-to-agent and agent-to-system contracts. It asks for protocols, inputs,
outputs, shared state, orchestration, retries, message delivery, observability,
and failure isolation. If agents coordinate, the coordination itself needs an
architecture.

`/arckit:agent-governance` makes the human control model explicit. That means
approval paths, audit trails, escalation, review cadence, exception handling,
and the boundary between assisted, supervised, and autonomous operation.

`/arckit:agent-security` treats agents as privileged software components. Tool
permissions, sandboxing, secrets exposure, data classification, prompt
injection paths, model/tool boundary controls, and logging all belong in the
architecture pack.

Together those documents make the agent system something an architecture board
can read, challenge, and improve.

## The `agent-architecture` recipe

The overlay also ships the `agent-architecture` build recipe.

The recipe starts with core ArcKit foundations: principles, requirements,
stakeholders, risk, and AI Playbook context. It then builds the agent
inventory, design, integration, governance, and security artefacts, with
maturity as an optional target.

The shape is:

```text
principles
  -> requirements + stakeholders
  -> risk + AI Playbook
  -> agent inventory
  -> agent design
  -> agent integration + governance + security
  -> optional agent maturity
  -> health + pages
```

That matters because an agent programme should not sit outside the normal
governance baseline. Requirements, stakeholders, risk, AI governance, agent
design, and security need to agree with each other.

## Getting started

The plugin depends on the core `arckit` Claude Code plugin:

```bash
claude plugin install arckit arckit-agent-architecture
```

Then run the commands directly:

```text
/arckit:agent-inventory "Casework triage agents"
/arckit:agent-design 003
/arckit:agent-integration 003
/arckit:agent-governance 003
/arckit:agent-security 003
/arckit:agent-maturity 003
```

Or use the build harness:

```text
/arckit:build 003 --recipe agent-architecture --plan
/arckit:build 003 --recipe agent-architecture
```

Use `--plan` first so you can review the target order before generating the
pack.

## Scope

This first release is focused on autonomous AI agent programmes: single
agents, multi-agent chains, swarms, hierarchical systems, orchestration, human
oversight, and security posture.

It is not a general LLM benchmark overlay. It is not a cloud infrastructure
deployment guide. It is not a substitute for regulatory overlays such as
`arckit-us`, `arckit-eu`, `arckit-uk-nhs`, or `arckit-uk-finance`.

It is the architecture layer for agents themselves.

## Why this belongs in ArcKit

ArcKit's central claim has not changed: the toolkit drafts, the architect
judges.

Agent architecture needs that bias. AI agents are too consequential to remain
as informal prompt chains, but too context-specific to be governed by a single
generic checklist. The useful middle path is a set of structured artefacts:
inventory, design, governance, integration, security, and maturity.

That gives the architect something concrete to inspect. It gives the team a
shared model of what the agents are allowed to do. It gives security and
assurance reviewers the evidence they need to challenge the design. And it
keeps agent delivery inside the same governed project structure as the rest of
the architecture.

That is what `arckit-agent-architecture` adds: not agent hype, but agent
governance as architecture work.

---

*`arckit-agent-architecture` is an MIT-licensed community overlay for Claude
Code. It requires the core `arckit` plugin.*

<!-- arckit:community-block -->
## Join the ArcKit Community

- **Discord** - real-time conversation, help with commands, and what people are building: [discord.gg/HsA4Y3hQ4](https://discord.gg/HsA4Y3hQ4)
- **LinkedIn Group** - announcements, case studies, and longer-form discussion: [linkedin.com/groups/17641034](https://www.linkedin.com/groups/17641034/)
- **GitHub** - code, issues, and contributions: [github.com/tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit)
