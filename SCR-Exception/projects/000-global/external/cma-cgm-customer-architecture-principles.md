---
title: "CMA CGM Customer Domain Architecture Principles"
document_id: "CMA-CUST-PRIN"
version: "1.0"
status: "Proposed"
owner: "Enterprise Architecture - Customer Domain"
organisation: "CMA CGM"
scope:
  - Booking
  - Documentation
  - Invoicing
  - Pricing
  - Customer Care
  - Sales and CRM
  - Value-Added Services (VAS)
intended_consumer: "ArcKit /arckit:principles and AI architecture assistants"
review_cycle: "At least annually and after a major strategy, regulatory, platform, or operating-model change"
classification: "Internal"
---

# CMA CGM Customer Domain Architecture Principles

## 1. Purpose

This file provides the organisation and domain context that an AI assistant MUST use when generating, reviewing, or assessing architecture principles for the CMA CGM customer domain with `/arckit:principles`.

It is a domain knowledge source, not an automatically approved policy. Generated principles and compliance conclusions remain drafts until reviewed by the relevant Enterprise Architect, Domain Architect, security, data, business, and Architecture Review Board stakeholders.

## 2. Instructions to the AI assistant

When this file is present in the ArcKit `external` directory, the assistant MUST:

1. Treat every `MUST` statement as a mandatory architecture constraint unless a documented exception is approved.
2. Treat every `SHOULD` statement as the preferred design, requiring explicit justification when not followed.
3. Preserve the principle identifiers defined in this file.
4. Include, for every generated principle: statement, rationale, implications, evidence, validation gates, and exception conditions.
5. Map each principle to the relevant domains: Booking, Documentation, Invoicing, Pricing, Customer Care, Sales/CRM, and VAS.
6. Distinguish business ownership, data ownership, application ownership, and platform ownership.
7. Identify contradictions between requirements, target architecture, existing systems, and these principles.
8. Never invent CMA CGM policies, application capabilities, data classifications, regulatory obligations, owners, SLAs, or roadmaps. Mark missing information as `TBD` and request validation in the generated artefact.
9. Prefer domain-level contracts and reusable enterprise capabilities over point-to-point or consumer-specific solutions.
10. Record deviations as architecture decisions and time-bound exceptions with an owner, rationale, risk, expiry date, and remediation plan.

## 3. Domain context

The customer domain covers the end-to-end customer journey from commercial engagement and quotation through booking, transport documentation, invoicing, customer service, and the sale and fulfilment of Value-Added Services.

The architecture must support:

- consistent customer experiences across web, API, EDI, email, assisted-service, and internal channels;
- clear separation of channel, orchestration, domain execution, and system-of-record responsibilities;
- reusable business capabilities exposed through governed contracts;
- traceability of customer requests and business transactions across domains;
- progressive modernization without uncontrolled duplication or disruption of operational processes;
- regulatory, tax, customs, trade, security, privacy, and audit requirements;
- global standards with controlled local variation;
- VAS discovery, eligibility, pricing, recommendation, sale, fulfilment, invoicing, and reporting.

## 4. Core architecture principles

### CUST-001 — Customer Journey First, Domain Ownership Always

**Statement**  
Solutions MUST optimize the end-to-end customer journey while preserving explicit ownership of each business capability and transaction by the responsible domain.

**Rationale**  
A customer request can cross Sales, Pricing, Booking, Documentation, Invoicing, Care, and VAS. Customer experience must be seamless without creating a central application that absorbs every domain responsibility.

**Implications**

- Channels may coordinate the experience but MUST NOT own domain execution rules that belong to Booking, Pricing, Documentation, Invoicing, Care, Sales, or VAS.
- Each domain MUST expose a stable business contract for its capability.
- Cross-domain journeys MUST identify the owner of each step, business object, decision, and outcome.

**Evidence**

- capability map and domain ownership matrix;
- customer journey and business-process model;
- API/event ownership catalogue;
- architecture decision records.

**Validation gates**

- [ ] Every business capability has one accountable domain owner.
- [ ] Channel responsibilities are separated from domain execution responsibilities.
- [ ] Cross-domain hand-offs and outcomes are documented.
- [ ] No consumer directly depends on a domain's internal workflow implementation.

