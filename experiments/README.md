# Prime Node OS — Experiments

This directory contains reproducible, runtime-aligned experiments designed to
test behavior inside the actual Prime Node OS engine. These are not standalone
scripts — every experiment here runs **through the same trap taxonomy, thresholds,
gate routing, and model client** used by Cold Mirror and the Thoth Engine.

## Purpose

Experiments here evaluate:
- trap-load behavior under different interaction patterns  
- loop vs replay divergence  
- threshold sensitivity  
- gate policy effects  
- drift vs convergence under controlled conditions  

All experiments are built for **falsifiability** and **repeatability**.  
They produce structured JSONL outputs that can be inspected, shared, or passed
into downstream analysis tools.

## Current Work

### Loop vs Replay Trap-Load Experiment
A small harness that runs a task in three modes:

1. **single** — one-shot model response  
2. **live_loop** — model called turn-by-turn with gate policies active  
3. **replay** — the live transcript replayed with no corrections and no adaptive gates  

Each mode emits a trap-load vector grouped by trap families using the
canonical `trap_seeds.yaml` and `thresholds_1.1.yaml`.

Results are written to:

```
results/loop_vs_replay.jsonl
```

with fields:

```
task_id
model_name
gate_policy
run_type
trap_family
trap_score
timestamp
```

## Requirements

- Prime Node OS runtime must be installed  
- `trap_seeds.yaml` and `thresholds_1.1.yaml` must be present  
- The OpenAI client or compatible client must be configured  

## Structure

```
experiments/
    loop_vs_replay.py      # experiment harness (coming next)
    README.md              # this file
    results/               # auto-generated outputs
```

## Philosophy

Experiments live **inside** Prime Node OS because reproducibility requires
running inside the same runtime that powers the engine.  
No external repos, no shadow environments.

If an experiment can’t pass inside the real system, it doesn’t count.

