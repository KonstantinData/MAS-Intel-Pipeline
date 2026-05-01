# Repository Governance

## Purpose

This document defines the governance rules for the repository. Governance ensures that all changes to the repository are controlled, traceable, and auditable. No code or documentation is merged into protected branches without a defined approval process.

---

## CODEOWNERS

The `.github/CODEOWNERS` file defines which individuals or teams are responsible for specific paths in the repository. When changes are made to these paths, review requests are automatically assigned to the corresponding CODEOWNERS.

Example configuration:

```text
* @KonstantinData
docs/de/privacy/ @KonstantinData
docs/en/security/ @KonstantinData
.github/workflows/ @KonstantinData
```


Rules:

* Changes to all paths require approval from the responsible CODEOWNERS.
* This applies to both `docs/de` and `docs/en`.
* A merge without CODEOWNERS approval is not possible, provided that the corresponding branch protection rules are enabled.

---

## Branch Protection

The following branches are protected by branch protection rules:

* `main` (mandatory)
* `develop` (optional, recommended)

Required settings:

* Pull request required before merge
* Review from CODEOWNERS required
* Status checks must pass successfully
* Administrators are included in protection rules (must be enabled)

---

## Merge Process

1. Create a new branch from the current state of `main`.
2. Make changes and open a pull request.
3. CODEOWNERS are automatically requested for review and must approve the PR.
4. All configured CI checks must pass successfully.
5. Merge is only allowed after full approval and successful checks.

---

## Governance Scope

The following repository areas are subject to governance:

* `docs/de/**`
* `docs/en/**`
* `policies/**`
* `bom/**`
* `.github/workflows/**`
* `scripts/**`

---

## Non-Compliance

A merge is blocked if any of the following conditions apply:

* No approval from CODEOWNERS
* Required status checks have failed
* Required documentation is missing
* Structural violations of repository conventions are present
