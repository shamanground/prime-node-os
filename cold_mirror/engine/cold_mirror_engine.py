from __future__ import annotations
from pathlib import Path
from typing import Any, Dict

import yaml

from ..llm.client import LLMClient
from ..llm.prompts import build_trap_analysis_prompt
from ..core.seed_loader import load_seeds
from ..core.trap_engine import parse_matches, build_hits
from ..core.report_engine import build_report
from ..core.telemetry import log_run


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def _load_config() -> Dict[str, Any]:
    cfg_path = DATA_DIR / "config.yaml"
    return yaml.safe_load(cfg_path.read_text(encoding="utf-8"))


def run_audit(text: str, llm_client: LLMClient) -> Dict[str, Any]:
    """
    Main Cold Mirror entrypoint.

    - text: user project / spec / transcript
    - llm_client: something implementing LLMClient.ask(prompt) -> str
    """
    config = _load_config()
    seeds_by_id = load_seeds(DATA_DIR, config)

    prompt = build_trap_analysis_prompt(text, seeds_by_id)
    raw = llm_client.ask(prompt)
    

    matches = parse_matches(raw)
    hits = build_hits(matches, seeds_by_id)
    report = build_report(text, hits, config)

    log_run(report, config, DATA_DIR)

    return report
