#!/usr/bin/env python3
"""
Prime Node OS — Cold Mirror bridge helper (auto-discovery, runtime-first)

This script:
  - Starts from the parent folder of prime-node-os (ShamanGround)
  - Searches for files named 'cold_mirror.py'
  - PREFERS ones whose parent folder is 'runtime' (i.e. runtime/cold_mirror.py)
  - Runs that script with --project and --intake

Usage (from prime-node-os root):

  python scripts/run_cold_mirror_plan.py --project examples/test/project_dump.txt --intake examples/test/intake.json
"""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]  # prime-node-os root
BASE = ROOT.parent  # ShamanGround folder


def find_cold_mirror_script() -> Path | None:
    """
    Look for cold_mirror.py anywhere under BASE.
    Prefer paths where parent folder is 'runtime'.
    """
    all_hits = list(BASE.rglob("cold_mirror.py"))
    if not all_hits:
        return None

    runtime_hits = [p for p in all_hits if p.parent.name == "runtime"]

    if runtime_hits:
        # deterministic order just to be safe
        runtime_hits.sort(key=lambda p: str(p))
        return runtime_hits[0]

    # fallback: anything else
    all_hits.sort(key=lambda p: str(p))
    return all_hits[0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Cold Mirror from Prime Node OS.")
    parser.add_argument(
        "--project",
        required=True,
        help="Path to project dump text file (relative to prime-node-os root or absolute).",
    )
    parser.add_argument(
        "--intake",
        required=True,
        help="Path to intake JSON file (relative to prime-node-os root or absolute).",
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        help="Python executable to use (default: this interpreter).",
    )
    return parser.parse_args()


def main() -> None:
    cm_script = find_cold_mirror_script()
    if cm_script is None:
        print("[error] Could not find any cold_mirror.py under:")
        print(f"        {BASE}")
        print("Make sure your Cold Mirror repo (cold_mirror_v2) is under this folder.")
        sys.exit(1)

    args = parse_args()

    project = Path(args.project).expanduser()
    if not project.is_absolute():
        project = ROOT / project
    project = project.resolve()

    intake = Path(args.intake).expanduser()
    if not intake.is_absolute():
        intake = ROOT / intake
    intake = intake.resolve()

    if not project.exists():
        print(f"[error] project file not found: {project}", file=sys.stderr)
        sys.exit(1)

    if not intake.exists():
        print(f"[error] intake file not found: {intake}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        args.python,
        str(cm_script),
        "--project",
        str(project),
        "--intake",
        str(intake),
    ]

    print(">>> Using Cold Mirror script at:", cm_script)
    print(">>> Running:", " ".join(cmd))
    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"[error] Cold Mirror exited with code {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)

    print(">>> Cold Mirror run completed.")


if __name__ == "__main__":
    main()
