from __future__ import annotations
from collections import defaultdict
from typing import Any, Dict, List


def build_report(
    raw_text: str,
    hits: List[Dict[str, Any]],
    config: Dict[str, Any],
) -> Dict[str, Any]:
    max_per_family = int(
        config.get("report", {}).get("max_seeds_per_family", 5)
    )

    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for h in hits:
        grouped[h["family"]].append(h)

    # sort + cap per family
    families = []
    for fam, items in grouped.items():
        items_sorted = sorted(
            items, key=lambda x: x.get("confidence", 0.0), reverse=True
        )[:max_per_family]
        families.append(
            {
                "family": fam,
                "hits": items_sorted,
            }
        )

    # order families by strongest hit
    families.sort(
        key=lambda f: max((h["confidence"] for h in f["hits"]), default=0.0),
        reverse=True,
    )

    summary = {
        "total_seed_hits": len(hits),
        "families_hit": [f["family"] for f in families],
    }

    return {
        "summary": summary,
        "families": families,
        "raw_text": raw_text,
    }
