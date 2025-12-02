#!/usr/bin/env python3
"""
Loop vs Replay Trap-Load Experiment
Prime Node OS — Cold Mirror Engine Integration

This experiment compares trap-load signatures between:
1. single     (one audit run)
2. live_loop  (identical to single — Cold Mirror is one-shot)
3. replay     (re-run audit with same prompt)

Detects drift, randomness, instability, and trap-set divergence.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime

# Cold Mirror imports
from cold_mirror.engine.cold_mirror_engine import run_audit
from cold_mirror.llm.openai_client import OpenAILLMClient

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / "engine"
EXPERIMENTS = ROOT / "experiments"

TRAP_SEEDS_PATH = ENGINE / "trap_seeds.yaml"
THRESHOLDS_PATH = ENGINE / "thresholds_1.1.yaml"


# ---------------------------------------------------------
# Load Trap Seeds + Thresholds
# ---------------------------------------------------------

def load_trap_families():
    data = yaml.safe_load(TRAP_SEEDS_PATH.read_text())
    families = {}

    for fam in data.get("trap_families", []):
        name = fam["family"]
        patterns = []
        for t in fam.get("traps", []):
            patterns.append(t.get("pattern", "").lower())
        families[name] = patterns

    return families


def load_thresholds():
    return yaml.safe_load(THRESHOLDS_PATH.read_text())


# ---------------------------------------------------------
# Trap-Load Scoring (Pattern Based)
# ---------------------------------------------------------

def score_trap_load(text: str, trap_families: dict) -> dict:
    text_lower = text.lower()
    scores = {fam: 0 for fam in trap_families.keys()}

    for fam, patterns in trap_families.items():
        for pattern in patterns:
            if pattern and pattern in text_lower:
                scores[fam] += 1

    return scores


# ---------------------------------------------------------
# Run modes
# ---------------------------------------------------------

def run_single(text: str, client):
    report = run_audit(text, client)
    return report["text"] if "text" in report else str(report)


def run_live_loop(text: str, client):
    # Cold Mirror is one-shot.
    # "Live loop" = same call as single.
    return run_single(text, client)


def run_replay(text: str, client):
    # Replay = run audit again with identical input.
    return run_single(text, client)


# ---------------------------------------------------------
# Write JSONL Results
# ---------------------------------------------------------

def write_result(task_id, run_type, scores):
    results_dir = EXPERIMENTS / "results"
    results_dir.mkdir(exist_ok=True)

    out_file = results_dir / "loop_vs_replay.jsonl"

    rec = {
        "task_id": task_id,
        "run_type": run_type,
        "trap_load": scores,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    with open(out_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def main():
    import argparse

    ap = argparse.ArgumentParser(description="Loop vs Replay Trap-Load Experiment")
    ap.add_argument("--intake", required=True, help="Path to intake.json")
    args = ap.parse_args()

    intake_text = Path(args.intake).read_text()

    task_id = Path(args.intake).stem

    client = OpenAILLMClient(model="gpt-4.1-mini")

    # Load trap seeds
    trap_families = load_trap_families()

    # SINGLE
    out_single = run_single(intake_text, client)
    scores_single = score_trap_load(out_single, trap_families)
    write_result(task_id, "single", scores_single)

    # LIVE LOOP
    out_live = run_live_loop(intake_text, client)
    scores_live = score_trap_load(out_live, trap_families)
    write_result(task_id, "live_loop", scores_live)

    # REPLAY
    out_replay = run_replay(intake_text, client)
    scores_replay = score_trap_load(out_replay, trap_families)
    write_result(task_id, "replay", scores_replay)

    print("✓ Loop vs Replay experiment completed.")
    print(f"Results saved to: {EXPERIMENTS / 'results' / 'loop_vs_replay.jsonl'}")


if __name__ == "__main__":
    main()