**Exceptions**  
Temporary orchestration may be accepted only with an approved target-state transition plan.

**Applies to**: All customer domains.

---

### CUST-002 — Omnichannel Consistency

**Statement**  
Equivalent customer intentions MUST produce consistent business outcomes regardless of whether they originate from web, API, EDI, email, voice, chat, assisted service, or internal operations.

**Rationale**  
Channel-specific implementations create inconsistent rules, duplicated integrations, and different outcomes for the same customer need.

**Implications**

- Channel information SHOULD be retained for traceability and analytics but MUST NOT change core domain rules unless a documented business exception exists.
- Structured and unstructured requests SHOULD converge toward common business commands, events, and statuses.
- Customer-facing status terminology SHOULD be consistent across channels.

**Evidence**

- channel-to-intent mapping;
- canonical request and status models;
- parity tests across channels;
- exception register.

**Validation gates**

- [ ] The same intent maps to the same domain capability.
- [ ] Channel-specific differences are explicit and justified.
- [ ] Statuses and error meanings are consistent across consuming channels.

**Exceptions**  
Regulatory, contractual, security, or operational channel constraints may justify a controlled variation.

**Applies to**: Booking, Documentation, Invoicing, Care, Sales/CRM, Pricing, VAS.

---

### CUST-003 — Domain Contracts over Internal Implementations

**Statement**  
Domains MUST expose capabilities through governed APIs, business events, or approved data products. Consumers MUST NOT call workflow engines, databases, bots, or internal components directly.

**Rationale**  
Stable contracts reduce coupling and allow domains to replace internal implementations without disrupting consumers.

**Implications**

- API-first or event-first does not mean one technology for every use case; the interaction pattern MUST match the business need.
- Workflow products such as process engines remain internal implementation details.
- Direct database integration requires an approved exception.

**Evidence**

- OpenAPI or AsyncAPI contracts;
- interaction catalogue;
- sequence diagrams;
- consumer and provider ownership;
- versioning and deprecation policy.

**Validation gates**

- [ ] The provider domain owns the exposed contract.
- [ ] No consumer invokes an internal workflow engine directly.
- [ ] No new point-to-point database dependency is introduced.
- [ ] Contract versioning, compatibility, and deprecation are defined.

**Exceptions**  
Time-bound legacy integration may be accepted with risk ownership and a migration plan.

**Applies to**: All customer domains.

---

### CUST-004 — Business Events for Cross-Domain State Changes

**Statement**  
Significant cross-domain business state changes SHOULD be published as governed business events when asynchronous distribution, decoupling, or multiple consumers are required.

**Rationale**  
Events allow Booking, Documentation, Invoicing, Care, Sales, Pricing, and VAS to evolve independently while sharing meaningful business outcomes.

**Implications**

- Events MUST represent completed or requested business facts, not technical table updates.
- Producers own event semantics; consumers own their reactions.
- Delivery, ordering, idempotency, replay, retention, and error handling MUST be designed explicitly.

**Evidence**

- event catalogue and schemas;
- producer/consumer matrix;
- idempotency and replay design;
- operational monitoring plan.

**Validation gates**

- [ ] Event names and payloads express business meaning.
- [ ] Events include correlation and causation identifiers.
- [ ] Duplicate, late, failed, and replayed events are handled.
- [ ] Sensitive data is minimized in event payloads.

**Exceptions**  
Synchronous APIs may be preferred when the caller requires an immediate authoritative response.

**Applies to**: All customer domains.

---

### CUST-005 — End-to-End Correlation and Auditability

**Statement**  
Every customer request that spans systems or domains MUST carry an end-to-end correlation identifier from intake through execution, status reporting, human intervention, and closure.

**Rationale**  
Cross-domain traceability is required for customer service, operational support, audit, troubleshooting, and performance analysis.

**Implications**

- Local identifiers such as case, booking, shipment, quotation, contract, invoice, or VAS order IDs MUST be linked to the shared correlation identifier.
- Logs and events MUST support reconstruction of the business journey without exposing unnecessary personal or commercial data.

**Evidence**

- correlation-ID specification;
- logging and observability design;
- trace examples across systems;
- audit-retention rules.

**Validation gates**

