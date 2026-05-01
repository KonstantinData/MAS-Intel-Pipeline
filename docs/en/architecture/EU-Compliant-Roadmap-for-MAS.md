# EU-Compliant Roadmap for a Multi-Agent System on GitHub

## Implementation guide with validated implementation information

**As of:** 01.05.2026
**Scope:** Python-based multi-agent system on GitHub
**Classification:** technical and organizational implementation recommendation, not legal advice

---

## 0. Binding planning baseline

### 0.1 Regulatory source baseline

This roadmap uses the following validated foundations:

| Area                              | Validated status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EU AI Act                         | In force since 01.08.2024. Prohibitions and AI literacy obligations apply since 02.02.2025. GPAI rules apply since 02.08.2025. General application from 02.08.2026. High-risk systems in regulated products with transition period until 02.08.2027. Source: European Commission, AI Act Timeline. ([Shaping Europe’s digital future]([https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com)"AI Act                                             |
| Digital Omnibus / High-risk shift | The Council of the EU proposed a position on 13.03.2026 according to which high-risk rules would be shifted to 02.12.2027 for stand-alone high-risk systems and 02.08.2028 for high-risk systems in products. This is to be tracked as a scenario, not as the sole operational basis. Source: Council of the EU, 13.03.2026. ([Council of the European Union](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/?utm_source=chatgpt.com "Council agrees position to streamline rules on Artificial ...")) |
| GDPR                              | Art. 5 contains, among other things, lawfulness, purpose limitation, data minimization, storage limitation, integrity/confidentiality, and accountability. Art. 25 requires data protection by design and by default. Source: EUR-Lex, Regulation (EU) 2016/679. ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng?utm_source=chatgpt.com "Regulation - 2016/679 - EN - gdpr - EUR-Lex - European Union"))                                                                                                                                                                             |
| CRA                               | Regulation (EU) 2024/2847. Full application from 11.12.2027. Reporting obligations for actively exploited vulnerabilities and serious security incidents from 11.09.2026. Source: European Commission and EUR-Lex. ([Shaping Europe’s digital future](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting?utm_source=chatgpt.com "Cyber Resilience Act - Reporting obligations"))                                                                                                                                                                                                    |
| GitHub Actions Security           | GitHub recommends full commit-SHA pinning because only this variant references an action release immutably. Source: GitHub Docs. ([GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com "Secure use reference - GitHub Docs"))                                                                                                                                                                                                                                                                                                                    |
| GitHub Artifact Attestations      | GitHub Artifact Attestations produce cryptographically signed provenance and integrity evidence for build artifacts. Source: GitHub Docs. ([GitHub Docs](https://docs.github.com/en/actions/concepts/security/artifact-attestations?utm_source=chatgpt.com "Artifact attestations - GitHub Docs"))                                                                                                                                                                                                                                                                                                |
| Agentic AI Security               | OWASP Top 10 for Agentic Applications 2026 names, among other things, Agent Goal Hijack, Tool Misuse, and Identity & Privilege Abuse as central risks. Source: OWASP, 09.12.2025. ([OWASP Gen AI Security Project](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/?utm_source=chatgpt.com "OWASP Top 10 for Agentic Applications for 2026"))                                                                                                                                                                                                                     |
| AI/ML-BOM                         | CycloneDX describes AI/ML-BOMs as a transparency instrument for models, datasets, dependencies, provenance, training methods, and configuration. Source: CycloneDX. ([cyclonedx.org](https://cyclonedx.org/capabilities/mlbom/?utm_source=chatgpt.com "Machine Learning Bill of Materials (AI/ML-BOM)"))                                                                                                                                                                                                                                                                                          |
| AI Management System              | ISO/IEC 42001:2023 is a management system standard for establishing, operating, maintaining, and continuously improving an AI management system. Source: ISO. ([ISO](https://www.iso.org/standard/42001?utm_source=chatgpt.com "ISO/IEC 42001:2023 - AI management systems"))                                                                                                                                                                                                                                                                                                                     |
| Generative AI risk management     | NIST AI 600-1 is a Generative AI profile for NIST AI RMF 1.0 and serves voluntary risk management of generative AI systems. Source: NIST, 2024. ([NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence?utm_source=chatgpt.com "Artificial Intelligence Risk Management Framework"))                                                                                                                                                                                                                                       |

---

## 1. Target architecture

The repository is run as a  **controlled compliance, security, privacy, model, and agent lifecycle** .

The repository itself is not automatically the regulated product. The following are assessed per release:

1. Use case
2. Deployment context
3. Role under the AI Act
4. Role under the CRA
5. Data classes
6. Model routes
7. Agent permissions
8. Tool permissions
9. Auditability
10. Release artifacts

---

## 2. Create repository structure

### 2.1 Target structure

```text
.
├── .github/
│   ├── CODEOWNERS
│   └── workflows/
│       ├── compliance-security-ai.yml
│       └── release-attestation.yml
│
├── bom/
│   ├── sbom/
│   ├── ai-bom/
│   └── ml-bom/
│
├── docs/
│   ├── de/
│   │   ├── architecture/
│   │   │   └── EU-Konforme-Roadmap-fuer-MAS.md
│   │   │
│   │   ├── ai-act/
│   │   │   ├── ai-system-card.md
│   │   │   ├── risk-classification.md
│   │   │   ├── provider-deployer-role-classification.md
│   │   │   ├── prohibited-practices-check.md
│   │   │   ├── human-oversight-matrix.md
│   │   │   ├── technical-documentation.md
│   │   │   ├── fundamental-rights-impact-assessment.md
│   │   │   ├── post-market-monitoring-plan.md
│   │   │   ├── serious-incident-response-ai.md
│   │   │   ├── corrective-action-process.md
│   │   │   └── ai-system-change-control.md
│   │   │
│   │   ├── ai-governance/
│   │   │   ├── ai-management-system.md
│   │   │   ├── ai-policy.md
│   │   │   ├── ai-risk-management-process.md
│   │   │   ├── ai-impact-assessment-template.md
│   │   │   ├── ai-literacy-program.md
│   │   │   └── ai-change-management.md
│   │   │
│   │   ├── privacy/
│   │   │   ├── dpia-draft.md
│   │   │   ├── data-flow-map.md
│   │   │   ├── data-classification-policy.md
│   │   │   ├── pii-handling-policy.md
│   │   │   ├── retention-policy.md
│   │   │   ├── deletion-policy.md
│   │   │   ├── model-privacy-policy.md
│   │   │   ├── international-transfer-assessment.md
│   │   │   ├── subprocessor-register.md
│   │   │   ├── ai-vendor-due-diligence.md
│   │   │   └── audit-log-minimization-policy.md
│   │   │
│   │   ├── security/
│   │   │   ├── threat-model.md
│   │   │   ├── secure-development-policy.md
│   │   │   ├── agent-to-agent-security.md
│   │   │   ├── incident-response-plan.md
│   │   │   ├── vulnerability-disclosure-policy.md
│   │   │   ├── cra-vulnerability-reporting.md
│   │   │   ├── coordinated-vulnerability-disclosure.md
│   │   │   ├── vulnerability-handling-sla.md
│   │   │   ├── security-update-policy.md
│   │   │   ├── support-period-policy.md
│   │   │   ├── sandboxed-execution-policy.md
│   │   │   └── tool-registry-security.md
│   │   │
│   │   ├── models/
│   │   │   ├── model-inventory.md
│   │   │   ├── model-routing-policy.md
│   │   │   ├── local-model-policy.md
│   │   │   ├── cloud-model-policy.md
│   │   │   └── model-cards/
│   │   │
│   │   ├── agents/
│   │   │   ├── agent-inventory.md
│   │   │   ├── agent-permission-matrix.md
│   │   │   ├── agent-communication-policy.md
│   │   │   └── agent-cards/
│   │   │
│   │   ├── licenses/
│   │   │   ├── license-policy.md
│   │   │   ├── model-license-policy.md
│   │   │   ├── dataset-license-policy.md
│   │   │   └── third-party-notices.md
│   │   │
│   │   ├── audit/
│   │   │   ├── audit-policy.md
│   │   │   ├── logging-schema.md
│   │   │   ├── evidence-retention-policy.md
│   │   │   └── release-attestation-policy.md
│   │   │
│   │   └── risk/
│   │       ├── nist-ai-rmf-map.md
│   │       ├── genai-risk-profile.md
│   │       ├── eval-and-red-team-plan.md
│   │       └── model-behavior-monitoring.md
│   │
│   └── en/
│       ├── architecture/
│       │   └── EU-Compliant-Roadmap-for-MAS.md
│       │
│       ├── ai-act/
│       │   ├── ai-system-card.md
│       │   ├── risk-classification.md
│       │   ├── provider-deployer-role-classification.md
│       │   ├── prohibited-practices-check.md
│       │   ├── human-oversight-matrix.md
│       │   ├── technical-documentation.md
│       │   ├── fundamental-rights-impact-assessment.md
│       │   ├── post-market-monitoring-plan.md
│       │   ├── serious-incident-response-ai.md
│       │   ├── corrective-action-process.md
│       │   └── ai-system-change-control.md
│       │
│       ├── ai-governance/
│       │   ├── ai-management-system.md
│       │   ├── ai-policy.md
│       │   ├── ai-risk-management-process.md
│       │   ├── ai-impact-assessment-template.md
│       │   ├── ai-literacy-program.md
│       │   └── ai-change-management.md
│       │
│       ├── privacy/
│       │   ├── dpia-draft.md
│       │   ├── data-flow-map.md
│       │   ├── data-classification-policy.md
│       │   ├── pii-handling-policy.md
│       │   ├── retention-policy.md
│       │   ├── deletion-policy.md
│       │   ├── model-privacy-policy.md
│       │   ├── international-transfer-assessment.md
│       │   ├── subprocessor-register.md
│       │   ├── ai-vendor-due-diligence.md
│       │   └── audit-log-minimization-policy.md
│       │
│       ├── security/
│       │   ├── threat-model.md
│       │   ├── secure-development-policy.md
│       │   ├── agent-to-agent-security.md
│       │   ├── incident-response-plan.md
│       │   ├── vulnerability-disclosure-policy.md
│       │   ├── cra-vulnerability-reporting.md
│       │   ├── coordinated-vulnerability-disclosure.md
│       │   ├── vulnerability-handling-sla.md
│       │   ├── security-update-policy.md
│       │   ├── support-period-policy.md
│       │   ├── sandboxed-execution-policy.md
│       │   └── tool-registry-security.md
│       │
│       ├── models/
│       │   ├── model-inventory.md
│       │   ├── model-routing-policy.md
│       │   ├── local-model-policy.md
│       │   ├── cloud-model-policy.md
│       │   └── model-cards/
│       │
│       ├── agents/
│       │   ├── agent-inventory.md
│       │   ├── agent-permission-matrix.md
│       │   ├── agent-communication-policy.md
│       │   └── agent-cards/
│       │
│       ├── licenses/
│       │   ├── license-policy.md
│       │   ├── model-license-policy.md
│       │   ├── dataset-license-policy.md
│       │   └── third-party-notices.md
│       │
│       ├── audit/
│       │   ├── audit-policy.md
│       │   ├── logging-schema.md
│       │   ├── evidence-retention-policy.md
│       │   └── release-attestation-policy.md
│       │
│       └── risk/
│           ├── nist-ai-rmf-map.md
│           ├── genai-risk-profile.md
│           ├── eval-and-red-team-plan.md
│           └── model-behavior-monitoring.md
│
├── policies/
│   ├── opa/
│   ├── rego/
│   ├── agent-guardrails/
│   ├── model-routing/
│   ├── data-classification/
│   ├── license/
│   └── tool-access/
│
└── scripts/
    ├── generate_ai_bom.py
    ├── validate_ai_bom.py
    ├── check_github_actions_hardening.py
    ├── generate_release_attestation.py
    └── validate_audit_schema.py
```

### 2.2 Acceptance criteria

The repository is baseline-ready only if these files exist:

```text
docs/ai-act/risk-classification.md
docs/ai-act/provider-deployer-role-classification.md
docs/privacy/data-classification-policy.md
docs/privacy/model-privacy-policy.md
docs/privacy/audit-log-minimization-policy.md
docs/security/threat-model.md
docs/security/agent-to-agent-security.md
docs/models/model-routing-policy.md
docs/agents/agent-permission-matrix.md
docs/audit/logging-schema.md
.github/CODEOWNERS
.github/workflows/compliance-security-ai.yml
```

---

## 3. Introduce role model and CODEOWNERS

### 3.1 Responsibilities

| Role                    | Responsibility                                   | Gate                |
| ----------------------- | ------------------------------------------------ | ------------------- |
| Product Owner           | Use case, product goal, release purpose          | Requirements Gate   |
| AI Compliance Owner     | AI Act role, risk class, AI documentation        | AI Risk Gate        |
| Security Architect      | Threat model, DevSecOps, agent security          | Security Gate       |
| Data Protection Officer | GDPR, DPIA, data subject rights, TOMs            | Privacy Gate        |
| Model Privacy Owner     | Model routes, local/EU/cloud strategy            | Model Privacy Gate  |
| Agent Security Owner    | Agent-to-agent security, zero trust, tool rights | Agent Security Gate |
| License Owner           | OSS, model, dataset, and prompt licenses         | License Gate        |
| Human Reviewer          | Review of critical agent decisions               | Human Approval Gate |
| Release Manager         | Release approval, signing, artifacts             | Release Gate        |
| Audit Owner             | Audit trail, evidence, archiving                 | Audit Gate          |
| Maintainer              | Code quality, tests, technical implementation    | Quality Gate        |

### 3.2 `.github/CODEOWNERS`

```text
# Global
* @maintainers

# AI Act / Governance
/docs/ai-act/ @ai-compliance-owner
/docs/ai-governance/ @ai-compliance-owner

# Privacy / GDPR / Model Privacy
/docs/privacy/ @privacy-owner @model-privacy-owner
/docs/models/ @model-privacy-owner

# Security / Agent Security
/docs/security/ @security-architect @agent-security-owner
/docs/agents/ @agent-security-owner

# Policies
/policies/ @security-architect @ai-compliance-owner

# Licenses
/docs/licenses/ @license-owner

# BOMs
/bom/ @release-manager @security-architect @license-owner

# Workflows
/.github/workflows/ @security-architect @release-manager

# Audit
/docs/audit/ @audit-owner @security-architect

# Scripts
/scripts/ @security-architect @maintainers
```

### 3.3 Acceptance criterion

A pull request must not be mergeable if affected CODEOWNERS have not approved.

---

## 4. Build AI Act role and risk classification

### 4.1 Create file

`docs/ai-act/provider-deployer-role-classification.md`

```markdown
# Provider/Deployer/Product Manufacturer Classification

## 1. Release
- Release ID:
- Commit:
- Date:
- Owner:

## 2. Use case
- Purpose:
- Target users:
- Affected persons:
- Deployment context:
- Internal / external:
- Commercial / non-commercial:

## 3. AI Act role
| Role | Yes/No | Rationale | Evidence |
|---|---:|---|---|
| Provider |  |  |  |
| Deployer |  |  |  |
| Importer |  |  |  |
| Distributor |  |  |  |
| Product Manufacturer |  |  |  |

## 4. CRA scope
| Question | Answer |
|---|---|
| Product with digital elements? |  |
| Placed on the EU market? |  |
| Commercial activity? |  |
| Purely internal use? |  |
| Open-source / FOSS component? |  |
| Managed service / support / monetization? |  |

## 5. Result
- Preliminary scope:
- Required gates:
- Reviewers:
- Next review:
```

### 4.2 Create risk classification

`docs/ai-act/risk-classification.md`

```markdown
# AI Act Risk Classification

## 1. Use case
- Description:
- User group:
- Affected persons:
- Decision impact:

## 2. Risk class
| Class | Yes/No | Rationale |
|---|---:|---|
| Minimal Risk |  |  |
| Limited Risk |  |  |
| High Risk |  |  |
| Prohibited Practice |  |  |

## 3. Limited-risk triggers
| Trigger | Yes/No | Measure |
|---|---:|---|
| User interacts with AI |  | AI notice |
| AI-generated content |  | Labeling |
| Chatbot / conversational agent |  | Transparency notice |
| Deepfake / synthetic content |  | Labeling |

## 4. High-risk triggers
| Area | Yes/No | Rationale |
|---|---:|---|
| Employment / HR |  |  |
| Education |  |  |
| Creditworthiness / financial access |  |  |
| Critical infrastructure |  |  |
| Health / medical |  |  |
| Law enforcement / migration / justice |  |  |
| Safety component of regulated products |  |  |

## 5. Mandatory measures
- Risk management:
- Technical documentation:
- Logging:
- Human oversight:
- Accuracy / robustness / cybersecurity:
- Post-market monitoring:
- FRIA required:
```

### 4.3 Acceptance criterion

A release is not approvable if no completed role and risk classification is present.

---

## 5. Introduce AI literacy program

AI literacy obligations apply according to the European Commission timeline since 02.02.2025. ([Shaping Europe’s digital future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com "AI Act | Shaping Europe's digital future - European Union"))

### 5.1 Create file

`docs/ai-governance/ai-literacy-program.md`

```markdown
# AI Literacy Program

## 1. Objective
All relevant roles must understand the capabilities, limitations, risks, and permissible usage of the multi-agent system.

## 2. Affected roles
| Role | Training required | Content | Evidence |
|---|---:|---|---|
| Product Owner | Yes | Use case, limits, AI Act |  |
| Maintainer | Yes | Secure AI development, prompt injection |  |
| Human Reviewer | Yes | Human oversight, escalation |  |
| Security Architect | Yes | Agent security, supply chain |  |
| Data protection | Yes | Data classes, model routing, transfers |  |
| End users | depends on the use case | Transparency, limits, safe usage |  |

## 3. Minimum contents
- AI Act basics
- GDPR basics
- Prompt injection
- Data classification
- Model routing
- Human oversight
- Misbehavior and incident reporting
- System limitations

## 4. Evidence
| Person/Role | Date | Content | Version | Confirmation |
|---|---|---|---|---|
```

### 5.2 Acceptance criterion

No productive operation without documented AI literacy coverage for relevant roles.

---

## 6. Build data classification and model privacy

### 6.1 Define data classes

`docs/privacy/data-classification-policy.md`

```markdown
# Data Classification Policy

## Data classes

| Class | Description | External model API | EU-hosted | Local |
|---|---|---:|---:|---:|
| public | Publicly available information | allowed | allowed | allowed |
| internal | Internal, non-public information | review | allowed | allowed |
| confidential | Trade secrets / confidential content | blocked | review | preferred |
| personal_data_masked | Masked personal data | exception approval | review | allowed |
| personal_data_unmasked | Unmasked personal data | blocked | review | preferred |
| special_category_data | Special categories of personal data | blocked | exception | block or local |
| secrets | Tokens, keys, credentials | blocked | blocked | blocked |
| security_sensitive | Vulnerabilities, exploit context, security code | blocked | review | preferred |
| audit_logs_sensitive | sensitive audit data | blocked | review | preferred |
```

### 6.2 Create model routing policy

`docs/models/model-routing-policy.md`

```yaml
model_routing_policy:
  default: deny

  data_classes:
    - public
    - internal
    - confidential
    - personal_data_masked
    - personal_data_unmasked
    - special_category_data
    - secrets
    - credentials
    - security_sensitive
    - private_repository_content
    - audit_logs_sensitive

  routes:
    local:
      allowed_data_classes:
        - public
        - internal
        - confidential
        - personal_data_masked
        - personal_data_unmasked
        - security_sensitive
        - private_repository_content
      required_controls:
        - local_execution_boundary
        - disk_encryption
        - access_logging
        - no_unapproved_network_egress

    eu_hosted:
      allowed_data_classes:
        - public
        - internal
        - personal_data_masked
      forbidden_data_classes:
        - secrets
        - credentials
        - special_category_data
      required_controls:
        - dpa
        - eu_region
        - no_training
        - encryption_at_rest
        - encryption_in_transit
        - audit_logging
        - tenant_isolation
        - subprocessor_review
        - support_access_controls
        - retention_policy
        - no_unapproved_third_country_access

    external_cloud_api:
      allowed_data_classes:
        - public
      forbidden_data_classes:
        - personal_data_unmasked
        - special_category_data
        - secrets
        - credentials
        - confidential
        - security_sensitive
        - private_repository_content
        - audit_logs_sensitive
      required_controls:
        - dpa
        - no_training
        - explicit_model_privacy_approval
        - prompt_minimization
        - egress_logging
        - subprocessor_review
        - chapter_v_transfer_check
        - retention_policy
        - support_access_controls
```

### 6.3 Create vendor due diligence

`docs/privacy/ai-vendor-due-diligence.md`

```markdown
# AI Vendor Due Diligence

## Provider
- Name:
- Service:
- Role: Controller / Processor / Subprocessor / own controller
- Region:
- Support region:
- Subprocessors:
- Data types:
- Retention:
- Training with customer data: Yes/No
- Telemetry: Yes/No

## GDPR review
| Item | Status | Evidence |
|---|---|---|
| DPA available |  |  |
| TOMs reviewed |  |  |
| Subprocessors reviewed |  |  |
| Third-country transfer reviewed |  |  |
| SCC / DPF / adequacy decision reviewed |  |  |
| TIA required |  |  |
| Deletion regulated |  |  |
| Incident notification regulated |  |  |

## Decision
- Approved:
- Approval scope:
- Data classes:
- Approval expiry date:
- Reviewer:
```

### 6.4 Acceptance criterion

An external model, embedding, tool, observability, or security API may only be used after `ai-vendor-due-diligence.md` has been completed and approved.

---

## 7. Build privacy by design and PII gate

### 7.1 PII workflow

```text
Input
→ Data Classification
→ PII Detection
→ Masking / Pseudonymization / Blocking
→ Model Routing Policy
→ Agent Processing
→ Output Validation
→ Audit Event
```

### 7.2 Recommended building blocks

| Purpose         | Open source / Technology                |
| --------------- | --------------------------------------- |
| PII detection   | Microsoft Presidio, spaCy, scrubadub    |
| Policy decision | Open Policy Agent / Rego                |
| Secrets         | HashiCorp Vault, GitHub OIDC, Cloud KMS |
| Egress control  | Proxy, AI gateway, firewall allowlist   |
| Audit           | immudb, OpenSearch, SIEM, WORM storage  |

### 7.3 Create audit minimization

`docs/privacy/audit-log-minimization-policy.md`

```markdown
# Audit Log Minimization Policy

## Principle
Auditability is primarily established via hashes, IDs, policy decisions, data classes, timestamps, signatures, and approval events.

## Default rules
| Content | Default | Exception |
|---|---|---|
| Prompt | Hash + prompt version | Raw prompt only with purpose, legal basis, retention |
| Output | Output hash + classification | Raw output only for review purpose or incident |
| PII | Redacted / tokenized | Plaintext only with compelling purpose |
| Secrets | never store | no exception |
| Tool parameters | Parameter hash | Raw parameters only for non-sensitive data |
| Policy decision | store in full | mandatory field |
| Human approval | store in full | mandatory field |
| Model route | store in full | mandatory field |
```

### 7.4 Acceptance criterion

Audit logs must not contain secrets. PII, raw prompts, and raw outputs may only be stored with documented purpose, legal basis, retention, and access protection.

---

## 8. Build agent-to-agent zero trust

### 8.1 Agent inventory

`docs/agents/agent-inventory.md`

```markdown
# Agent Inventory

| Agent ID | Role | Version | Owner | Data classes | Tools | Model route | Human approval required |
|---|---|---|---|---|---|---|---|
| research-agent | evidence_collection | 1.0.0 |  | public, internal | web_search, repo_read | eu_hosted/local | No |
| code-agent | code_generation | 1.0.0 |  | internal | repo_read, repo_write | local/eu_hosted | Yes |
| compliance-agent | policy_review | 1.0.0 |  | internal | repo_read, policy_eval | local/eu_hosted | Yes |
```

### 8.2 Agent card template

`docs/agents/agent-cards/agent-card-template.md`

```markdown
# Agent Card

## Identity
- Agent ID:
- Version:
- Owner:
- Role:
- Purpose:

## Permissions
- Allowed tools:
- Forbidden tools:
- Allowed data classes:
- Forbidden data classes:
- Allowed model routes:

## Security rules
- Must sign messages: Yes
- Must include policy version: Yes
- Must include capability scope: Yes
- May write memory: Yes/No
- May execute code: Yes/No
- Sandbox required: Yes/No

## Human oversight
- HITL required for:
- HOTL monitoring:
- Escalation rule:

## Audit
- Required fields:
- Retention:
```

### 8.3 Agent communication policy

`docs/agents/agent-communication-policy.md`

```yaml
agent_communication_policy:
  default_trust: deny
  authentication_required: true
  message_signing_required: true
  policy_version_required: true
  instruction_data_separation_required: true
  tool_result_signing_required: true

  allowed_message_types:
    - task_request
    - evidence_response
    - review_request
    - policy_decision
    - human_approval_request
    - signed_tool_result
    - sandbox_execution_result

  forbidden_message_types:
    - raw_secret_transfer
    - unmasked_pii_transfer
    - privilege_delegation_without_approval
    - external_api_forward_without_policy_check
    - unsigned_tool_result
    - executable_payload_without_sandbox
    - tool_metadata_instruction_payload

  require_policy_check_for:
    - external_api_call
    - code_generation
    - dependency_addition
    - deployment_action
    - personal_data_processing
    - model_route_change
    - memory_write
    - tool_registry_change
    - rag_context_ingestion
    - mcp_tool_registration
    - code_execution
    - audit_log_export

  require_human_approval_for:
    - high_risk_ai_decision
    - production_deployment
    - sensitive_data_export
    - license_exception
    - external_cloud_model_exception
    - security_policy_change
    - irreversible_tool_action
    - privilege_escalation
    - sandbox_escape_exception
```

### 8.4 Agent security controls

| Risk                       | Control                                                                    |
| -------------------------- | -------------------------------------------------------------------------- |
| Agent goal hijack          | Goal binding per agent, task-scoped capability tokens, goal validation     |
| Tool misuse                | Tool allowlist, schema validation, human approval for irreversible actions |
| Identity & privilege abuse | mTLS/SPIFFE, signed agent claims, scoped credentials                       |
| Prompt injection           | Instruction/data separation, context firewall, retrieval trust scoring     |
| RAG injection              | Always treat RAG documents as data, never as instructions                  |
| Tool poisoning             | Signed tool manifests, tool registry review                                |
| Memory poisoning           | Separate memory stores, write approval, memory audit                       |
| Insecure output handling   | Output schema validation, no direct shell/API/SQL execution                |
| Unsandboxed execution      | Ephemeral sandbox, no-network default, resource limits                     |
| MCP server compromise      | Server identity, tool manifest signing, capability scope                   |

### 8.5 Acceptance criterion

No agent may use a message, tool result, or memory entry from another agent without authentication, signature, policy version, data class, and capability scope.

---

## 9. Build OPA/Rego policies

### 9.1 Model routing policy

`policies/rego/model_routing.rego`

```rego
package model.routing

default allow = false

sensitive_classes := {
  "personal_data_unmasked",
  "special_category_data",
  "secrets",
  "credentials",
  "confidential",
  "security_sensitive",
  "private_repository_content",
  "audit_logs_sensitive"
}

allow {
  input.route == "local"
  input.controls.local_execution_boundary == true
  input.controls.no_unapproved_network_egress == true
}

allow {
  input.route == "eu_hosted"
  input.controls.dpa == true
  input.controls.eu_region == true
  input.controls.no_training == true
  input.controls.subprocessor_review == true
  input.controls.support_access_controls == true
  input.controls.retention_policy == true
  input.controls.no_unapproved_third_country_access == true
  not sensitive_classes[input.data_class]
}

allow {
  input.route == "external_cloud_api"
  input.controls.dpa == true
  input.controls.no_training == true
  input.controls.explicit_model_privacy_approval == true
  input.controls.prompt_minimization == true
  input.controls.chapter_v_transfer_check == true
  input.controls.subprocessor_review == true
  input.controls.retention_policy == true
  input.data_class == "public"
}

deny_reason[msg] {
  input.route == "external_cloud_api"
  sensitive_classes[input.data_class]
  msg := sprintf("External cloud route blocked for data class: %s", [input.data_class])
}
```

### 9.2 Agent communication policy

`policies/rego/agent_communication.rego`

```rego
package agent.communication

default allow = false

forbidden_types := {
  "raw_secret_transfer",
  "unmasked_pii_transfer",
  "privilege_delegation_without_approval",
  "external_api_forward_without_policy_check",
  "unsigned_tool_result",
  "executable_payload_without_sandbox",
  "tool_metadata_instruction_payload"
}

allow {
  input.sender.authenticated == true
  input.receiver.authenticated == true
  input.message.signed == true
  input.message.policy_version == input.required_policy_version
  input.sender.policy_version == input.required_policy_version
  not forbidden_types[input.message.type]
  input.capability in input.sender.allowed_capabilities
  input.message.instruction_data_separation == true
}

deny_reason[msg] {
  input.message.signed == false
  msg := "Unsigned agent message blocked"
}

deny_reason[msg] {
  input.message.contains_unmasked_pii == true
  msg := "Unmasked PII transfer between agents blocked"
}

deny_reason[msg] {
  input.message.requires_sandbox == true
  input.execution.sandboxed != true
  msg := "Executable payload blocked because sandbox execution is missing"
}
```

### 9.3 Acceptance criterion

CI must fail if `opa test policies/` fails or a deny result exists for model routing or agent communication.

---

## 10. Build DevSecOps pipeline

### 10.1 Required gates

| Gate                          | Blocks on                                                        |
| ----------------------------- | ---------------------------------------------------------------- |
| Quality Gate                  | Ruff/mypy/pytest errors                                          |
| SAST Gate                     | High/Critical finding                                            |
| Secret Gate                   | found secret                                                     |
| Dependency Gate               | Critical CVE or disallowed dependency                            |
| License Gate                  | prohibited or unknown license                                    |
| Model License Gate            | unclear model/dataset license                                    |
| Privacy Gate                  | unmasked PII in disallowed context                               |
| Transfer Gate                 | external vendor without DPA, subprocessor review, transfer check |
| Model Privacy Gate            | external model route without approval                            |
| Agent-to-Agent Gate           | missing authentication, signature, policy version                |
| Execution Gate                | code/tool execution without sandbox                              |
| Tool Registry Gate            | unsigned tools or unreviewed tool manifests                      |
| AI-BOM Gate                   | missing models, prompts, agents, tools, or datasets              |
| SBOM Gate                     | missing or outdated SBOM                                         |
| Audit Privacy Gate            | audit logs with PII/secrets/raw prompts without legal basis      |
| Release Integrity Gate        | missing signature, provenance, or attestation                    |
| GitHub Actions Hardening Gate | unpinned actions or overly broad permissions                     |

### 10.2 Create workflow

`.github/workflows/compliance-security-ai.yml`

```yaml
name: compliance-security-ai

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  quality:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - uses: actions/setup-python@v5 # production: pin to full commit SHA
        with:
          python-version: "3.12"
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt ruff mypy pytest coverage
      - run: ruff check .
      - run: mypy .
      - run: pytest --cov=.

  codeql:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - uses: github/codeql-action/init@v3 # production: pin to full commit SHA
        with:
          languages: python
      - uses: github/codeql-action/analyze@v3 # production: pin to full commit SHA

  sast:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - run: pip install bandit semgrep
      - run: bandit -r . -ll
      - run: semgrep scan --config auto --sarif --output semgrep.sarif
      - uses: github/codeql-action/upload-sarif@v3 # production: pin to full commit SHA
        with:
          sarif_file: semgrep.sarif

  dependency_review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - uses: actions/dependency-review-action@v4 # production: pin to full commit SHA
        with:
          fail-on-severity: critical
          comment-summary-in-pr: always

  secrets:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - uses: gitleaks/gitleaks-action@v2 # production: pin to full commit SHA

  sbom:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - name: Install syft
        run: |
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
      - name: Generate SBOM
        run: |
          mkdir -p bom/sbom
          syft . -o cyclonedx-json > bom/sbom/sbom.json
      - name: Verify SBOM
        run: test -s bom/sbom/sbom.json

  ai_bom:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - name: Generate AI-BOM
        run: python scripts/generate_ai_bom.py
      - name: Validate AI-BOM
        run: python scripts/validate_ai_bom.py bom/ai-bom/ai-bom.json

  policy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - name: Install OPA
        run: |
          curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static
          chmod +x opa
          sudo mv opa /usr/local/bin/opa
      - name: OPA Policy Checks
        run: |
          opa test policies/
          opa eval --fail-defined -i policy-input.json -d policies/ "data.compliance.deny"

  actions_hardening:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - name: Check GitHub Actions hardening
        run: python scripts/check_github_actions_hardening.py

  audit_docs:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - run: test -f docs/ai-act/risk-classification.md
      - run: test -f docs/ai-act/provider-deployer-role-classification.md
      - run: test -f docs/privacy/data-flow-map.md
      - run: test -f docs/privacy/model-privacy-policy.md
      - run: test -f docs/privacy/audit-log-minimization-policy.md
      - run: test -f docs/security/threat-model.md
      - run: test -f docs/security/agent-to-agent-security.md
      - run: test -f docs/audit/logging-schema.md
```

### 10.3 Production requirement

The YAML file shows tags for readability. For production use, third-party actions must be pinned to full commit SHAs because GitHub describes full commit SHAs as the only immutable pinning variant. ([GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com "Secure use reference - GitHub Docs"))

---

## 11. Build SBOM and AI/ML-BOM

### 11.1 SBOM

Mandatory per release:

```text
bom/sbom/sbom.json
```

Format:

```text
CycloneDX JSON
```

Contents:

* Python dependencies
* Container dependencies
* Build tools
* Runtime dependencies
* Licenses
* Package hashes
* Known vulnerability links, as far as tooling is available

### 11.2 AI-BOM schema

`bom/ai-bom/ai-bom.json`

```json
{
  "release_id": "v1.0.0",
  "commit": "COMMIT_SHA",
  "generated_at": "2026-05-01T00:00:00Z",
  "legal_scope": {
    "role": "REVIEW_REQUIRED",
    "use_case": "REVIEW_REQUIRED",
    "deployment_context": "REVIEW_REQUIRED",
    "cra_scope": "REVIEW_REQUIRED",
    "foss_scope": "REVIEW_REQUIRED",
    "reviewed_at": "2026-05-01"
  },
  "models": [
    {
      "id": "local-llm-001",
      "name": "example-local-model",
      "version": "x.y.z",
      "runtime": "ollama",
      "route": "local",
      "license": "REVIEW_REQUIRED",
      "hash": "sha256:...",
      "hosting_location": "local"
    }
  ],
  "agents": [
    {
      "id": "research-agent",
      "version": "1.0.0",
      "role": "evidence_collection",
      "allowed_tools": ["web_search", "repo_read"],
      "policy_version": "2026-05-01",
      "prompt_hash": "sha256:..."
    }
  ],
  "prompts": [
    {
      "id": "system-research-agent",
      "version": "1.0.0",
      "hash": "sha256:...",
      "classification": "internal",
      "owner": "REVIEW_REQUIRED"
    }
  ],
  "datasets": [],
  "model_routes": [
    {
      "agent_id": "research-agent",
      "data_class": "public",
      "route": "eu_hosted",
      "policy_decision": "allow"
    }
  ],
  "vendors": [
    {
      "id": "model-provider-001",
      "name": "REVIEW_REQUIRED",
      "service": "model_api",
      "region": "REVIEW_REQUIRED",
      "dpa": "REVIEW_REQUIRED",
      "subprocessor_review": "REVIEW_REQUIRED",
      "transfer_basis": "REVIEW_REQUIRED",
      "retention": "REVIEW_REQUIRED",
      "training_use": "REVIEW_REQUIRED"
    }
  ],
  "runtime_controls": {
    "sandbox_required": true,
    "network_egress_default": "deny",
    "tool_registry_signed": true,
    "actions_pinned_to_sha": true
  },
  "evaluations": [
    {
      "id": "eval-release-v1",
      "scope": "safety-security-regression",
      "status": "REVIEW_REQUIRED",
      "evidence_ref": "docs/risk/eval-and-red-team-plan.md"
    }
  ],
  "audit": {
    "sbom_id": "sbom-v1.0.0",
    "signature": "cosign-signature-ref",
    "generated_at": "2026-05-01T00:00:00Z"
  }
}
```

### 11.3 Acceptance criterion

A release must not be created if SBOM or AI-BOM is missing, empty, or cannot be validated.

---

## 12. Build release integrity and attestation

### 12.1 Release artifacts

Each release contains:

```text
bom/sbom/sbom.json
bom/ai-bom/ai-bom.json
docs/ai-act/risk-classification.md
docs/ai-act/provider-deployer-role-classification.md
docs/privacy/model-privacy-policy.md
docs/privacy/ai-vendor-due-diligence.md
docs/security/threat-model.md
docs/security/agent-to-agent-security.md
docs/audit/logging-schema.md
release-attestation.json
security-report.json
license-report.json
```

### 12.2 Attestation workflow

`.github/workflows/release-attestation.yml`

```yaml
name: release-attestation

on:
  release:
    types: [published]

permissions:
  contents: read
  id-token: write
  attestations: write

jobs:
  attest_release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4 # production: pin to full commit SHA
      - name: Generate release attestation
        run: python scripts/generate_release_attestation.py
      - name: Verify release attestation exists
        run: test -s release-attestation.json
```

GitHub describes Artifact Attestations as cryptographically signed claims that make build provenance and integrity verifiable. ([GitHub Docs](https://docs.github.com/en/actions/concepts/security/artifact-attestations?utm_source=chatgpt.com "Artifact attestations - GitHub Docs"))

### 12.3 Acceptance criterion

A release without signed attestation is not approvable.

---

## 13. Build audit logging

### 13.1 Mandatory events

`docs/audit/logging-schema.md`

```markdown
# Logging Schema

| Event | Mandatory fields |
|---|---|
| Agent start | Agent ID, version, role, policy version |
| Agent-to-agent message | Sender, receiver, message hash, signature, auth status |
| User input | Input category, purpose, PII status |
| PII detection | detected entities, masking status, policy decision |
| Model routing | Model route, data class, jurisdiction, decision |
| Tool call | Tool ID, parameter hash, result hash |
| Policy decision | Policy ID, version, result, rationale |
| Guardrail violation | Rule, severity, block/allow decision |
| Human approval | Reviewer, timestamp, decision, scope |
| Code change | Commit ID, PR ID, author, agent ID |
| Release | SBOM ID, AI-BOM ID, signature, artifact hash |
| Output | Output hash, prompt version, model version |
| Legal role assessment | Use case, role, scope, release ID, reviewer, result |
| FRIA trigger | Trigger, risk class, affected group, decision |
| Vendor transfer check | Vendor, jurisdiction, subprocessors, transfer basis |
| Sandbox execution | Sandbox ID, tool ID, input hash, output hash, network policy |
| Tool registry change | Tool ID, manifest hash, signature, permissions, reviewer |
| RAG context ingestion | Document ID, source, trust score, data class, hash |
| Audit redaction | Field, redaction type, policy ID, result |
| Post-market monitoring signal | Signal ID, model/agent, severity, measure |
```

### 13.2 Audit pipeline

```text
Agent Event
→ Event Normalization
→ JSON Schema Validation
→ Redaction / Tokenization
→ Hash Chain
→ Digital Signature
→ Trusted Timestamp
→ Append-only Storage
→ WORM Archive
→ SIEM Export
→ Audit Report
```

### 13.3 Acceptance criterion

Audit logs must be tamper-resistant, data-minimizing, access-restricted, and exportable.

---

## 14. Build CRA vulnerability handling

### 14.1 Create file

`docs/security/cra-vulnerability-reporting.md`

```markdown
# CRA Vulnerability Reporting

## 1. Scope
This procedure applies to products with digital elements insofar as CRA scope is confirmed.

## 2. Reportable events
- actively exploited vulnerability
- serious security incident affecting the security of the product

## 3. Deadlines
- Early warning: within 24 hours
- Main report: within 72 hours
- Final report: after analysis / remediation

## 4. Mandatory fields
| Field | Description |
|---|---|
| Product / Release | affected version |
| Vulnerability | type, component, CVE if available |
| Exploitation | known / suspected / confirmed |
| Impact | affected users, systems, data |
| Measures | mitigation, patch, workaround |
| Timeline | discovery, assessment, reporting, remediation |
| Responsible parties | incident owner, security owner, release manager |

## 5. Evidence
- Logs
- SBOM
- AI-BOM, if AI component affected
- Commit IDs
- Patches
- Communication
```

The European Commission states that CRA reporting obligations for actively exploited vulnerabilities and serious security incidents apply from 11.09.2026. ([Shaping Europe’s digital future](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting?utm_source=chatgpt.com "Cyber Resilience Act - Reporting obligations"))

### 14.2 Acceptance criterion

For CRA-relevant releases, a 24h/72h reporting process must be documented, tested, and assigned to an incident owner.

---

## 15. Build human oversight

### 15.1 Human oversight matrix

`docs/ai-act/human-oversight-matrix.md`

```markdown
# Human Oversight Matrix

| Action | Risk | Mode | Approval required |
|---|---|---|---|
| Information research | low | Human-on-the-loop | No |
| Code generation | medium | Human-in-the-loop | Yes for merge |
| Add dependency | medium/high | Human-in-the-loop | Yes |
| Enable external model route | high | Human-in-the-loop | Yes |
| Deploy to production | high | Human-in-the-loop | Yes |
| Export sensitive data | high | Human-in-the-loop | Yes |
| High-risk AI decision | high/critical | Human-in-the-loop | Yes |
| Change security policy | high | Human-in-the-loop | Yes |
| Irreversible tool action | high | Human-in-the-loop | Yes |
```

### 15.2 Acceptance criterion

Critical actions must not be triggered solely by agents.

---

## 16. Build post-market monitoring and eval regression

### 16.1 Monitoring file

`docs/ai-act/post-market-monitoring-plan.md`

```markdown
# Post-Market Monitoring Plan

## 1. Components monitored
- Models
- Agents
- Prompts
- Tools
- Policies
- Model routes
- Data sources
- RAG contexts

## 2. Signals
| Signal | Source | Reaction |
|---|---|---|
| Misclassification | Eval suite | Review |
| Policy bypass | OPA logs | Incident |
| Prompt injection attempt | Guardrail logs | Block + review |
| Tool misuse | Tool audit | Incident |
| Drift | Eval regression | Re-evaluation |
| Sensitive data exposure | DLP / audit | Incident |
| User complaint | Support / ticket | Review |
| Security finding | SAST/DAST/SIEM | Incident |

## 3. Frequency
- Release: full regression
- Monthly: policy review
- Quarterly: model privacy review
- Event-based: incident / major model change / new tool
```

### 16.2 Acceptance criterion

No productive release without defined eval regression and monitoring signals.

---

## 17. Prioritized implementation

### Phase 1 — Governance baseline

**Goal:** control regulatory and organizational scope.

Implement:

1. Create repository structure.
2. Enable CODEOWNERS.
3. Document provider/deployer/product manufacturer/FOSS scope.
4. Document AI Act risk class per use case.
5. Document AI literacy program.
6. Create agent inventory.
7. Create model inventory.
8. Create tool registry.
9. Create risk register.

Output:

```text
docs/ai-act/provider-deployer-role-classification.md
docs/ai-act/risk-classification.md
docs/ai-governance/ai-literacy-program.md
docs/agents/agent-inventory.md
docs/models/model-inventory.md
.github/CODEOWNERS
```

Definition of done:

```text
All mandatory files exist.
All owners are named.
Each use case has role, scope, and risk class.
```

---

### Phase 2 — Data protection and model privacy

**Goal:** no uncontrolled data transfer to models, tools, or agents.

Implement:

1. Define data classes.
2. Create model routing policy.
3. Set external model APIs to default-deny.
4. Define PII detection and masking.
5. Introduce vendor due diligence.
6. Introduce transfer checks.
7. Create audit log minimization policy.
8. Create DPIA draft.

Output:

```text
docs/privacy/data-classification-policy.md
docs/models/model-routing-policy.md
docs/privacy/ai-vendor-due-diligence.md
docs/privacy/international-transfer-assessment.md
docs/privacy/audit-log-minimization-policy.md
docs/privacy/dpia-draft.md
```

Definition of done:

```text
No external model route without policy decision.
No personal data without a data class.
No vendor approval without DPA/subprocessor/transfer review.
```

---

### Phase 3 — DevSecOps and supply chain

**Goal:** block pull requests with unsafe changes.

Implement:

1. Integrate Ruff, mypy, pytest.
2. Integrate CodeQL.
3. Integrate Semgrep and Bandit.
4. Enable dependency review.
5. Enable Gitleaks.
6. Integrate license checks.
7. Automate SBOM.
8. Check GitHub Actions hardening.
9. Enable SARIF upload.
10. Enable required checks.

Output:

```text
.github/workflows/compliance-security-ai.yml
scripts/check_github_actions_hardening.py
bom/sbom/sbom.json
security-report.json
license-report.json
```

Definition of done:

```text
PRs with critical CVE, secrets, high/critical SAST finding, or unknown license are blocked.
```

---

### Phase 4 — Agent-to-agent security

**Goal:** zero trust between agents.

Implement:

1. Create agent cards.
2. Create agent permission matrix.
3. Introduce agent communication policy.
4. Enforce signed agent messages.
5. Introduce capability tokens.
6. Introduce tool allowlist.
7. Introduce memory write controls.
8. Enforce instruction/data separation.
9. Introduce sandbox for code/tool execution.
10. Introduce tool/MCP manifest signing.

Output:

```text
docs/agents/agent-cards/
docs/agents/agent-permission-matrix.md
docs/agents/agent-communication-policy.md
docs/security/sandboxed-execution-policy.md
docs/security/tool-registry-security.md
policies/rego/agent_communication.rego
```

Definition of done:

```text
No agent accepts unsigned messages, unsigned tool results, or third-party data without a policy check.
```

---

### Phase 5 — AI-BOM and release governance

**Goal:** each release is auditable, reproducible, and signed.

Implement:

1. Finalize AI-BOM schema.
2. Build AI-BOM generator.
3. Build AI-BOM validator.
4. Enforce model cards.
5. Enforce agent cards.
6. Generate release attestation.
7. Integrate cosign/Sigstore or GitHub Artifact Attestations.
8. Generate release bundle.
9. Enforce human approval for critical releases.

Output:

```text
bom/ai-bom/ai-bom.json
bom/ml-bom/
release-attestation.json
docs/models/model-cards/
docs/agents/agent-cards/
```

Definition of done:

```text
No release without SBOM, AI-BOM, risk classification, signature, and attestation.
```

---

### Phase 6 — Audit, monitoring, and operations

**Goal:** audit-grade traceability without unnecessary raw data logging.

Implement:

1. Introduce logging schema.
2. Enforce audit minimization.
3. Introduce hash chains.
4. Introduce signed audit events.
5. Connect append-only storage.
6. Connect WORM archive.
7. Introduce SIEM export.
8. Introduce post-market monitoring.
9. Introduce CRA vulnerability reporting.
10. Introduce serious incident response for AI incidents.

Output:

```text
docs/audit/logging-schema.md
docs/audit/audit-policy.md
docs/ai-act/post-market-monitoring-plan.md
docs/ai-act/serious-incident-response-ai.md
docs/security/cra-vulnerability-reporting.md
audit-export.jsonl
```

Definition of done:

```text
Every critical agent, model, tool, policy, and release decision is traceable via hashes, signatures, IDs, and policy decisions.
```

---

## 18. Do not accept

These states block merge or release:

```text
unmasked PII in external model calls
special categories of personal data in external model calls
unreviewed third-country/support/subprocessor access
unsigned agent-to-agent communication
agent-to-agent communication without policy version
agents with blanket tool permissions
RAG contexts treated as instructions
tool/MCP manifests without signature and review
code or tool execution without sandbox for risky actions
new dependencies without CVE and license review
releases without SBOM
releases without AI-BOM
releases without signature, provenance, or attestation
prompts or system prompts without version, hash, owner, and classification
cloud model usage without DPA, no-training commitment, retention rules, subprocessor review, and jurisdiction checks
audit logs with PII, secrets, or raw prompts without documented legal basis, purpose limitation, retention, and access protection
```

---

## 19. Final acceptance checklist

| Area                                                       | Mandatory met |
| ---------------------------------------------------------- | ------------: |
| AI Act role documented per use case                        |            ☐ |
| AI Act risk class documented                               |            ☐ |
| AI literacy program documented                             |            ☐ |
| GDPR data classes defined                                  |            ☐ |
| DPIA draft present                                         |            ☐ |
| Model routing policy active                                |            ☐ |
| External model APIs default-deny                           |            ☐ |
| Vendor due diligence present                               |            ☐ |
| Transfer review present                                    |            ☐ |
| CODEOWNERS active                                          |            ☐ |
| Required checks active                                     |            ☐ |
| CodeQL active                                              |            ☐ |
| Semgrep/Bandit active                                      |            ☐ |
| Dependency review active                                   |            ☐ |
| Secret scanning active                                     |            ☐ |
| License review active                                      |            ☐ |
| GitHub Actions SHA pinning planned/implemented             |            ☐ |
| SBOM present per release                                   |            ☐ |
| AI-BOM present per release                                 |            ☐ |
| Agent cards present                                        |            ☐ |
| Model cards present                                        |            ☐ |
| Agent-to-agent signatures active                           |            ☐ |
| Capability tokens active                                   |            ☐ |
| Sandbox policy active                                      |            ☐ |
| Tool registry signed                                       |            ☐ |
| Audit logging schema present                               |            ☐ |
| Audit minimization documented                              |            ☐ |
| Release attestation present                                |            ☐ |
| Post-market monitoring present                             |            ☐ |
| CRA vulnerability reporting present if CRA scope confirmed |            ☐ |
| Serious incident response present                          |            ☐ |

---

## 20. Target state

The repository is release-ready only if the following statement is provable:

> Every agent, every model, every tool, every prompt, every policy, every dependency, and every release is classified, versioned, authorized, tested, auditable, and reproducible. External model and tool routes are default-deny. Critical actions require human approval. Releases without SBOM, AI-BOM, signature, provenance, and risk classification are blocked.
>
