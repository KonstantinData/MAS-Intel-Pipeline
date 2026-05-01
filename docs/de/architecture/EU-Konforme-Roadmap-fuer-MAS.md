# EU-konforme Roadmap für ein Multi-Agent-System auf GitHub

## Bauanleitung mit validierten Umsetzungsinformationen

**Stand:** 01.05.2026
**Scope:** Python-basiertes Multi-Agent-System auf GitHub
**Einordnung:** technische und organisatorische Umsetzungsempfehlung, keine Rechtsberatung

---

## 0. Verbindliche Planungsgrundlage

### 0.1 Regulatorischer Quellenstand

Diese Roadmap verwendet folgende validierte Grundlagen:

| Bereich                                  | Validierter Stand                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EU AI Act                                | In Kraft seit 01.08.2024. Verbote und AI-Literacy-Pflichten gelten seit 02.02.2025. GPAI-Regeln gelten seit 02.08.2025. Allgemeine Anwendung ab 02.08.2026. High-Risk-Systeme in regulierten Produkten mit Übergangsfrist bis 02.08.2027. Quelle: Europäische Kommission, AI Act Timeline. ([Digitale Zukunft Europas](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com "AI Act                                                                                                                                                         |
| Digital Omnibus / High-Risk-Verschiebung | Der Rat der EU hat am 13.03.2026 eine Position vorgeschlagen, nach der High-Risk-Regeln auf 02.12.2027 für stand-alone High-Risk-Systeme und 02.08.2028 für High-Risk-Systeme in Produkten verschoben würden. Das ist als Szenario zu verfolgen, nicht als alleinige operative Grundlage. Quelle: Rat der EU, 13.03.2026. ([Rat der Europäischen Union](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/?utm_source=chatgpt.com "Council agrees position to streamline rules on Artificial ...")) |
| DSGVO                                    | Art. 5 enthält u. a. Rechtmäßigkeit, Zweckbindung, Datenminimierung, Speicherbegrenzung, Integrität/Vertraulichkeit und Rechenschaftspflicht. Art. 25 verlangt Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen. Quelle: EUR-Lex, Regulation (EU) 2016/679. ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng?utm_source=chatgpt.com "Regulation - 2016/679 - EN - gdpr - EUR-Lex - European Union"))                                                                                                                                             |
| CRA                                      | Regulation (EU) 2024/2847. Vollanwendung ab 11.12.2027. Meldepflichten für aktiv ausgenutzte Schwachstellen und schwere Sicherheitsvorfälle ab 11.09.2026. Quelle: Europäische Kommission und EUR-Lex. ([Digitale Zukunft Europas](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting?utm_source=chatgpt.com "Cyber Resilience Act - Reporting obligations"))                                                                                                                                                                                                                   |
| GitHub Actions Security                  | GitHub empfiehlt vollständige Commit-SHA-Pinning, weil nur diese Variante ein Action-Release unveränderlich referenziert. Quelle: GitHub Docs. ([GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com "Secure use reference - GitHub Docs"))                                                                                                                                                                                                                                                                                                  |
| GitHub Artifact Attestations             | GitHub Artifact Attestations erzeugen kryptografisch signierte Provenance- und Integritätsnachweise für Build-Artefakte. Quelle: GitHub Docs. ([GitHub Docs](https://docs.github.com/en/actions/concepts/security/artifact-attestations?utm_source=chatgpt.com "Artifact attestations - GitHub Docs"))                                                                                                                                                                                                                                                                                        |
| Agentic AI Security                      | OWASP Top 10 for Agentic Applications 2026 benennt u. a. Agent Goal Hijack, Tool Misuse und Identity & Privilege Abuse als zentrale Risiken. Quelle: OWASP, 09.12.2025. ([OWASP Gen AI Security Project](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/?utm_source=chatgpt.com "OWASP Top 10 for Agentic Applications for 2026"))                                                                                                                                                                                                                             |
| AI-/ML-BOM                               | CycloneDX beschreibt AI-/ML-BOMs als Transparenzinstrument für Modelle, Datasets, Dependencies, Provenance, Trainingsmethoden und Konfigurationen. Quelle: CycloneDX. ([cyclonedx.org](https://cyclonedx.org/capabilities/mlbom/?utm_source=chatgpt.com "Machine Learning Bill of Materials (AI/ML-BOM)"))                                                                                                                                                                                                                                                                                     |
| AI Management System                     | ISO/IEC 42001:2023 ist ein Managementsystem-Standard für Aufbau, Betrieb, Pflege und kontinuierliche Verbesserung eines AI Management Systems. Quelle: ISO. ([ISO](https://www.iso.org/standard/42001?utm_source=chatgpt.com "ISO/IEC 42001:2023 - AI management systems"))                                                                                                                                                                                                                                                                                                                    |
| Generative-AI-Risikomanagement           | NIST AI 600-1 ist ein Generative-AI-Profil zum NIST AI RMF 1.0 und dient der freiwilligen Risikosteuerung generativer KI-Systeme. Quelle: NIST, 2024. ([NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence?utm_source=chatgpt.com "Artificial Intelligence Risk Management Framework"))                                                                                                                                                                                                                               |

---

## 1. Zielarchitektur

Das Repository wird als **kontrollierter Compliance-, Security-, Privacy-, Model- und Agent-Lifecycle** geführt.

Nicht das Repository selbst ist automatisch das regulierte Produkt. Bewertet werden je Release:

1. Use Case
2. Deployment-Kontext
3. Rolle nach AI Act
4. Rolle nach CRA
5. Datenklassen
6. Modellrouten
7. Agentenrechte
8. Toolrechte
9. Auditierbarkeit
10. Release-Artefakte

---

## 2. Repository-Struktur anlegen

### 2.1 Zielstruktur

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

### 2.2 Abnahmekriterium

Das Repository ist erst baseline-fähig, wenn diese Dateien existieren:

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

## 3. Rollenmodell und CODEOWNERS einführen

### 3.1 Verantwortlichkeiten

| Rolle                    | Verantwortung                                   | Gate                |
| ------------------------ | ----------------------------------------------- | ------------------- |
| Product Owner            | Use Case, Produktziel, Release-Zweck            | Requirements Gate   |
| AI Compliance Owner      | AI-Act-Rolle, Risikoklasse, AI-Dokumentation    | AI Risk Gate        |
| Security Architect       | Threat Model, DevSecOps, Agent Security         | Security Gate       |
| Datenschutzbeauftragte/r | DSGVO, DPIA, Betroffenenrechte, TOMs            | Privacy Gate        |
| Model Privacy Owner      | Modellrouten, lokale/EU/Cloud-Strategie         | Model Privacy Gate  |
| Agent Security Owner     | Agent-to-Agent Security, Zero Trust, Toolrechte | Agent Security Gate |
| License Owner            | OSS-, Modell-, Dataset- und Prompt-Lizenzen     | License Gate        |
| Human Reviewer           | Prüfung kritischer Agentenentscheidungen       | Human Approval Gate |
| Release Manager          | Release-Freigabe, Signierung, Artefakte         | Release Gate        |
| Audit Owner              | Audit Trail, Evidenz, Archivierung              | Audit Gate          |
| Maintainer               | Codequalität, Tests, technische Umsetzung      | Quality Gate        |

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

### 3.3 Abnahmekriterium

Ein Pull Request darf nicht mergebar sein, wenn betroffene CODEOWNER nicht genehmigt haben.

---

## 4. AI-Act-Rollen- und Risikoklassifizierung bauen

### 4.1 Datei anlegen

`docs/ai-act/provider-deployer-role-classification.md`

```markdown
# Provider-/Deployer-/Product-Manufacturer-Klassifizierung

## 1. Release
- Release-ID:
- Commit:
- Datum:
- Owner:

## 2. Use Case
- Zweck:
- Zielnutzer:
- Betroffene Personen:
- Deployment-Kontext:
- Intern / extern:
- Kommerziell / nicht kommerziell:

## 3. AI-Act-Rolle
| Rolle | Ja/Nein | Begründung | Evidenz |
|---|---:|---|---|
| Provider |  |  |  |
| Deployer |  |  |  |
| Importeur |  |  |  |
| Distributor |  |  |  |
| Product Manufacturer |  |  |  |

## 4. CRA-Scope
| Frage | Antwort |
|---|---|
| Produkt mit digitalen Elementen? |  |
| Bereitstellung am EU-Markt? |  |
| Kommerzielle Tätigkeit? |  |
| Reine interne Nutzung? |  |
| Open-Source-/FOSS-Komponente? |  |
| Managed Service / Support / Monetarisierung? |  |

## 5. Ergebnis
- Vorläufiger Scope:
- Pflicht-Gates:
- Reviewer:
- Nächste Prüfung:
```

### 4.2 Risikoklassifizierung anlegen

`docs/ai-act/risk-classification.md`

```markdown
# AI-Act-Risikoklassifizierung

## 1. Use Case
- Beschreibung:
- Nutzergruppe:
- Betroffene Personen:
- Entscheidungsauswirkung:

## 2. Risikoklasse
| Klasse | Ja/Nein | Begründung |
|---|---:|---|
| Minimal Risk |  |  |
| Limited Risk |  |  |
| High Risk |  |  |
| Prohibited Practice |  |  |

## 3. Limited-Risk-Trigger
| Trigger | Ja/Nein | Maßnahme |
|---|---:|---|
| Nutzer interagiert mit KI |  | KI-Hinweis |
| KI-generierter Inhalt |  | Kennzeichnung |
| Chatbot / Conversational Agent |  | Transparenzhinweis |
| Deepfake / synthetischer Inhalt |  | Kennzeichnung |

## 4. High-Risk-Trigger
| Bereich | Ja/Nein | Begründung |
|---|---:|---|
| Beschäftigung / HR |  |  |
| Bildung |  |  |
| Kreditwürdigkeit / Finanzzugang |  |  |
| Kritische Infrastruktur |  |  |
| Gesundheit / Medizin |  |  |
| Strafverfolgung / Migration / Justiz |  |  |
| Sicherheitskomponente regulierter Produkte |  |  |

## 5. Pflichtmaßnahmen
- Risk Management:
- Technical Documentation:
- Logging:
- Human Oversight:
- Accuracy / Robustness / Cybersecurity:
- Post-Market Monitoring:
- FRIA erforderlich:
```

### 4.3 Abnahmekriterium

Ein Release ist nicht freigabefähig, wenn keine ausgefüllte Rollen- und Risikoklassifizierung vorliegt.

---

## 5. AI-Literacy-Programm einführen

AI-Literacy-Pflichten gelten nach EU-Kommissions-Timeline seit 02.02.2025. ([Digitale Zukunft Europas](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai?utm_source=chatgpt.com "AI Act | Shaping Europe's digital future - European Union"))

### 5.1 Datei anlegen

`docs/ai-governance/ai-literacy-program.md`

```markdown
# AI Literacy Program

## 1. Ziel
Alle relevanten Rollen müssen die Fähigkeiten, Grenzen, Risiken und zulässigen Nutzungsweisen des Multi-Agent-Systems verstehen.

## 2. Betroffene Rollen
| Rolle | Schulung erforderlich | Inhalt | Nachweis |
|---|---:|---|---|
| Product Owner | Ja | Use Case, Grenzen, AI Act |  |
| Maintainer | Ja | Secure AI Development, Prompt Injection |  |
| Human Reviewer | Ja | Human Oversight, Eskalation |  |
| Security Architect | Ja | Agent Security, Supply Chain |  |
| Datenschutz | Ja | Datenklassen, Model Routing, Transfers |  |
| Endnutzer | abhängig vom Use Case | Transparenz, Grenzen, sichere Nutzung |  |

## 3. Mindestinhalte
- AI-Act-Grundlagen
- DSGVO-Grundlagen
- Prompt Injection
- Datenklassifizierung
- Model Routing
- Human Oversight
- Fehlverhalten und Incident-Meldung
- Grenzen des Systems

## 4. Nachweis
| Person/Rolle | Datum | Inhalt | Version | Bestätigung |
|---|---|---|---|---|
```

### 5.2 Abnahmekriterium

Kein produktiver Betrieb ohne dokumentierte AI-Literacy-Abdeckung für relevante Rollen.

---

## 6. Datenklassifizierung und Model Privacy bauen

### 6.1 Datenklassen definieren

`docs/privacy/data-classification-policy.md`

```markdown
# Data Classification Policy

## Datenklassen

| Klasse | Beschreibung | Externe Modell-API | EU-hosted | Lokal |
|---|---|---:|---:|---:|
| public | Öffentlich verfügbare Informationen | erlaubt | erlaubt | erlaubt |
| internal | Interne, nicht öffentliche Informationen | Review | erlaubt | erlaubt |
| confidential | Geschäftsgeheimnisse / vertrauliche Inhalte | blockiert | Review | bevorzugt |
| personal_data_masked | Maskierte personenbezogene Daten | Ausnahmefreigabe | Review | erlaubt |
| personal_data_unmasked | Unmaskierte personenbezogene Daten | blockiert | Review | bevorzugt |
| special_category_data | Besondere Kategorien personenbezogener Daten | blockiert | Ausnahme | blockieren oder lokal |
| secrets | Tokens, Keys, Credentials | blockiert | blockiert | blockiert |
| security_sensitive | Schwachstellen, Exploit-Kontext, Security-Code | blockiert | Review | bevorzugt |
| audit_logs_sensitive | sensible Auditdaten | blockiert | Review | bevorzugt |
```

### 6.2 Model-Routing-Policy anlegen

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

### 6.3 Vendor Due Diligence anlegen

`docs/privacy/ai-vendor-due-diligence.md`

```markdown
# AI Vendor Due Diligence

## Anbieter
- Name:
- Dienst:
- Rolle: Controller / Processor / Subprocessor / eigener Verantwortlicher
- Region:
- Support-Region:
- Subprozessoren:
- Datenarten:
- Retention:
- Training mit Kundendaten: Ja/Nein
- Telemetrie: Ja/Nein

## DSGVO-Prüfung
| Punkt | Status | Evidenz |
|---|---|---|
| AVV/DPA vorhanden |  |  |
| TOMs geprüft |  |  |
| Subprozessoren geprüft |  |  |
| Drittlandtransfer geprüft |  |  |
| SCC / DPF / Angemessenheitsbeschluss geprüft |  |  |
| TIA erforderlich |  |  |
| Löschung geregelt |  |  |
| Incident Notification geregelt |  |  |

## Entscheidung
- Freigegeben:
- Freigabeumfang:
- Datenklassen:
- Ablaufdatum der Freigabe:
- Reviewer:
```

### 6.4 Abnahmekriterium

Eine externe Modell-, Embedding-, Tool-, Observability- oder Security-API darf erst genutzt werden, wenn `ai-vendor-due-diligence.md` ausgefüllt und genehmigt ist.

---

## 7. Privacy-by-Design und PII-Gate bauen

### 7.1 PII-Workflow

```text
Input
→ Data Classification
→ PII Detection
→ Masking / Pseudonymisierung / Blockierung
→ Model Routing Policy
→ Agent Processing
→ Output Validation
→ Audit Event
```

### 7.2 Empfohlene Bausteine

| Zweck           | Open Source / Technik                   |
| --------------- | --------------------------------------- |
| PII Detection   | Microsoft Presidio, spaCy, scrubadub    |
| Policy Decision | Open Policy Agent / Rego                |
| Secrets         | HashiCorp Vault, GitHub OIDC, Cloud KMS |
| Egress Control  | Proxy, AI Gateway, Firewall Allowlist   |
| Audit           | immudb, OpenSearch, SIEM, WORM Storage  |

### 7.3 Audit-Minimierung anlegen

`docs/privacy/audit-log-minimization-policy.md`

```markdown
# Audit Log Minimization Policy

## Grundsatz
Auditierbarkeit wird primär über Hashes, IDs, Policy Decisions, Datenklassen, Zeitpunkte, Signaturen und Freigabeereignisse hergestellt.

## Default-Regeln
| Inhalt | Default | Ausnahme |
|---|---|---|
| Prompt | Hash + Prompt-Version | Rohprompt nur mit Zweck, Rechtsgrundlage, Retention |
| Output | Output-Hash + Klassifikation | Rohoutput nur bei Prüfzweck oder Incident |
| PII | Redacted / tokenisiert | Klartext nur bei zwingendem Zweck |
| Secrets | niemals speichern | keine Ausnahme |
| Tool-Parameter | Parameter-Hash | Rohparameter nur bei nicht-sensitiven Daten |
| Policy Decision | vollständig speichern | Pflichtfeld |
| Human Approval | vollständig speichern | Pflichtfeld |
| Model Route | vollständig speichern | Pflichtfeld |
```

### 7.4 Abnahmekriterium

Audit Logs dürfen keine Secrets enthalten. PII, Rohprompts und Rohoutputs dürfen nur mit dokumentiertem Zweck, Rechtsgrundlage, Retention und Zugriffsschutz gespeichert werden.

---

## 8. Agent-to-Agent Zero Trust bauen

### 8.1 Agenten-Inventar

`docs/agents/agent-inventory.md`

```markdown
# Agent Inventory

| Agent-ID | Rolle | Version | Owner | Datenklassen | Tools | Modellroute | Human Approval erforderlich |
|---|---|---|---|---|---|---|---|
| research-agent | evidence_collection | 1.0.0 |  | public, internal | web_search, repo_read | eu_hosted/local | Nein |
| code-agent | code_generation | 1.0.0 |  | internal | repo_read, repo_write | local/eu_hosted | Ja |
| compliance-agent | policy_review | 1.0.0 |  | internal | repo_read, policy_eval | local/eu_hosted | Ja |
```

### 8.2 Agent Card Template

`docs/agents/agent-cards/agent-card-template.md`

```markdown
# Agent Card

## Identität
- Agent-ID:
- Version:
- Owner:
- Rolle:
- Zweck:

## Berechtigungen
- Erlaubte Tools:
- Verbotene Tools:
- Erlaubte Datenklassen:
- Verbotene Datenklassen:
- Erlaubte Modellrouten:

## Sicherheitsregeln
- Muss Nachrichten signieren: Ja
- Muss Policy-Version mitsenden: Ja
- Muss Capability Scope mitsenden: Ja
- Darf Memory schreiben: Ja/Nein
- Darf Code ausführen: Ja/Nein
- Sandbox erforderlich: Ja/Nein

## Human Oversight
- HITL erforderlich bei:
- HOTL Monitoring:
- Eskalationsregel:

## Audit
- Pflichtfelder:
- Retention:
```

### 8.3 Agent Communication Policy

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

### 8.4 Agent-Security-Controls

| Risiko                     | Kontrolle                                                                    |
| -------------------------- | ---------------------------------------------------------------------------- |
| Agent Goal Hijack          | Zielbindung je Agent, task-scoped capability tokens, Zielvalidierung         |
| Tool Misuse                | Tool Allowlist, Schema Validation, Human Approval bei irreversiblen Aktionen |
| Identity & Privilege Abuse | mTLS/SPIFFE, signierte Agent Claims, scoped credentials                      |
| Prompt Injection           | Instruction/Data Separation, Context Firewall, Retrieval Trust Scoring       |
| RAG-Injection              | RAG-Dokumente immer als Daten behandeln, nie als Instruktionen               |
| Tool Poisoning             | signierte Tool-Manifeste, Tool Registry Review                               |
| Memory Poisoning           | getrennte Memory Stores, Write Approval, Memory Audit                        |
| Insecure Output Handling   | Output Schema Validation, keine direkte Shell/API/SQL-Ausführung            |
| Unsandboxed Execution      | Ephemeral Sandbox, no-network default, Ressourcenlimits                      |
| MCP Server Compromise      | Server Identity, Tool Manifest Signing, Capability Scope                     |

### 8.5 Abnahmekriterium

Kein Agent darf eine Nachricht, ein Tool-Ergebnis oder einen Memory-Eintrag eines anderen Agenten ohne Authentifizierung, Signatur, Policy-Version, Datenklasse und Capability Scope verwenden.

---

## 9. OPA/Rego-Policies bauen

### 9.1 Model Routing Policy

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

### 9.2 Agent Communication Policy

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

### 9.3 Abnahmekriterium

CI muss fehlschlagen, wenn `opa test policies/` fehlschlägt oder ein Deny-Ergebnis für Model Routing oder Agent Communication vorliegt.

---

## 10. DevSecOps-Pipeline bauen

### 10.1 Required Gates

| Gate                          | Blockiert bei                                                     |
| ----------------------------- | ----------------------------------------------------------------- |
| Quality Gate                  | Ruff/mypy/pytest Fehler                                           |
| SAST Gate                     | High/Critical Finding                                             |
| Secret Gate                   | gefundenes Secret                                                 |
| Dependency Gate               | Critical CVE oder unzulässige Dependency                         |
| License Gate                  | verbotene oder unbekannte Lizenz                                  |
| Model License Gate            | unklare Modell-/Dataset-Lizenz                                    |
| Privacy Gate                  | unmaskierte PII in nicht erlaubtem Kontext                        |
| Transfer Gate                 | externer Anbieter ohne DPA, Subprocessor Review, Transferprüfung |
| Model Privacy Gate            | externe Modellroute ohne Freigabe                                 |
| Agent-to-Agent Gate           | fehlende Authentifizierung, Signatur, Policy-Version              |
| Execution Gate                | Code-/Tool-Ausführung ohne Sandbox                               |
| Tool Registry Gate            | unsignierte Tools oder ungeprüfte Tool-Manifeste                 |
| AI-BOM Gate                   | fehlende Modelle, Prompts, Agents, Tools oder Datasets            |
| SBOM Gate                     | fehlende oder veraltete SBOM                                      |
| Audit Privacy Gate            | Audit Logs mit PII/Secrets/Rohprompts ohne Rechtsgrundlage        |
| Release Integrity Gate        | fehlende Signatur, Provenance oder Attestation                    |
| GitHub Actions Hardening Gate | ungepinnte Actions oder zu breite Permissions                     |

### 10.2 Workflow anlegen

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

### 10.3 Produktionsanforderung

Die YAML-Datei zeigt Tags zur Lesbarkeit. Für produktive Nutzung müssen Third-Party-Actions auf vollständige Commit-SHAs gepinnt werden, weil GitHub vollständige Commit-SHAs als einzige unveränderliche Pinning-Variante beschreibt. ([GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use?utm_source=chatgpt.com "Secure use reference - GitHub Docs"))

---

## 11. SBOM und AI-/ML-BOM bauen

### 11.1 SBOM

Pflicht pro Release:

```text
bom/sbom/sbom.json
```

Format:

```text
CycloneDX JSON
```

Inhalt:

* Python Dependencies
* Container Dependencies
* Build Tools
* Runtime Dependencies
* Licenses
* Package Hashes
* Known Vulnerability Links, soweit Tooling verfügbar

### 11.2 AI-BOM Schema

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

### 11.3 Abnahmekriterium

Ein Release darf nicht erstellt werden, wenn SBOM oder AI-BOM fehlen, leer sind oder nicht validiert werden können.

---

## 12. Release Integrity und Attestation bauen

### 12.1 Release-Artefakte

Jeder Release enthält:

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

### 12.2 Attestation Workflow

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

GitHub beschreibt Artifact Attestations als kryptografisch signierte Claims, die Build-Provenance und Integrität nachweisbar machen. ([GitHub Docs](https://docs.github.com/en/actions/concepts/security/artifact-attestations?utm_source=chatgpt.com "Artifact attestations - GitHub Docs"))

### 12.3 Abnahmekriterium

Ein Release ohne signierte Attestation ist nicht freigabefähig.

---

## 13. Audit Logging bauen

### 13.1 Pflicht-Events

`docs/audit/logging-schema.md`

```markdown
# Logging Schema

| Ereignis | Pflichtfelder |
|---|---|
| Agentenstart | Agent-ID, Version, Rolle, Policy-Version |
| Agent-to-Agent-Nachricht | Sender, Empfänger, Message Hash, Signatur, Auth-Status |
| Nutzereingabe | Input-Kategorie, Zweck, PII-Status |
| PII-Erkennung | erkannte Entitäten, Masking-Status, Policy Decision |
| Model Routing | Modellroute, Datenklasse, Rechtsraum, Entscheidung |
| Tool-Aufruf | Tool-ID, Parameter-Hash, Ergebnis-Hash |
| Policy-Entscheidung | Policy-ID, Version, Ergebnis, Begründung |
| Guardrail-Verstoß | Regel, Schweregrad, Block-/Allow-Entscheidung |
| Human Approval | Prüfer, Zeitpunkt, Entscheidung, Scope |
| Codeänderung | Commit-ID, PR-ID, Autor, Agent-ID |
| Release | SBOM-ID, AI-BOM-ID, Signatur, Artefakt-Hash |
| Output | Output-Hash, Prompt-Version, Modellversion |
| Rechtsrollenbewertung | Use Case, Rolle, Scope, Release-ID, Prüfer, Ergebnis |
| FRIA Trigger | Trigger, Risikoklasse, Betroffenengruppe, Entscheidung |
| Vendor Transfer Check | Anbieter, Rechtsraum, Subprozessoren, Transfergrundlage |
| Sandbox Execution | Sandbox-ID, Tool-ID, Input-Hash, Output-Hash, Network Policy |
| Tool Registry Change | Tool-ID, Manifest Hash, Signatur, Berechtigungen, Reviewer |
| RAG Context Ingestion | Dokument-ID, Quelle, Trust Score, Datenklasse, Hash |
| Audit Redaction | Feld, Redaction-Typ, Policy-ID, Ergebnis |
| Post-Market Monitoring Signal | Signal-ID, Modell/Agent, Schweregrad, Maßnahme |
```

### 13.2 Audit-Pipeline

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

### 13.3 Abnahmekriterium

Audit Logs müssen manipulationsresistent, datensparsam, zugriffsbeschränkt und exportierbar sein.

---

## 14. CRA Vulnerability Handling bauen

### 14.1 Datei anlegen

`docs/security/cra-vulnerability-reporting.md`

```markdown
# CRA Vulnerability Reporting

## 1. Scope
Dieses Verfahren gilt für Produkte mit digitalen Elementen, soweit der CRA-Scope bestätigt ist.

## 2. Meldepflichtige Ereignisse
- aktiv ausgenutzte Schwachstelle
- schwerer Sicherheitsvorfall mit Auswirkung auf die Sicherheit des Produkts

## 3. Fristen
- Early Warning: innerhalb von 24 Stunden
- Hauptmeldung: innerhalb von 72 Stunden
- Abschlussbericht: nach Analyse / Behebung

## 4. Pflichtfelder
| Feld | Beschreibung |
|---|---|
| Produkt / Release | betroffene Version |
| Schwachstelle | Art, Komponente, CVE falls vorhanden |
| Ausnutzung | bekannt / vermutet / bestätigt |
| Auswirkungen | betroffene Nutzer, Systeme, Daten |
| Maßnahmen | Mitigation, Patch, Workaround |
| Zeitlinie | Entdeckung, Bewertung, Meldung, Behebung |
| Verantwortliche | Incident Owner, Security Owner, Release Manager |

## 5. Evidence
- Logs
- SBOM
- AI-BOM, falls KI-Komponente betroffen
- Commit IDs
- Patches
- Kommunikation
```

Die Europäische Kommission nennt für CRA-Meldepflichten ab 11.09.2026 aktiv ausgenutzte Schwachstellen und schwere Sicherheitsvorfälle. ([Digitale Zukunft Europas](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting?utm_source=chatgpt.com "Cyber Resilience Act - Reporting obligations"))

### 14.2 Abnahmekriterium

Für CRA-relevante Releases muss ein 24h/72h-Meldeprozess dokumentiert, getestet und einem Incident Owner zugewiesen sein.

---

## 15. Human Oversight bauen

### 15.1 Human Oversight Matrix

`docs/ai-act/human-oversight-matrix.md`

```markdown
# Human Oversight Matrix

| Aktion | Risiko | Modus | Freigabe erforderlich |
|---|---|---|---|
| Informationsrecherche | niedrig | Human-on-the-loop | Nein |
| Codegenerierung | mittel | Human-in-the-loop | Ja bei Merge |
| Dependency hinzufügen | mittel/hoch | Human-in-the-loop | Ja |
| Externe Modellroute aktivieren | hoch | Human-in-the-loop | Ja |
| Produktion deployen | hoch | Human-in-the-loop | Ja |
| Sensitive Daten exportieren | hoch | Human-in-the-loop | Ja |
| High-Risk-AI-Entscheidung | hoch/kritisch | Human-in-the-loop | Ja |
| Security Policy ändern | hoch | Human-in-the-loop | Ja |
| Irreversible Tool Action | hoch | Human-in-the-loop | Ja |
```

### 15.2 Abnahmekriterium

Kritische Aktionen dürfen nicht allein durch Agenten ausgelöst werden.

---

## 16. Post-Market Monitoring und Eval Regression bauen

### 16.1 Monitoring-Datei

`docs/ai-act/post-market-monitoring-plan.md`

```markdown
# Post-Market Monitoring Plan

## 1. Überwachte Komponenten
- Modelle
- Agenten
- Prompts
- Tools
- Policies
- Model Routes
- Datenquellen
- RAG-Kontexte

## 2. Signale
| Signal | Quelle | Reaktion |
|---|---|---|
| Fehlklassifikation | Eval Suite | Review |
| Policy Bypass | OPA Logs | Incident |
| Prompt Injection Attempt | Guardrail Logs | Block + Review |
| Tool Misuse | Tool Audit | Incident |
| Drift | Eval Regression | Re-Evaluation |
| Sensitive Data Exposure | DLP / Audit | Incident |
| Nutzerbeschwerde | Support / Ticket | Review |
| Security Finding | SAST/DAST/SIEM | Incident |

## 3. Frequenz
- Release: vollständige Regression
- Monatlich: Policy Review
- Quartalsweise: Model Privacy Review
- Ereignisbasiert: Incident / Major Model Change / New Tool
```

### 16.2 Abnahmekriterium

Kein produktiver Release ohne definierte Eval Regression und Monitoring-Signale.

---

## 17. Priorisierte Umsetzung

### Phase 1 — Governance-Baseline

**Ziel:** regulatorischen und organisatorischen Scope kontrollieren.

Umsetzen:

1. Repository-Struktur anlegen.
2. CODEOWNERS aktivieren.
3. Provider-/Deployer-/Product-Manufacturer-/FOSS-Scope dokumentieren.
4. AI-Act-Risikoklasse je Use Case dokumentieren.
5. AI-Literacy-Programm dokumentieren.
6. Agenten-Inventar erstellen.
7. Modell-Inventar erstellen.
8. Tool-Registry erstellen.
9. Risk Register anlegen.

Output:

```text
docs/ai-act/provider-deployer-role-classification.md
docs/ai-act/risk-classification.md
docs/ai-governance/ai-literacy-program.md
docs/agents/agent-inventory.md
docs/models/model-inventory.md
.github/CODEOWNERS
```

Definition of Done:

```text
Alle Pflichtdateien existieren.
Alle Owner sind benannt.
Jeder Use Case hat Rolle, Scope und Risikoklasse.
```

---

### Phase 2 — Datenschutz und Model Privacy

**Ziel:** keine unkontrollierte Datenweitergabe an Modelle, Tools oder Agenten.

Umsetzen:

1. Datenklassen definieren.
2. Model-Routing-Policy erstellen.
3. Externe Modell-APIs default-deny setzen.
4. PII-Erkennung und Masking definieren.
5. Vendor Due Diligence einführen.
6. Transferprüfung einführen.
7. Audit Log Minimization Policy erstellen.
8. DPIA Draft erstellen.

Output:

```text
docs/privacy/data-classification-policy.md
docs/models/model-routing-policy.md
docs/privacy/ai-vendor-due-diligence.md
docs/privacy/international-transfer-assessment.md
docs/privacy/audit-log-minimization-policy.md
docs/privacy/dpia-draft.md
```

Definition of Done:

```text
Keine externe Modellroute ohne Policy Decision.
Keine personenbezogenen Daten ohne Datenklasse.
Keine Anbieterfreigabe ohne DPA/Subprocessor/Transfer-Prüfung.
```

---

### Phase 3 — DevSecOps und Supply Chain

**Ziel:** Pull Requests blockieren unsichere Änderungen.

Umsetzen:

1. Ruff, mypy, pytest integrieren.
2. CodeQL integrieren.
3. Semgrep und Bandit integrieren.
4. Dependency Review aktivieren.
5. Gitleaks aktivieren.
6. Lizenzprüfung integrieren.
7. SBOM automatisieren.
8. GitHub Actions Hardening prüfen.
9. SARIF Upload aktivieren.
10. Required Checks aktivieren.

Output:

```text
.github/workflows/compliance-security-ai.yml
scripts/check_github_actions_hardening.py
bom/sbom/sbom.json
security-report.json
license-report.json
```

Definition of Done:

```text
PRs mit Critical CVE, Secrets, High/Critical SAST Finding oder unbekannter Lizenz werden blockiert.
```

---

### Phase 4 — Agent-to-Agent Security

**Ziel:** Zero Trust zwischen Agenten.

Umsetzen:

1. Agent Cards erstellen.
2. Agent Permission Matrix erstellen.
3. Agent Communication Policy einführen.
4. Signierte Agent Messages erzwingen.
5. Capability Tokens einführen.
6. Tool Allowlist einführen.
7. Memory Write Controls einführen.
8. Instruction/Data Separation erzwingen.
9. Sandbox für Code-/Tool-Ausführung einführen.
10. Tool-/MCP-Manifest-Signierung einführen.

Output:

```text
docs/agents/agent-cards/
docs/agents/agent-permission-matrix.md
docs/agents/agent-communication-policy.md
docs/security/sandboxed-execution-policy.md
docs/security/tool-registry-security.md
policies/rego/agent_communication.rego
```

Definition of Done:

```text
Kein Agent akzeptiert unsignierte Nachrichten, unsignierte Tool-Ergebnisse oder fremde Daten ohne Policy Check.
```

---

### Phase 5 — AI-BOM und Release Governance

**Ziel:** jeder Release ist prüfbar, reproduzierbar und signiert.

Umsetzen:

1. AI-BOM Schema finalisieren.
2. AI-BOM Generator bauen.
3. AI-BOM Validator bauen.
4. Model Cards erzwingen.
5. Agent Cards erzwingen.
6. Release Attestation erzeugen.
7. cosign/Sigstore oder GitHub Artifact Attestations integrieren.
8. Release Bundle erzeugen.
9. Human Approval für kritische Releases erzwingen.

Output:

```text
bom/ai-bom/ai-bom.json
bom/ml-bom/
release-attestation.json
docs/models/model-cards/
docs/agents/agent-cards/
```

Definition of Done:

```text
Kein Release ohne SBOM, AI-BOM, Risikoklassifizierung, Signatur und Attestation.
```

---

### Phase 6 — Audit, Monitoring und Betrieb

**Ziel:** revisionsfähige Nachvollziehbarkeit ohne unnötige Rohdatenprotokollierung.

Umsetzen:

1. Logging Schema einführen.
2. Audit-Minimierung erzwingen.
3. Hash Chains einführen.
4. Signierte Audit Events einführen.
5. Append-only Storage anbinden.
6. WORM Archive anbinden.
7. SIEM Export einführen.
8. Post-Market Monitoring einführen.
9. CRA Vulnerability Reporting einführen.
10. Serious Incident Response für AI-Vorfälle einführen.

Output:

```text
docs/audit/logging-schema.md
docs/audit/audit-policy.md
docs/ai-act/post-market-monitoring-plan.md
docs/ai-act/serious-incident-response-ai.md
docs/security/cra-vulnerability-reporting.md
audit-export.jsonl
```

Definition of Done:

```text
Jede kritische Agenten-, Modell-, Tool-, Policy- und Release-Entscheidung ist über Hashes, Signaturen, IDs und Policy Decisions nachvollziehbar.
```

---

## 18. Nicht akzeptieren

Diese Zustände blockieren Merge oder Release:

```text
unmaskierte PII in externen Modellaufrufen
besondere Kategorien personenbezogener Daten in externen Modellaufrufen
ungeprüfte Drittland-, Support- oder Subprocessor-Zugriffe
unsignierte Agent-to-Agent-Kommunikation
Agent-to-Agent-Kommunikation ohne Policy-Version
Agenten mit pauschalen Tool-Rechten
RAG-Kontexte, die als Instruktionen behandelt werden
Tool-/MCP-Manifeste ohne Signatur und Review
Code- oder Tool-Ausführung ohne Sandbox bei riskanten Aktionen
neue Dependencies ohne CVE- und Lizenzprüfung
Releases ohne SBOM
Releases ohne AI-BOM
Releases ohne Signatur, Provenance oder Attestation
Prompts oder Systemprompts ohne Version, Hash, Owner und Klassifizierung
Cloud-Modellnutzung ohne DPA, No-Training-Zusage, Retention-Regelung, Subprocessor Review und Rechtsraumprüfung
Audit Logs mit PII, Secrets oder Rohprompts ohne dokumentierte Rechtsgrundlage, Zweckbindung, Retention und Zugriffsschutz
```

---

## 19. Finale Abnahme-Checkliste

| Bereich                                                           | Pflicht erfüllt |
| ----------------------------------------------------------------- | ---------------: |
| AI-Act-Rolle je Use Case dokumentiert                             |               ☐ |
| AI-Act-Risikoklasse dokumentiert                                  |               ☐ |
| AI-Literacy-Programm dokumentiert                                 |               ☐ |
| DSGVO-Datenklassen definiert                                      |               ☐ |
| DPIA Draft vorhanden                                              |               ☐ |
| Model Routing Policy aktiv                                        |               ☐ |
| Externe Modell-APIs default-deny                                  |               ☐ |
| Vendor Due Diligence vorhanden                                    |               ☐ |
| Transferprüfung vorhanden                                        |               ☐ |
| CODEOWNERS aktiv                                                  |               ☐ |
| Required Checks aktiv                                             |               ☐ |
| CodeQL aktiv                                                      |               ☐ |
| Semgrep/Bandit aktiv                                              |               ☐ |
| Dependency Review aktiv                                           |               ☐ |
| Secret Scanning aktiv                                             |               ☐ |
| Lizenzprüfung aktiv                                              |               ☐ |
| GitHub Actions SHA-Pinning geplant/umgesetzt                      |               ☐ |
| SBOM pro Release vorhanden                                        |               ☐ |
| AI-BOM pro Release vorhanden                                      |               ☐ |
| Agent Cards vorhanden                                             |               ☐ |
| Model Cards vorhanden                                             |               ☐ |
| Agent-to-Agent Signaturen aktiv                                   |               ☐ |
| Capability Tokens aktiv                                           |               ☐ |
| Sandbox Policy aktiv                                              |               ☐ |
| Tool Registry signiert                                            |               ☐ |
| Audit Logging Schema vorhanden                                    |               ☐ |
| Audit-Minimierung dokumentiert                                    |               ☐ |
| Release Attestation vorhanden                                     |               ☐ |
| Post-Market Monitoring vorhanden                                  |               ☐ |
| CRA Vulnerability Reporting vorhanden, falls CRA-Scope bestätigt |               ☐ |
| Serious Incident Response vorhanden                               |               ☐ |

---

## 20. Zielzustand

Das Repository ist erst releasefähig, wenn folgende Aussage belegbar ist:

> Jeder Agent, jedes Modell, jedes Tool, jeder Prompt, jede Policy, jede Dependency und jeder Release ist klassifiziert, versioniert, berechtigt, geprüft, auditierbar und reproduzierbar. Externe Modell- und Toolrouten sind default-deny. Kritische Aktionen benötigen Human Approval. Releases ohne SBOM, AI-BOM, Signatur, Provenance und Risikoklassifizierung werden blockiert.