- [ ] Correlation starts at the earliest controlled intake point.
- [ ] All participating components propagate or map the identifier.
- [ ] Support teams can reconstruct the complete transaction path.

**Exceptions**  
Legacy systems unable to propagate the identifier require an adapter mapping and a documented sunset plan.

**Applies to**: All customer domains.

---

### CUST-006 — Authoritative Sources and Single Ownership of Business Data

**Statement**  
Each critical business object and rule set MUST have one declared authoritative source and one accountable owner. Copies MUST be read-only, derived, or synchronized through governed mechanisms.

**Rationale**  
Multiple editable masters create inconsistent customer, quotation, booking, document, invoice, tariff, eligibility, and VAS information.

**Implications**

- Architecture documents MUST distinguish system of record, system of engagement, analytical copy, cache, and reporting view.
- Editable duplication and dual mastering are prohibited unless explicitly approved.
- Consumers SHOULD access mastered data through approved APIs, events, reference services, or governed data products.

**Evidence**

- business-object catalogue;
- data ownership and stewardship matrix;
- source-to-consumer lineage;
- synchronization and reconciliation controls.

**Validation gates**

- [ ] Every critical data object has an authoritative source.
- [ ] Update rights and stewardship are explicit.
- [ ] Derived stores have reconciliation and freshness controls.
- [ ] No uncontrolled Excel or local mapping becomes a de facto master.

**Exceptions**  
Temporary co-existence during migration requires conflict-resolution rules and an exit date.

**Applies to**: All customer domains, especially Pricing, Customer Profile, Booking, Invoicing, and VAS referentials.

---

### CUST-007 — Customer Profile and Party Consistency

**Statement**  
Customer, partner, payer, shipper, consignee, notify party, and related-party identities MUST use governed identifiers and approved reference services across customer-domain processes.

**Rationale**  
Reliable party identification is foundational for quotation, booking, documentation, invoicing, customer care, authorization, sanctions controls, and VAS eligibility.

**Implications**

- Local party copies MUST retain links to governed enterprise identifiers.
- Matching or AI confidence thresholds MUST be explicit, testable, and route uncertain cases to human review.
- Applications MUST NOT create independent identity-matching rules without governance.

**Evidence**

- party model and identifier mapping;
- matching rules and thresholds;
- manual-review process;
- data-quality metrics.

**Validation gates**

- [ ] The authoritative party identifier is used or mapped.
- [ ] Ambiguous matches are not silently accepted.
- [ ] Authorization uses the correct customer-party relationship.

**Exceptions**  
Local legal identifiers may supplement, but not replace, governed enterprise identity links.

**Applies to**: Booking, Documentation, Invoicing, Care, Sales/CRM, Pricing, VAS.

---

### CUST-008 — Security, Privacy, and Commercial Confidentiality by Design

**Statement**  
Identity, access control, privacy, commercial confidentiality, fraud prevention, segregation of duties, and audit requirements MUST be designed from the start and enforced consistently across channels and domains.

**Rationale**  
Customer-domain solutions process sensitive customer, commercial, contractual, shipment, payment, document, and pricing information.

**Implications**

- Access MUST follow least privilege and business-purpose limitation.
- Customer-facing APIs MUST verify that the caller is authorized for the relevant customer, booking, shipment, contract, document, invoice, or case.
- Secrets and personal or commercially sensitive data MUST NOT appear in source code, prompts, logs, events, or test data unless specifically protected and approved.

**Evidence**

- threat model;
- access-control matrix;
- privacy and data-classification assessment;
- security testing;
- audit and fraud controls.

**Validation gates**

- [ ] Authentication and authorization are addressed separately.
- [ ] Object-level authorization is enforced.
- [ ] Sensitive data is minimized and protected in transit and at rest.
- [ ] Privileged and financial actions are auditable.

**Exceptions**  
No exception may bypass legal or mandatory security obligations. Other exceptions require security approval and compensating controls.

**Applies to**: All customer domains.

---

### CUST-009 — Global Standard, Controlled Local Variation

**Statement**  
Customer-domain capabilities MUST use global processes, contracts, and platforms by default. Local variations MUST be externalized, traceable, and limited to verified regulatory, tax, customs, contractual, or operational needs.

