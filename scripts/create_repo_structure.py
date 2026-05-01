#!/usr/bin/env python3
"""
Create the repo folder structure and placeholder files.

Rules:
- All Markdown docs are created under docs/en/... only.
- Non-doc files (.github, workflows, scripts, bom, policies) are created once.
- The script is idempotent (won't overwrite existing files by default).

Usage:
  python create_repo_structure.py [--root .] [--overwrite]

Notes:
- docs/models/model-cards/ and docs/agents/agent-cards/ are directories only.
- scripts/*.py are created as placeholders (empty or minimal header).
- workflow yml + CODEOWNERS are created as placeholders.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse


DOC_SUBDIRS = [
    "ai-act",
    "ai-governance",
    "privacy",
    "security",
    "models",
    "agents",
    "licenses",
    "audit",
    "risk",
]

DOC_DIR_ONLY = [
    "models/model-cards",
    "agents/agent-cards",
]

DOC_FILES = [
    # docs/ai-act/
    "ai-act/ai-system-card.md",
    "ai-act/risk-classification.md",
    "ai-act/provider-deployer-role-classification.md",
    "ai-act/prohibited-practices-check.md",
    "ai-act/human-oversight-matrix.md",
    "ai-act/technical-documentation.md",
    "ai-act/fundamental-rights-impact-assessment.md",
    "ai-act/post-market-monitoring-plan.md",
    "ai-act/serious-incident-response-ai.md",
    "ai-act/corrective-action-process.md",
    "ai-act/ai-system-change-control.md",
    # docs/ai-governance/
    "ai-governance/ai-management-system.md",
    "ai-governance/ai-policy.md",
    "ai-governance/ai-risk-management-process.md",
    "ai-governance/ai-impact-assessment-template.md",
    "ai-governance/ai-literacy-program.md",
    "ai-governance/ai-change-management.md",
    # docs/privacy/
    "privacy/dpia-draft.md",
    "privacy/data-flow-map.md",
    "privacy/data-classification-policy.md",
    "privacy/pii-handling-policy.md",
    "privacy/retention-policy.md",
    "privacy/deletion-policy.md",
    "privacy/model-privacy-policy.md",
    "privacy/international-transfer-assessment.md",
    "privacy/subprocessor-register.md",
    "privacy/ai-vendor-due-diligence.md",
    "privacy/audit-log-minimization-policy.md",
    # docs/security/
    "security/threat-model.md",
    "security/secure-development-policy.md",
    "security/agent-to-agent-security.md",
    "security/incident-response-plan.md",
    "security/vulnerability-disclosure-policy.md",
    "security/cra-vulnerability-reporting.md",
    "security/coordinated-vulnerability-disclosure.md",
    "security/vulnerability-handling-sla.md",
    "security/security-update-policy.md",
    "security/support-period-policy.md",
    "security/sandboxed-execution-policy.md",
    "security/tool-registry-security.md",
    # docs/models/
    "models/model-inventory.md",
    "models/model-routing-policy.md",
    "models/local-model-policy.md",
    "models/cloud-model-policy.md",
    # docs/agents/
    "agents/agent-inventory.md",
    "agents/agent-permission-matrix.md",
    "agents/agent-communication-policy.md",
    # docs/licenses/
    "licenses/license-policy.md",
    "licenses/model-license-policy.md",
    "licenses/dataset-license-policy.md",
    "licenses/third-party-notices.md",
    # docs/audit/
    "audit/audit-policy.md",
    "audit/logging-schema.md",
    "audit/evidence-retention-policy.md",
    "audit/release-attestation-policy.md",
    # docs/risk/
    "risk/nist-ai-rmf-map.md",
    "risk/genai-risk-profile.md",
    "risk/eval-and-red-team-plan.md",
    "risk/model-behavior-monitoring.md",
]

SINGLETON_DIRS = [
    ".github/workflows",
    "bom/sbom",
    "bom/ai-bom",
    "bom/ml-bom",
    "policies/opa",
    "policies/rego",
    "policies/agent-guardrails",
    "policies/model-routing",
    "policies/data-classification",
    "policies/license",
    "policies/tool-access",
    "scripts",
]

SINGLETON_FILES = [
    ".github/CODEOWNERS",
    ".github/workflows/compliance-security-ai.yml",
    ".github/workflows/release-attestation.yml",
    "scripts/generate_ai_bom.py",
    "scripts/validate_ai_bom.py",
    "scripts/check_github_actions_hardening.py",
    "scripts/generate_release_attestation.py",
    "scripts/validate_audit_schema.py",
]

# From "2.2 Abnahmekriterium" (paths are WITHOUT language prefix in the spec)
ACCEPTANCE_DOCS = [
    "ai-act/risk-classification.md",
    "ai-act/provider-deployer-role-classification.md",
    "privacy/data-classification-policy.md",
    "privacy/model-privacy-policy.md",
    "privacy/audit-log-minimization-policy.md",
    "security/threat-model.md",
    "security/agent-to-agent-security.md",
    "models/model-routing-policy.md",
    "agents/agent-permission-matrix.md",
    "audit/logging-schema.md",
]
ACCEPTANCE_SINGLETON = [
    ".github/CODEOWNERS",
    ".github/workflows/compliance-security-ai.yml",
]


@dataclass(frozen=True)
class WriteResult:
    created: int
    skipped: int


def mkdirp(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str, overwrite: bool) -> bool:
    """
    Returns True if created/overwritten, False if skipped.
    """
    if path.exists() and not overwrite:
        return False
    mkdirp(path.parent)
    path.write_text(content, encoding="utf-8")
    return True


def md_placeholder(rel_md_path: str, lang: str) -> str:
    title = Path(rel_md_path).stem.replace("-", " ").title()
    return (
        f"# {title}\n\n"
        f"> Language: `{lang}`\n"
        f"> Path: `{rel_md_path}`\n\n"
        "## Purpose\n\n"
        "TBD\n"
    )


def py_placeholder(rel_py_path: str) -> str:
    return (
        '"""Placeholder script.\n\n'
        f"Path: {rel_py_path}\n"
        '"""\n\n'
        "def main() -> None:\n"
        "    raise SystemExit('Not implemented')\n\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    )


