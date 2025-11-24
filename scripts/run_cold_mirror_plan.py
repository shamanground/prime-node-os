#!/usr/bin/env python3
"""
Prime Node OS — Cold Mirror bridge helper

Usage:
  python scripts/run_cold_mirror_plan.py --project path/to/project_dump.txt --intake path/to/intake.json

This is a thin wrapper around:
  python -m cold_mirror.cli.wizard --project ... --intake ...
"""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Cold Mirror wizard from Prime Node OS.")
    parser.add_argument(
        "--project",
        required=True,
        help="Path to project dump text file.",
    )
    parser.add_argument(
        "--intake",
        required=True,
        help="Path to intake JSON file.",
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        help="Python executable to use (default: this interpreter).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    project = Path(args.project).expanduser().resolve()
    intake = Path(args.intake).expanduser().resolve()

    if not project.exists():
        print(f"[error] project file not found: {project}", file=sys.stderr)
        sys.exit(1)

    if not intake.exists():
        print(f"[error] intake file not found: {intake}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        args.python,
        "-m",
        "cold_mirror.cli.wizard",
        "--project",
        str(project),
        "--intake",
        str(intake),
    ]

    print(">>> Running:", " ".join(cmd))
    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"[error] Cold Mirror exited with code {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    print(">>> Cold Mirror wizard completed.")


if __name__ == "__main__":
    main()