**Rationale**  
Uncontrolled local customization increases cost, inconsistency, and technical debt, while maritime operations still require legitimate country and agency variations.

**Implications**

- Local rules SHOULD be configuration or governed rule assets, not code forks.
- Every localization MUST identify jurisdiction, owner, rationale, validity period, and test evidence.
- The global model MUST remain usable without embedding local assumptions.

**Evidence**

- localization register;
- rule catalogue;
- country and agency configuration model;
- regression test suite.

**Validation gates**

- [ ] The global flow is defined first.
- [ ] Local deviations have an explicit legal or business basis.
- [ ] Local logic is externalized and versioned.
- [ ] Expired local rules can be detected and removed.

**Exceptions**  
A local implementation is permitted only where the global platform cannot meet a mandatory requirement and a convergence plan exists.

**Applies to**: Booking, Documentation, Invoicing, Pricing, Care, Sales/CRM, VAS.

---

### CUST-010 — Automation with Explicit Human Control

**Statement**  
Automation and AI SHOULD maximize straight-through processing, but uncertain, high-risk, exceptional, or regulated cases MUST be routed to controlled human review with context, reason, and audit trail.

**Rationale**  
Booking, documentation, invoicing, pricing, care, and VAS decisions can have operational, financial, legal, or customer impacts.

**Implications**

- Automation eligibility, confidence, validation, and fallback rules MUST be explicit.
- A failed automated attempt MUST produce a meaningful status and recoverable workflow.
- Human reviewers MUST receive the evidence needed to understand and override the result.

**Evidence**

- automation decision table;
- confidence thresholds;
- human-in-the-loop workflow;
- model and rule monitoring;
- override audit records.

**Validation gates**

- [ ] Happy path and manual fallback are both designed.
- [ ] Confidence and exception thresholds are approved.
- [ ] Automation failures do not silently lose or duplicate requests.
- [ ] Human overrides are traceable.

**Exceptions**  
Fully autonomous execution requires explicit risk acceptance and evidence that the decision class is appropriate for automation.

**Applies to**: All customer domains, especially email processing, booking automation, pricing recommendations, invoice processing, and VAS recommendations.

---

### CUST-011 — VAS as Reusable Product Capabilities

**Statement**  
VAS information and execution MUST be modeled as reusable product capabilities covering catalogue, classification, eligibility, applicability, pricing, recommendation, sale, fulfilment, invoicing, and reporting.

**Rationale**  
VAS must be consistently discoverable and sellable across channels and customer journey stages without duplicating product logic in every touchpoint.

**Implications**

- VAS catalogue and classification MUST have governed ownership.
- Eligibility and applicability rules SHOULD be provided through reusable domain services.
- Recommendation engines MUST NOT become the authoritative source for catalogue, eligibility, or price.
- VAS sales, fulfilment, charge codes, invoice treatment, and revenue reporting MUST be traceable end to end.

**Evidence**

- VAS capability and product model;
- catalogue and eligibility contracts;
- charge-code and revenue mappings;
- recommendation-to-sale traceability;
- fulfilment and invoicing flows.

**Validation gates**

- [ ] A single governed VAS definition is reused by channels.
- [ ] Eligibility, price, recommendation, and fulfilment responsibilities are separated.
- [ ] Product and charge-code mappings are governed.
- [ ] Bundles and revenue splits have explicit business rules.

**Exceptions**  
A pilot may use a limited local catalogue only if it does not become an uncontrolled enterprise reference.

**Applies to**: Sales/CRM, Pricing, Booking, Invoicing, Care, VAS.

---

### CUST-012 — Pricing Authority and Quote-to-Invoice Traceability

**Statement**  
Pricing decisions MUST be calculated or validated by the authoritative Pricing capability, and the commercial basis of a sale MUST remain traceable from quotation and contract through booking, VAS selection, charge calculation, and invoice.

**Rationale**  
Duplicated pricing logic creates margin leakage, inconsistent quotations, disputes, and invoice discrepancies.

**Implications**

- Channels and consuming domains MUST NOT reimplement authoritative tariff, surcharge, contract, or eligibility calculations.
- Derived pricing caches require freshness, reconciliation, and expiry controls.
- Adjustments, overrides, leeways, and exceptions MUST be authorized and auditable.

