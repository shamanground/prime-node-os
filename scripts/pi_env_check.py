#!/usr/bin/env python3
"""
Prime Node OS — Raspberry Pi environment check

Prints basic platform, CPU and RAM info so users can confirm
their box matches the v0 reference profile.
"""

from pathlib import Path
import platform


def print_header(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def check_platform() -> None:
    print_header("Platform")
    print("System :", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Python :", platform.python_version())


def check_cpu() -> None:
    cpuinfo = Path("/proc/cpuinfo")
    if not cpuinfo.exists():
        return

    print_header("CPU")
    model = None
    with cpuinfo.open() as f:
        for line in f:
            lower = line.lower()
            if lower.startswith("model name") or lower.startswith("hardware"):
                model = line.split(":", 1)[1].strip()
                break

    if model:
        print("Model:", model)


def check_ram() -> None:
    meminfo = Path("/proc/meminfo")
    if not meminfo.exists():
        return

    print_header("Memory")
    mem_total_kb = None
    for line in meminfo.read_text().splitlines():
        if line.startswith("MemTotal:"):
            parts = line.split()
            if len(parts) >= 2:
                mem_total_kb = int(parts[1])
                break

    if mem_total_kb:
        gb = mem_total_kb / 1024 / 1024
        print(f"Total RAM: {gb:.2f} GB")


def main() -> None:
    check_platform()
    check_cpu()
    check_ram()


if __name__ == "__main__":
    main()
