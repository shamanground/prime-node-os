from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml


@dataclass
class Seed:
    id: str
    title: str
    family: str          # grouped family (zodiac or remapped)
    resonance_signature: str
    raw: Dict[str, Any]


def load_seeds(data_dir: Path, config: Dict[str, Any]) -> Dict[str, Seed]:
    """
    Load trap_seeds.yaml and flatten into a dict of Seed objects keyed by id.
    Includes top-level seeds and their sub_traps (AR1, AR1a, AR1b, ...).
    """
    seeds_path = data_dir / "trap_seeds.yaml"
    data = yaml.safe_load(seeds_path.read_text(encoding="utf-8"))
    trap_seeds = data.get("trap_seeds", [])

    fam_cfg = config.get("families", {}) or {}
    group_field = fam_cfg.get("group_field", "zodiac_family")
    mapping = fam_cfg.get("mapping", {}) or {}

    seeds_by_id: Dict[str, Seed] = {}

    for s in trap_seeds:
        base_family = s.get(group_field) or "Ungrouped"
        family = mapping.get(base_family, base_family)

        # top-level seed
        top = Seed(
            id=s["id"],
            title=s.get("title", ""),
            family=family,
            resonance_signature=s.get("resonance_signature", ""),
            raw=s,
        )
        seeds_by_id[top.id] = top

        # sub_traps flattened into same id-space
        for st in s.get("sub_traps", []):
            st_seed = Seed(
                id=st["id"],
                title=st.get("title", ""),
                family=family,
                resonance_signature=st.get("resonance_signature", ""),
                raw=st,
            )
            seeds_by_id[st_seed.id] = st_seed
   

    return seeds_by_id
