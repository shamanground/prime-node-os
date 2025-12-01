from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


def load_adapters(data_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Load adapters.yaml and return (step_sets, adapters).
    step_sets: name -> {steps: [...]}
    adapters:  context_key -> {use: step_set_name}
    """
    path = data_dir / "adapters.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    step_sets = data.get("step_sets", {}) or {}
    adapters = data.get("adapters", {}) or {}
    return step_sets, adapters


def resolve_steps(context_key: str, step_sets: Dict[str, Any], adapters: Dict[str, Any]) -> List[str]:
    """
    Given a context key like 'ai_drift_dx', return the list of steps defined
    in adapters.yaml. If not found, returns [].
    """
    cfg = adapters.get(context_key)
    if not cfg:
        return []
    use_name = cfg.get("use")
    if not use_name:
        return []
    steps_cfg = step_sets.get(use_name, {})
    return list(steps_cfg.get("steps", []))