**Evidence**

- quote-to-booking-to-invoice lineage;
- pricing API or event contracts;
- override matrix;
- reconciliation and discrepancy reports.

**Validation gates**

- [ ] The authoritative source of each price component is declared.
- [ ] Manual overrides have authorization and audit controls.
- [ ] Booking and invoice can reference the applicable quotation or contract basis.
- [ ] VAS price and charge-code treatment are traceable.

**Exceptions**  
Offline or resilience modes require bounded validity and post-restoration reconciliation.

**Applies to**: Pricing, Sales/CRM, Booking, Invoicing, VAS.

---

### CUST-013 — Regulatory and Document Integrity

**Statement**  
Customer documents, invoices, customs information, shipping instructions, bills of lading, certificates, and related evidence MUST preserve integrity, provenance, version, legal status, and retention requirements throughout their lifecycle.

**Rationale**  
Documentation and invoicing artefacts may carry contractual, customs, tax, trade, and financial obligations.

**Implications**

- Draft, issued, amended, cancelled, and archived states MUST be explicit.
- Generated documents MUST be reproducible from controlled data and templates where required.
- Amendments MUST preserve a complete audit history.
- Country-specific requirements MUST follow CUST-009.

**Evidence**

- document lifecycle model;
- version and amendment history;
- template governance;
- retention and legal-hold rules;
- integrity controls.

**Validation gates**

- [ ] Document state and legal status are distinguishable.
- [ ] Source data and template version are traceable.
- [ ] Amendments do not overwrite audit history.
- [ ] Retention and access rules are documented.

**Exceptions**  
None for mandatory legal integrity or retention controls.

**Applies to**: Documentation, Invoicing, Booking, Care.

---

### CUST-014 — Resilience Proportional to Customer and Operational Impact

**Statement**  
Availability, recovery, performance, and continuity requirements MUST be defined from customer impact and operational criticality rather than inherited from a technology default.

**Rationale**  
Failures in quotation, booking, documentation, invoicing, care, or VAS can disrupt shipments, revenue, regulatory processing, and customer trust.

**Implications**

- Critical journeys and peak-load scenarios MUST be identified.
- Dependencies, degraded modes, queues, retries, timeouts, and recovery procedures MUST be explicit.
- Synchronous chains SHOULD be minimized across domains.

**Evidence**

- business impact analysis;
- SLOs and recovery objectives;
- load and resilience tests;
- dependency map;
- disaster-recovery and continuity evidence.

**Validation gates**

- [ ] Critical business journeys are prioritized.
- [ ] Failure of a dependency has a defined behavior.
- [ ] Capacity and performance evidence exists for expected peaks.
- [ ] Recovery is tested, not only documented.

**Exceptions**  
Temporary reduced resilience requires explicit business risk acceptance and a remediation date.

**Applies to**: All customer domains.

---

### CUST-015 — Observability in Business Terms

**Statement**  
Customer-domain services MUST expose technical and business observability that allows teams to understand request volume, processing status, failures, retries, automation outcomes, and customer impact.

**Rationale**  
Technical health alone does not show whether bookings, documents, invoices, cases, quotations, or VAS orders are progressing successfully.

**Implications**

- Monitoring MUST include business states and correlation identifiers.
- Alerts SHOULD identify the responsible domain and operational action.
- Metrics MUST avoid exposing unnecessary personal or commercially sensitive data.

**Evidence**

- telemetry specification;
- dashboards and alert catalogue;
- business KPI definitions;
- runbooks.

**Validation gates**

- [ ] Business success and failure are measurable.
- [ ] Operational ownership is clear for alerts.
- [ ] Cross-domain traces are available.
- [ ] Monitoring covers automated and manual queues.

**Exceptions**  
None for critical production services; implementation depth may be phased with an approved plan.

**Applies to**: All customer domains.

---

### CUST-016 — Reuse before Build, Simplify before Automate

**Statement**  
Teams MUST assess existing CMA CGM capabilities, contracts, platforms, and shared services before creating a new component. Processes SHOULD be simplified and standardized before automation.

**Rationale**  
New local services, bots, mappings, and workflow variants increase cost, inconsistency, and support complexity.

