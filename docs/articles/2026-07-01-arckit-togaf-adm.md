# ArcKit TOGAF ADM: The Method Becomes a Governed Workflow

**`arckit-togaf-adm` turns the TOGAF Architecture Development Method into
versioned ArcKit artefacts. It ships nine commands and the `togaf-adm-full`
build recipe for ADM preliminary work, capability mapping, application
inventory, rationalization, gap analysis, transition architecture,
implementation governance, change management, and architecture repository
synthesis.**

---

## Why TOGAF belongs in the harness

Many enterprise architecture teams already use TOGAF language. They talk about
preliminary work, architecture vision, business architecture, application
architecture, opportunities and solutions, migration planning, implementation
governance, architecture change, and the architecture repository.

The problem is not the vocabulary. The problem is how easily the work turns
into disconnected documents.

A capability map sits in one deck. An application inventory lives in a
spreadsheet. A gap analysis becomes a workshop note. Transition architecture
gets copied into a roadmap. Architecture board decisions are recorded
somewhere else. Lessons learned may never reach the repository.

`arckit-togaf-adm` brings those ADM-shaped outputs into the ArcKit project
model: versioned files, document control, provenance, traceability, templates,
health checks, and repeatable naming.

## What the overlay adds

The plugin adds nine slash commands:

- `/arckit:adm-preliminary` for preliminary phase, scope, drivers,
  constraints, and architecture vision.
- `/arckit:business-capability-map` for strategy, capabilities, value chains,
  and business architecture.
- `/arckit:application-inventory` for application portfolio assessment,
  lifecycle, ownership, and integration patterns.
- `/arckit:application-rationalization` for consolidate, retire, replace, or
  retain decisions.
- `/arckit:gap-analysis` for target-state gaps, workload prioritization, and
  opportunities and solutions.
- `/arckit:transition-architecture` for migration planning, transition states,
  work packages, and sequencing.
- `/arckit:architecture-board` for implementation governance, board cadence,
  compliance review, and decision tracking.
- `/arckit:architecture-change` for change requests, impact, approvals, and
  ADM re-entry.
- `/arckit:architecture-repository` for patterns, standards, reference
  architectures, reusable decisions, and lessons learned.

The document codes are `ADMP`, `BPCM`, `APP`, `APPR`, `GAPA`, `TRANS`,
`BORD`, `ACHG`, and `REPO`.

That means TOGAF ADM work becomes ordinary ArcKit output:

```text
projects/003-modernisation/
  ARC-003-ADMP-v1.0.md    # ADM Preliminary / Architecture Vision
  ARC-003-BPCM-v1.0.md    # Business Capability Map
  ARC-003-APP-v1.0.md     # Application Inventory
  ARC-003-APPR-v1.0.md    # Application Rationalization
  ARC-003-GAPA-v1.0.md    # Gap Analysis
  ARC-003-TRANS-v1.0.md   # Transition Architecture
  ARC-003-BORD-v1.0.md    # Architecture Board
```

Global repository synthesis can live where cross-project knowledge belongs:

```text
projects/000-global/ARC-000-REPO-v1.0.md
```

## ADM without a parallel document universe

The useful part is composability.

`/arckit:adm-preliminary` can read principles, stakeholders, and strategy.
`/arckit:business-capability-map` can connect back to requirements and drivers.
`/arckit:application-inventory` gives gap analysis and rationalization a real
portfolio baseline. `transition-architecture` depends on the gap analysis.
`architecture-board` ties implementation governance back to principles and ADM
preliminary work. `architecture-repository` synthesizes reusable knowledge
from completed artefacts.

That keeps ADM work from becoming a parallel universe. It is part of the same
governed architecture project as requirements, risks, ADRs, diagrams, business
cases, procurement notes, and assurance evidence.

## The `togaf-adm-full` recipe

The overlay includes the `togaf-adm-full` build recipe.

The recipe starts with core ArcKit foundations:

```text
principles
  -> requirements + stakeholders
  -> strategy
```

It then builds the ADM flow:

```text
adm preliminary
  -> business capability map
  -> application inventory
  -> application rationalization
  -> gap analysis
  -> transition architecture
  -> architecture board
  -> optional architecture change
  -> optional architecture repository
  -> health + traceability
```

The optional targets matter. Not every architecture cycle needs an immediate
change request. Not every project should synthesize the global architecture
repository on every run. The recipe makes those choices explicit.

## Working with the agent architecture overlay

`arckit-togaf-adm` is useful on its own, but it also composes with
`arckit-agent-architecture`.

That is why the TOGAF plugin includes `togaf-agent-full`. It combines ADM
delivery with the agent inventory, design, governance, integration, security,
and optional maturity outputs from the agent overlay.

Use that combined recipe when the enterprise architecture question and the
agent question are the same delivery problem. For example, a team modernising
a casework platform may also be introducing triage, summarisation, research,
and workflow agents. The capability map, application inventory, transition
architecture, agent design, integration contracts, security posture, and
architecture board need to agree with each other.

The separate agent architecture article covers that overlay in detail. The key
point for TOGAF users is simpler: ADM remains the frame, and agent governance
can sit inside it.

## Getting started

The plugin depends on the core `arckit` Claude Code plugin:

```bash
claude plugin install arckit arckit-togaf-adm
```

Then run the commands directly:

```text
/arckit:adm-preliminary "Casework modernisation"
/arckit:business-capability-map 003
/arckit:application-inventory 003
/arckit:application-rationalization 003
/arckit:gap-analysis 003
/arckit:transition-architecture 003
/arckit:architecture-board 003
/arckit:architecture-change 003
/arckit:architecture-repository 000
```

Or use the build harness:

```text
/arckit:build 003 --recipe togaf-adm-full --plan
/arckit:build 003 --recipe togaf-adm-full
```

If the agent overlay is also installed, use the combined recipe:

```text
claude plugin install arckit arckit-togaf-adm arckit-agent-architecture
/arckit:build 003 --recipe togaf-agent-full --plan
```

## Scope

This first release covers the ADM cycle and the architecture repository:
Preliminary, phases A through H, plus repository synthesis.

It does not attempt to implement the full TOGAF content framework meta-model.
It does not replace organization-specific ADM tailoring guidance. Those are
candidates for future extension work. The initial goal is narrower and more
useful: make ADM-shaped architecture delivery fit ArcKit's governed artefact
model.

## Why this matters

TOGAF is often treated as a method outside the delivery system. ArcKit works
best when the method is inside the work: commands, templates, generated
artefacts, document IDs, dependencies, checks, and traceability.

`arckit-togaf-adm` makes that possible for teams that already speak ADM. It
does not ask them to abandon the method. It gives the method a working surface.

That is the practical value: less ceremony drifting across files, more
architecture work that can be inspected, versioned, challenged, reused, and
connected to the decisions a programme is actually making.

---

*`arckit-togaf-adm` is an MIT-licensed community overlay for Claude Code. It
requires the core `arckit` plugin.*

<!-- arckit:community-block -->
## Join the ArcKit Community

- **Discord** - real-time conversation, help with commands, and what people are building: [discord.gg/HsA4Y3hQ4](https://discord.gg/HsA4Y3hQ4)
- **LinkedIn Group** - announcements, case studies, and longer-form discussion: [linkedin.com/groups/17641034](https://www.linkedin.com/groups/17641034/)
- **GitHub** - code, issues, and contributions: [github.com/tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit)
