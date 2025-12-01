from __future__ import annotations
from pathlib import Path
import yaml
import json

# --- Cold Mirror Core ---
from cold_mirror.core.seed_loader import load_seeds
from cold_mirror.core.trap_engine import parse_matches, build_hits
from cold_mirror.core.report_engine import build_report
from cold_mirror.core.adapters_engine import resolve_steps, load_adapters
from cold_mirror.core.telemetry import log_run

# --- Thoth OM Runtime ---
from engine.mask_runtime import adjust_thresholds_with_lunar
from engine.mask_runtime import finish_turn   # telemetry

ROOT = Path("/mnt/data")
CM_DIR = ROOT / "cold_mirror"
DATA_DIR = CM_DIR / "data"

# -----------------------
# Load base configs
# -----------------------
def load_config():
    return yaml.safe_load((DATA_DIR / "config.yaml").read_text(encoding="utf-8"))

def load_thresholds():
    thr_path = ROOT / "engine" / "thresholds_1.1.yaml"
    return yaml.safe_load(thr_path.read_text(encoding="utf-8"))


# -----------------------
# Gate Routing Logic
# -----------------------
def load_segment_map():
    p = ROOT / "engine" / "segment_to_gates.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def route_hits_to_gates(hits, segment_map):
    """
    hits: list of CM hits → each with (seed_id, title, family, confidence)
    segment_map: mapping for Problem/Audience/... to GateName
    """
    routed = []
    for h in hits:
        fam = h.get("family")
        gate = segment_map.get(fam) or segment_map.get(h.get("family"))
        routed.append({**h, "gate": gate})
    return routed


# -----------------------
# Unified Audit Entry Point
# -----------------------
def run_prime_node_audit(text: str, llm_client):
    config = load_config()
    thresholds = load_thresholds()
    segment_map = load_segment_map()

    # 1. Load seeds
    seeds_by_id = load_seeds(DATA_DIR, config)

    # 2. Build CM prompt + ask model
    from cold_mirror.llm.prompts import build_trap_analysis_prompt
    prompt = build_trap_analysis_prompt(text, seeds_by_id)
    raw = llm_client.ask(prompt)

    # 3. Parse + build hits
    matches = parse_matches(raw)
    hits = build_hits(matches, seeds_by_id)

    # 4. Gate routing
    routed_hits = route_hits_to_gates(hits, segment_map)

    # 5. Thoth OM threshold modulation (includes lunar nudges)
    adj_thresholds = adjust_thresholds_with_lunar(thresholds)

    # 6. Build CM report
    report = build_report(text, hits, config)
    report["gated_hits"] = routed_hits
    report["thresholds_used"] = adj_thresholds

    # 7. Telemetry
    log_run(report, config, DATA_DIR)
    finish_turn(
        coherence=1.0,               # placeholder until model scoring
        mirror_residual=len(hits),   # crude metric, can refine later
        samples=1
    )

    return report