**Implications**

- Architecture studies MUST document reuse options and the rationale for build, buy, reuse, or retire decisions.
- Automation MUST NOT preserve unnecessary process complexity by default.
- Reused capability fitness MUST be validated for functional, security, performance, and lifecycle needs.

**Evidence**

- option assessment;
- capability and application landscape;
- reuse decision record;
- process simplification analysis.

**Validation gates**

- [ ] Existing capabilities were assessed.
- [ ] Duplication is justified by measurable constraints.
- [ ] The process was simplified before automation.
- [ ] Ownership and support model are defined.

**Exceptions**  
A tactical component may be accepted when reuse cannot meet a mandatory deadline, with a retirement or convergence plan.

**Applies to**: All customer domains.

---

### CUST-017 — Progressive Modernization and Controlled Technical Debt

**Statement**  
Modernization MUST preserve business continuity while moving toward the target architecture. New technical debt and deviations MUST be explicit, owned, risk-assessed, time-bound, and tracked to remediation.

**Rationale**  
The customer landscape includes legacy platforms, local solutions, RPAs, shared databases, and strategic modernization programmes that cannot all change at once.

**Implications**

- Transitional architectures MUST distinguish temporary and target components.
- New consumers SHOULD NOT be connected to a retiring pattern without approval.
- Migration, coexistence, reconciliation, rollback, and decommissioning MUST be designed together.

**Evidence**

- transition-state diagrams;
- migration roadmap;
- derogation and technical-debt register;
- decommissioning criteria;
- rollback plan.

**Validation gates**

- [ ] Current, transition, and target states are explicit.
- [ ] The change does not create an unowned permanent interim solution.
- [ ] Data and transaction reconciliation are planned.
- [ ] Legacy retirement criteria and dependencies are documented.

**Exceptions**  
Exceptions require ARB approval, owner, risk, expiry date, and funded remediation path.

**Applies to**: All customer domains.

---

### CUST-018 — Technology and Vendor Portability

**Statement**  
Business capabilities and data contracts SHOULD remain portable across technology products and vendors. Application consumers MUST depend on business contracts rather than product-specific features wherever practicable.

**Rationale**  
Portability reduces lock-in and allows CMA CGM to evolve platforms, workflow engines, AI models, integration technologies, and hosting choices.

**Implications**

- Product-specific logic SHOULD be isolated behind domain or platform interfaces.
- Data MUST be exportable in documented formats.
- Exit, migration, and continuity requirements MUST be considered for strategic vendors and SaaS products.

**Evidence**

- abstraction and adapter design;
- exit strategy;
- data export test;
- dependency assessment;
- ADRs.

**Validation gates**

- [ ] Business consumers do not depend unnecessarily on proprietary internals.
- [ ] Data portability and exit paths are documented.
- [ ] Replacement impact is understood.

**Exceptions**  
Deliberate product coupling may be accepted where benefits outweigh exit risk and the decision is recorded.

**Applies to**: All customer domains.

## 5. Domain-specific extensions

### Booking

- Booking execution rules MUST remain owned by the Booking domain.
- Channels and assistants SHOULD submit governed booking commands or events rather than manipulate booking workflows directly.
- Amendments, cancellation, reactivation, partner validation, equipment, route, voyage, allocation, and pricing dependencies MUST be explicit.
- Automated booking decisions MUST provide manual fallback and traceability.

### Documentation

- Shipping instructions and document amendments MUST use controlled lifecycle states and preserve audit history.
- Document automation MUST validate mandatory information and route incomplete or ambiguous requests for human review.
- Customs and country-specific document rules MUST be externalized and governed.

### Invoicing

- Invoice generation, tax treatment, currency, charge, grouped invoice, payment, credit, refund, and document requirements MUST have explicit ownership.
- Customer-specific formats SHOULD converge toward a standard model; unavoidable variations MUST be governed.
- Invoice outputs MUST remain traceable to their underlying local invoices, charges, quotations, contracts, and business transactions where applicable.

### Pricing

- Tariff, surcharge, contract, quotation, and pricing-rule ownership MUST be explicit.
- Pricing logic MUST NOT be duplicated in e-commerce, booking, sales, care, or VAS channels.
- Event-driven publication may distribute tariff changes, while authoritative evaluation MUST remain governed by Pricing.

