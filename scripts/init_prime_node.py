#!/usr/bin/env python3
"""
Prime Node OS — v0 initializer

- Creates baseline folders: engine/, runtime/, scripts/, schemas/, memory/, thread/, logs/
- Seeds a minimal runtime/runtime.yaml if missing
- Seeds a simple .gitignore if missing
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRS = [
    "engine",
    "runtime",
    "scripts",
    "schemas",
    "memory",
    "thread",
    "logs",
]


def ensure_dirs() -> None:
    for d in DIRS:
        p = ROOT / d
        p.mkdir(parents=True, exist_ok=True)


def seed_runtime_config() -> None:
    cfg = ROOT / "runtime" / "runtime.yaml"
    if cfg.exists():
        return

    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(
        """# Prime Node OS v0 runtime config
version: "0.0.1"

node:
  role: "single-node"
  platform: "raspberry-pi"

telemetry:
  enabled: true
  file: "logs/telemetry.log"

cold_mirror:
  enabled: true
  mode: "cli"
  # path can be 'python -m cold_mirror.cli.wizard' or your own wrapper
  command: "python -m cold_mirror.cli.wizard"
"""
    )


def seed_gitignore() -> None:
    gi = ROOT / ".gitignore"
    if gi.exists():
        return

    gi.write_text(
        "\n".join(
            [
                "# Prime Node OS",
                "logs/",
                "__pycache__/",
                ".env",
                "*.pyc",
                ".DS_Store",
            ]
        )
        + "\n"
    )


def main() -> None:
    print(">>> Initializing Prime Node OS v0 skeleton at", ROOT)
    ensure_dirs()
    seed_runtime_config()
    seed_gitignore()
    print(">>> Done.")


if __name__ == "__main__":
    main()