def yml_placeholder(rel_yml_path: str) -> str:
    name = Path(rel_yml_path).stem.replace("-", " ").title()
    return (
        f"name: {name}\n"
        "on:\n"
        "  workflow_dispatch:\n"
        "permissions: {}\n"
        "jobs:\n"
        "  placeholder:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - run: echo 'TODO'\n"
    )


def codeowners_placeholder() -> str:
    return (
        "# Placeholder CODEOWNERS\n"
        "# Example:\n"
        "# * @your-org/your-team\n"
    )


def create_structure(root: Path, overwrite: bool) -> None:
    # Singleton dirs
    for d in SINGLETON_DIRS:
        mkdirp(root / d)

    created = skipped = 0

    # Singleton files
    for f in SINGLETON_FILES:
        p = root / f
        if p.suffix == ".py":
            content = py_placeholder(f)
        elif p.suffix in (".yml", ".yaml"):
            content = yml_placeholder(f)
        else:
            content = ""
        ok = write_file(p, content, overwrite=overwrite)
        created += int(ok)
        skipped += int(not ok)

    # CODEOWNERS with content
    p = root / ".github" / "CODEOWNERS"
    ok = write_file(p, codeowners_placeholder(), overwrite=overwrite)
    created += int(ok)
    skipped += int(not ok)

    # Docs: en only
    lang = "en"
    # Create base folders
    for sd in DOC_SUBDIRS:
        mkdirp(root / "docs" / lang / sd)

    # Create "dir only" folders
    for dd in DOC_DIR_ONLY:
        mkdirp(root / "docs" / lang / dd)

    # Create md files
    for rel in DOC_FILES:
        p = root / "docs" / lang / rel
        ok = write_file(p, md_placeholder(
            rel, lang=lang), overwrite=overwrite)
        created += int(ok)
        skipped += int(not ok)

    print(f"Done. created/overwritten={created}, skipped={skipped}")
    verify_acceptance(root)


def verify_acceptance(root: Path) -> None:
    missing = []

    # Acceptance docs must exist in en
    for rel in ACCEPTANCE_DOCS:
        p = root / "docs" / "en" / rel
        if not p.exists():
            missing.append(str(p.relative_to(root)))

    # Acceptance singleton files
    for rel in ACCEPTANCE_SINGLETON:
        p = root / rel
        if not p.exists():
            missing.append(str(p.relative_to(root)))

    if missing:
        print("\nACCEPTANCE CHECK: FAILED (missing paths)")
        for m in missing:
            print(f"  - {m}")
        raise SystemExit(2)

    print("ACCEPTANCE CHECK: OK")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root directory")
    ap.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files (default: skip if exists)",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    create_structure(root, overwrite=bool(args.overwrite))


if __name__ == "__main__":
    main()
