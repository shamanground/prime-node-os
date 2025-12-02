# Loop vs Replay Trap-Load Experiment
Prime Node OS · Cold Mirror Engine

This experiment measures how trap-load changes under three interaction modes:
**single**, **live_loop**, and **replay**.  
It is designed for falsifiability, reproducibility, and side-by-side comparison.

---

## Objective

To determine whether looped conversations with active gate policies introduce
measurable trap-load differences compared to:

1. **single** — one-shot model inference  
2. **live_loop** — full turn-by-turn inference with gate routing active  
3. **replay** — deterministic replay of the `live_loop` transcript with *no* gates

A divergence between **live_loop** and **replay** indicates:
- adaptation,
- drift,
- or loop-amplulated trap accumulation.

A convergence indicates:
- stable behavior,
- minimal gate-induced distortion,
- and predictable execution under replay.

---

## Inputs

This experiment uses real Cold Mirror data:

- `trap_seeds.yaml` — canonical 72-trap taxonomy  
- `thresholds_1.1.yaml` — scoring profiles and normalization  
- `segment_to_gates.yaml` — gate routing map  
- `runtime.yaml` and `Thoth_engine_1.0.yaml` — live engine config  
- Cold Mirror artifacts:
  - `intake.json`
  - `project_dump.txt`
  - `report.json` (or `.md`)

Each task is derived from a real intake + project_dump pair.

---

## Modes

### **1. single**
Runs the task as a single prompt.  
No turns, no gates, no correction flow.

### **2. live_loop**
Full Cold Mirror loop:
- segment parsing  
- gate policies  
- threshold shaping  
- model turn-by-turn  
- telemetry per turn  

This transcript becomes the source for replay.

### **3. replay**
Replays each human turn from the `live_loop` transcript:

- no gate routing  
- no harmonizers  
- no lunar nudges  
- no overrides  
- no correction logic  
- pure model autoregression  

Replay is the falsifier.

If loop behavior requires gate pressure to produce the same output, replay divergence will show it.

---

## Trap-Load Computation

Each run produces a trap-load vector:

```
{
  "Overreach": 0.14,
  "ScopeCreep": 0.07,
  "Collapse": 0.02,
  "Drift": 0.31,
  ...
}
```

Derived from:
- pattern matches in the model output  
- trap_id → family mapping  
- normalization via `thresholds_1.1.yaml`  

---

## Output Format

Results are written to:

```
experiments/results/loop_vs_replay.jsonl
```

Each line:

```json
{
  "task_id": "coldmirror_example_01",
  "model_name": "gpt-4.1",
  "gate_policy": "SVC-Standard",
  "run_type": "live_loop",
  "trap_family": "Overreach",
  "trap_score": 0.14,
  "timestamp": "2025-12-02T04:21:55Z"
}
```

This makes the experiment easy to graph, diff, or pass to external analyzers.

---

## Falsifier Condition

A loop-induced trap signature is confirmed if:

- **trap_load(live_loop)** ≠ **trap_load(replay)**  
  AND  
- replay receives *identical user turns*  
  AND  
- model + thresholds + trap seeds remain unchanged  

If loop and replay converge, then loop artifacts are not due to gate amplification.

---

## Directory Structure

```
experiments/
    loop_vs_replay.py
    loop_vs_replay.md
    results/
```

`loop_vs_replay.py` pulls the runtime, trap seeds, thresholds, and uses the
same inference pipeline as Cold Mirror.

---

## Why It Matters

This experiment exposes:

- whether gate functions create stabilizing or destabilizing pressure  
- whether drift is inherent or loop-amplified  
- whether replay can reproduce the loop behavior  
- whether your trap system behaves like a consistent metric or a dynamic field  
- whether Country’s hypothesis about loop-pressure holds  

It is the cleanest, smallest falsifier that still touches the full engine.

---

## Next Steps

- Add additional tasks beyond the initial Cold Mirror example  
- Compare multiple models for drift/convergence differences  
- Add variance tracking across N runs per mode  
- Use this harness to test future gate policies

