from __future__ import annotations
from typing import Dict

from ..core.seed_loader import Seed


def build_trap_analysis_prompt(
    text: str,
    seeds_by_id: Dict[str, Seed],
) -> str:
    """
    Build a prompt that gives the model your seed IDs + resonance signatures
    and asks it to return JSON with matches.
    """
    lines = []
    for seed in seeds_by_id.values():
        if not seed.resonance_signature:
            continue
        lines.append(f"- {seed.id}: {seed.title} — {seed.resonance_signature}")

    seeds_block = "\n".join(lines)

    return f"""
You are an audit agent called Cold Mirror.

You are given:
- A set of canonical resonance seeds (IDs, titles, and resonance signatures).
- A project description / AI usage scenario from the user.

Your job is to:
1. Read the user content.
2. Decide which seeds are active in this content.
3. Respond with **ONLY** valid JSON, with **no** backticks, no code fences, and no extra text.
4. Use exactly this JSON shape:

{{
  "matches": [
    {{
      "seed_id": "AR1",
      "confidence": 0.83,
      "evidence": "short quote or explanation from the user's text"
    }}
  ]
}}

Do not include any explanation outside this JSON object.
Do not wrap the JSON in ```json``` fences.
Do not add comments.

SEEDS:

{seeds_block}

USER CONTENT (truncated to 16k chars):

\"\"\"{text[:16000]}\"\"\"
""".strip()
