#!/usr/bin/env python3
"""
Loop vs Replay Trap-Load Experiment (Skeleton)
Prime Node OS — Cold Mirror Runtime Integration

This script defines:
- run_single
- run_live_loop
- run_replay
- score_trap_load
- CLI entrypoint

The real implementation will hook into:
- trap_seeds.yaml
- thresholds_1.1.yaml
- runtime loader (thoth_loader)
- model client used by Cold Mirror
"""

import json
import yaml
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]     # prime-node-os/
ENGINE = ROOT / "engine"
RUNTIME = ROOT / "runtime"
EXPERIMENTS = ROOT / "experiments"

TRAP_SEEDS_PATH = ENGINE / "trap_seeds.yaml"
THRESHOLDS_PATH = ENGINE / "thresholds_1.1.yaml"

# ---------------------------------------------------------------------------
# Load trap seeds + thresholds
# ---------------------------------------------------------------------------

def load_trap_seeds():
    """Load the 72 trap taxonomy from trap_seeds.yaml."""
    data = yaml.safe_load(TRAP_SEEDS_PATH.read_text())
    index = {}

    for fam in data.get("trap_families", []):
        fam_name = fam["family"]
        fam_id = fam["id"]

        for t in fam.get("traps", []):
            index[t["id"]] = {
                "family": fam_name,
                "family_id": fam_id,
                "trap": t["name"],
                "pattern": t.get("pattern", "")
            }

    return index


def load_thresholds():
    """Load normalization + scoring thresholds."""
    return yaml.safe_load(THRESHOLDS_PATH.read_text())

# ---------------------------------------------------------------------------
# Stub: model client + runtime loader hooks
# ---------------------------------------------------------------------------

def load_runtime_client():
    """
    Placeholder:
    Will import your actual model client from cold_mirror/thin_client.py
    or the Thoth loader.
    """
    return None  # will be replaced later

# ---------------------------------------------------------------------------
# Scoring skeleton
# ---------------------------------------------------------------------------

def score_trap_load(output_text, trap_index, thresholds):
    """
    Stub scoring function.
    Returns a fake structure for now so the experiment runs.
    """

    # TODO: integrate real Cold Mirror trap scoring
    return {
        "Overreach": 0.0,
        "Collapse": 0.0,
        "Drift": 0.0,
    }

# ---------------------------------------------------------------------------
# Run-type skeletons
# ---------------------------------------------------------------------------

def run_single(task):
    """
    One-shot run (no loops, no gate routing).
    """
    # TODO: call your model client with a single prompt
    model_output = "[single-mode output placeholder]"
    return model_output


def run_live_loop(task):
    """
    Full looped inference using SVC-style gate execution.
    """
    # TODO: pull in segment_to_gates + runtime logic
    transcript = []
    transcript.append("[live_loop turn 1 placeholder]")
    transcript.append("[live_loop turn 2 placeholder]")
    return transcript


def run_replay(task, transcript):
    """
    Reproduce the live transcript with no gate effects.
    """
    # TODO: call model turn-by-turn with no routing
    replay_output = []
    for t in transcript:
        replay_output.append(f"[replay placeholder for: {t}]")
    return replay_output

# ---------------------------------------------------------------------------
# Results writer
# ---------------------------------------------------------------------------

def write_results(task_id, run_type, scores):
    results_path = EXPERIMENTS / "results"
    results_path.mkdir(exist_ok=True)

    out_path = results_path / "loop_vs_replay.jsonl"
    rec = {
        "task_id": task_id,
        "run_type": run_type,
        "scores": scores,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    with out_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")

# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def main():
    import argparse

    ap = argparse.ArgumentParser(description="Loop vs Replay Experiment (Skeleton)")
    ap.add_argument("--intake", required=True, help="Path to intake.json")
    args = ap.parse_args()

    task_id = Path(args.intake).stem
    task = json.loads(Path(args.intake).read_text())

    trap_index = load_trap_seeds()
    thresholds = load_thresholds()

    # --- single
    single_out = run_single(task)
    single_score = score_trap_load(single_out, trap_index, thresholds)
    write_results(task_id, "single", single_score)

    # --- live loop
    loop_transcript = run_live_loop(task)
    loop_score = score_trap_load("\n".join(loop_transcript), trap_index, thresholds)
    write_results(task_id, "live_loop", loop_score)

    # --- replay
    replay_output = run_replay(task, loop_transcript)
    replay_score = score_trap_load("\n".join(replay_output), trap_index, thresholds)
    write_results(task_id, "replay", replay_score)

    print("✓ Experiment complete. Results written to experiments/results/loop_vs_replay.jsonl")


if __name__ == "__main__":
    main()
