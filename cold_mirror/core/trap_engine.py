from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def log_run(report: Dict[str, Any], config: Dict[str, Any], data_dir: Path) -> None:
    """
    Local hive ledger: each run logs which families fired.
    No network calls, no phoning home. Purely local.
    """
    report_cfg = config.get("report", {}) or {}
    if not report_cfg.get("log_telemetry", True):
        return

    ledger_name = report_cfg.get("telemetry_file", "cold_mirror_ledger.jsonl")
    ledger_path = data_dir / ledger_name

    families = report.get("families", [])
    top_family = families[0]["family"] if families else None

    rec: Dict[str, Any] = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_seed_hits": report.get("summary", {}).get("total_seed_hits", 0),
        "families_hit": [f["family"] for f in families],
        "top_family": top_family,
    }

    with ledger_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