### Customer Care

- Care platforms SHOULD manage customer interaction, case context, routing, communication, and human work, not take ownership of downstream domain execution.
- Automation failures MUST return meaningful statuses that can trigger a case or manual workflow.
- Knowledge used for customer answers MUST be governed, current, attributable, and access-controlled.

### Sales and CRM

- CRM SHOULD own commercial engagement, opportunities, activities, and sales processes, while consuming authoritative product, pricing, booking, invoice, and service information from their domains.
- Customer 360 views MUST identify source, freshness, and authorization for each data element.
- AI recommendations MUST be explainable enough for sales use and MUST remain distinct from authoritative eligibility and pricing decisions.

### Value-Added Services

- A governed VAS index/catalogue MUST support consistent product names, categories, descriptions, eligibility, applicability, pricing references, charge-code mappings, and lifecycle states.
- VAS recommendations MAY prioritize opportunities but MUST call authoritative services for eligibility and price before sale.
- VAS bundles, leeways, exceptions, fulfilment steps, charge codes, invoicing, and revenue splits MUST be explicitly modeled.
- VAS capabilities SHOULD be available consistently across quotation, booking, post-booking, care, and sales touchpoints.

## 6. Mandatory output structure for `/arckit:principles`

When generating the ArcKit principles artefact from this source, use the following structure:

1. Executive summary
2. Scope and applicability
3. Business and regulatory drivers
4. Principle catalogue
5. Domain applicability matrix
6. Design review checklist
7. Evidence and compliance expectations
8. Exception and derogation process
9. Open questions and assumptions
10. Approval and review history

For each principle, emit:

```markdown
### <ID> — <Name>

**Statement**: <testable MUST/SHOULD statement>

**Rationale**: <why this principle exists>

**Implications**:
- <design consequence>

**Evidence**:
- <required artefact or proof>

**Validation gates**:
- [ ] <testable control>

**Exceptions**: <approver, expiry, remediation expectations>

**Applies to**: <domains>
```

## 7. Exception and derogation requirements

Any exception MUST record:

- principle ID;
- impacted domain, capability, application, interface, or data object;
- business justification;
- alternatives assessed;
- security, data, operational, financial, customer, and regulatory risks;
- compensating controls;
- accountable owner;
- approving governance body;
- approval date and expiry date;
- remediation or convergence plan;
- review status.

An exception MUST NOT be presented as compliance. Expired exceptions MUST be treated as non-compliance until renewed or remediated.

## 8. Minimum design-review checklist

Before recommending an architecture, the assistant MUST verify:

- [ ] Customer journey and business outcome are clear.
- [ ] Domain boundaries and owners are clear.
- [ ] Systems of record are declared.
- [ ] API, event, and data-product contracts are governed.
- [ ] No internal workflow or database is exposed directly without exception.
- [ ] Correlation and auditability are end to end.
- [ ] Security, privacy, authorization, and confidentiality are addressed.
- [ ] Global and local rules are separated.
- [ ] Manual fallback exists for uncertain automation.
- [ ] Pricing and VAS responsibilities are separated correctly.
- [ ] Resilience and observability reflect business criticality.
- [ ] Reuse options and target-state alignment are assessed.
- [ ] Technical debt, migration, and decommissioning are explicit.
- [ ] Missing information is marked `TBD`, not invented.

## 9. Suggested ArcKit invocation context

Use this file as an external knowledge source, then invoke:

```text
/arckit:principles
Create organisation and domain architecture principles for CMA CGM's Customer domain.
Use external/cma-cgm-customer-architecture-principles.md as mandatory context.
Preserve all CUST principle identifiers, identify contradictions and duplicates,
and generate a concise, testable, evidence-based principles artefact for ARB review.
Do not invent policies, owners, systems, deadlines, regulations, or capabilities.
Mark unsupported information as TBD.
```

## 10. Approval note

This document is a proposed domain baseline prepared to guide AI-generated architecture work. It MUST be reconciled with the official CMA CGM Enterprise Architecture principles, cybersecurity standards, data governance policies, integration standards, cloud standards, AI governance rules, and applicable legal or regulatory requirements before formal adoption.
