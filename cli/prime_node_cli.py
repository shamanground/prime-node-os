#!/usr/bin/env python3
# Prime Node OS — CLI Audit Runner
# Runs the unified fusion engine (Cold Mirror + Gate Routing + Threshold Logic)

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

# --- Import Prime Node Runtime ---
# expects: /mnt/data/engine/prime_node_runtime.py
ENGINE_PATH = Path("/mnt/data/engine/prime_node_runtime.py")

if not ENGINE_PATH.exists():
    print(f"[ERROR] Fusion engine not found at: {ENGINE_PATH}")
    sys.exit(1)

# dynamic import without disturbing path
import importlib.util
spec = importlib.util.spec_from_file_location("prime_node_runtime", ENGINE_PATH)
pn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pn)

# --- Import LLM Client ---
# You must have: /mnt/data/cold_mirror/engine/llm/openai_client.py
try:
    from cold_mirror.engine.llm.openai_client import OpenAIClient
except Exception:
    print("[ERROR] OpenAIClient not found. Provide your own LLMClient.")
    sys.exit(1)


def load_text_from_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"[ERROR] File not found: {path}")
        sys.exit(1)
    return p.read_text(encoding="utf-8", errors="replace")


def run_audit(text: str, model: str, api_key: str):
    llm = OpenAIClient(api_key=api_key, model=model)
    return pn.run_prime_node_audit(text, llm)


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="prime-node",
        description="Prime Node OS — Unified Audit CLI"
    )

    ap.add_argument(
        "--text",
        "-t",
        type=str,
        help="Raw text to audit"
    )

    ap.add_argument(
        "--file",
        "-f",
        type=str,
        help="Path to file containing text to audit"
    )

    ap.add_argument(
        "--model",
        "-m",
        type=str,
        default="gpt-4.1-mini",
        help="LLM model to use (default: gpt-4.1-mini)"
    )

    ap.add_argument(
        "--api_key",
        type=str,
        default=None,
        help="API key for the model backend"
    )

    ap.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print output instead of raw JSON"
    )

    args = ap.parse_args(argv)

    if not args.text and not args.file:
        print("[ERROR] Provide either --text or --file")
        sys.exit(1)

    if args.file:
        text = load_text_from_file(args.file)
    else:
        text = args.text

    api_key = args.api_key or ""
    if not api_key:
        print("[WARN] No API key provided — assuming OPENAI_API_KEY env var")

    # Run audit through fusion engine
    report = run_audit(text, args.model, api_key)

    # Output
    if args.pretty:
        print(json.dumps(report, indent=2))
    else:
        print(json.dumps(report))


if __name__ == "__main__":
    main()
