
# Prime Node OS · v0 Lab Build

> Local-first AI runtime **scaffold** for sovereign nodes.  
> Cold Mirror wired in as the first system agent. Early, experimental, not production-ready.

Right now this repo gives you:

- A baseline folder tree for a node:
  - `engine/`, `runtime/`, `schemas/`, `memory/`, `thread/`, `logs/`, `scripts/`, `examples/`
- Environment check for target hardware (laptop / mini-PC / Pi / Raspberry Pi):
  - `python scripts/pi_env_check.py`
- A bridge script that calls **Cold Mirror** as the first system agent:
  - `python scripts/run_cold_mirror_plan.py --project examples/test/project_dump.txt --intake examples/test/intake.json`

Prime Node OS is being built in the open.  
Right now this repo is a **reference scaffold** + scripts, not a full runtime.

---

## Status

- ✅ Folder structure + runtime seed (`scripts/init_prime_node.py`)
- ✅ Cold Mirror integration script (delegates to working Cold Mirror CLI engine)
- ✅ Tested end-to-end on a live server with a real `cold_mirror_run.json`
- 🚧 No full node orchestrator yet
- 🚧 No one-command installer yet
- 🚧 No multi-node / P2P logic yet

---

## Repository Layout (v0)

```text
prime-node-os/
  docs/
    overview.md              # high-level notes about Prime Node OS
  engine/                    # future orchestrator + node logic
  examples/
    single_node_example/
      README.md              # example walkthrough (to be expanded)
    test/
      project_dump.txt       # example project description for Cold Mirror
      intake.json            # example intake schema for Cold Mirror
  logs/
  memory/
  runtime/
    runtime.yaml             # starter runtime config (lab use)
  schemas/
  scripts/
    init_prime_node.py       # seeds folders + runtime.yaml
    pi_env_check.py          # prints host env info for Pi / mini-PC
    run_cold_mirror_plan.py  # calls Cold Mirror CLI, saves run JSON
  thread/
  .gitignore
  LICENSE
  README.md
```

---

## Quick Start (Lab Use)

### 1. Clone the repo

```bash
git clone https://github.com/shamanground/prime-node-os.git
cd prime-node-os
```

### 2. Seed the folders

Safe to run more than once:

```bash
python scripts/init_prime_node.py
```

This will make sure the baseline folders exist and that `runtime/runtime.yaml` is present.

### 3. Check your environment

This is mostly for logging + Pi/mini-PC targeting:

```bash
python scripts/pi_env_check.py
```

You’ll see basic OS + Python info printed to the console.

---

## Wiring in Cold Mirror (Local Integration)

Prime Node OS v0 uses **Cold Mirror** as the first system agent.  
The `run_cold_mirror_plan.py` script expects this layout on your machine:

```text
ShamanGround/
  cold_mirror_v2/            # Cold Mirror CLI engine (separate repo)
  prime-node-os/             # this repo
```

Inside `cold_mirror_v2` you should have a working Cold Mirror install that can be run like:

```bash
python -m cold_mirror.cli.main --help
```

If that works, you can run the bridge script from inside `prime-node-os`:

```bash
cd prime-node-os

python scripts/run_cold_mirror_plan.py   --project examples/test/project_dump.txt   --intake examples/test/intake.json
```

If everything is wired correctly, you’ll see output similar to:

```text
>>> Using Cold Mirror script at: /path/to/cold_mirror_v2/cold_mirror.py
>>> Running: python /path/to/cold_mirror_v2/cold_mirror.py --file ...
>>> Cold Mirror wizard completed.
```

And a file like this will appear:

```text
prime-node-os/
  cold_mirror_run.json
```

That JSON contains:

- Trap hits by family (e.g., Overreach Trap, Time Slip Trap)
- Evidence snippets from your project description
- A 24h / 7d / 30d shipping plan based on your intake

You can feed that into other tools, dashboards, or your own agents.

---

## Notes on Cold Mirror Itself

This repo does **not** contain the full Cold Mirror engine.  
For that, see the separate Cold Mirror repository and documentation.

Prime Node OS just assumes:

- You have a working Cold Mirror CLI engine in `../cold_mirror_v2/`
- Your engine is configured with:
  - A valid `OPENAI_API_KEY` in the environment (or equivalent model setup)
  - The usual Cold Mirror trap datasets + YAML config

If you can run Cold Mirror directly from its own repo, the integration here should work.

---

## Roadmap (High-Level)

Prime Node OS v0 is intentionally narrow:

1. **Single Node Runtime (lab build)**
   - Clean folder + config structure for a sovereign AI node
   - One working system agent (Cold Mirror) wired in via scripts
   - Clear pattern for adding more agents over time

2. **Orchestrator + CLI**
   - Node-level process that owns:
     - intake → agent selection → output routing
     - simple logging + memory hooks
   - CLI commands for common flows:
     - `prime-node audit` (Cold Mirror)
     - `prime-node run` (future agents)

3. **Multi-Node / P2P (Future)**
   - Experiments in:
     - Nodes sharing vector signals and tags
     - Phones / small devices as roaming neurons
     - Home servers as somas coordinating long arcs

None of that is promised in this v0 lab build.  
This repo is the **starting point**.

---

## Contributing / Feedback

Right now this is a one-man lab project. If you want to help:

- Open issues or PRs on:
  - Folder structure
  - Script ergonomics
  - Docs and examples
- Run the Cold Mirror bridge on your own project and share:
  - What worked
  - Where it broke
  - What you’d want from a real v0 runtime

---

## License

This project is released under the MIT License. See `LICENSE` for details.
