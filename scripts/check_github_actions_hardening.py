"""Validate GitHub Actions workflow hardening baseline."""

from __future__ import annotations

from pathlib import Path
import argparse
import re


DISALLOWED_PATTERNS = [
    r"\bpull_request_target\b",
    r"permissions:\s*write-all",
    r"permissions:\s*\{\s*\}",
]

PLACEHOLDER_PATTERNS = [
    r"run:\s*echo\s+['\"]TODO['\"]",
    r"^\s*placeholder:\s*$",
]


def check_workflow_hardening(workflow_files: list[Path]) -> list[str]:
    failures: list[str] = []
    if not workflow_files:
        failures.append("No workflow files found.")
        return failures

    for wf in workflow_files:
        text = wf.read_text(encoding="utf-8")
        if "permissions:" not in text:
            failures.append(f"{wf.as_posix()}: missing top-level permissions block")

        for pattern in DISALLOWED_PATTERNS:
            if re.search(pattern, text):
                failures.append(f"{wf.as_posix()}: matched disallowed pattern `{pattern}`")

        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, text, flags=re.MULTILINE):
                failures.append(f"{wf.as_posix()}: matched placeholder pattern `{pattern}`")

    return failures


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workflow-dir",
        default=".github/workflows",
        help="Directory containing workflow *.yml files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workflow_dir = Path(args.workflow_dir)
    files = sorted(workflow_dir.glob("*.yml"))
    failures = check_workflow_hardening(files)
    if failures:
        raise SystemExit("Hardening gate failed:\n- " + "\n- ".join(failures))
    print("Workflow hardening baseline passed.")


if __name__ == "__main__":
    main()
