# Prime Node OS · v0 Lab Build

> Local-first AI runtime **scaffold** for sovereign nodes.  
> This is an early lab build, not a polished product.

Right now this repo gives you:

- A baseline folder tree for a node:
  - `engine/`, `runtime/`, `schemas/`, `memory/`, `thread/`, `logs/`, `scripts/`, `examples/`
- Environment check for target hardware (laptop / mini-PC / Pi):
  - `python scripts/pi_env_check.py`
- A bridge script that calls **Cold Mirror** as the first system agent:
  - `python scripts/run_cold_mirror_plan.py --project examples/test/project_dump.txt --intake examples/test/intake.json`

Prime Node OS is being built in the open.  
Right now this repo is a **reference scaffold** + scripts, not a full runtime.

## Status

- ✅ Folder structure + runtime seed (`scripts/init_prime_node.py`)
- ✅ Cold Mirror integration script (delegates to working Cold Mirror CLI engine)
- ✅ Tested end-to-end on a live server with a real `cold_mirror_run.json`
- 🚧 No full node orchestrator yet
- 🚧 No one-command installer
- 🚧 No multi-node / P2P logic yet

## Quick start (lab use)

Clone the repo:

```bash
git clone https://github.com/shamanground/prime-node-os.git
cd prime-node-os
---

## Why this exists

Right now “AI” mostly means asking a few big companies to think for you on their servers. They own the models, the logs, and eventually the narrative.

Prime Node OS is the opposite direction:

- **Local-first** – your hardware, your keys, your logs.
- **Trap-aware** – guardrails against scope creep, overreach, and “just one more feature” death spirals.
- **Bitcoin-funded** – built in a one-man lab, not steered by VC decks.
- **Mesh-ready** – v0 is a single sovereign node; later versions link those nodes into a peer-to-peer AI mesh.

This repo is the foundation for that first node.

---

## What v0 aims to ship

The initial public release (`v0`) is a **single-node reference build**:

- 🧠 **Local AI runtime**  
  Runs on a laptop, mini-PC, Raspberry Pi, or home server.

- 🛡 **Trap-aware gates**  
  Request/response filters that catch Overreach, Time Slip, Scope Creep and other builder traps before they become habits.

- 🔍 **Cold Mirror as first audit agent**  
  Blunt, text-based audits of your plans vs your calendar: what you *say* you'll ship vs what actually fits.

- 📚 **Clean install path + docs**  
  Step-by-step setup, config examples, and a single-node example you can fork.

- 🔌 **Room for your agents**  
  A clear place to plug in your own tools and workflows as additional agents.

---

## Repository layout (current)

As `v0` comes together, this repo will grow. For now:

- `docs/` – design notes, architecture sketches, and early user docs for the runtime.  
- `examples/` *(planned)* – example layouts for common environments (laptop, mini-PC, Pi, home server).  
- `runtime/` *(planned)* – reference implementation of the node runtime and agent wiring.  

If a folder isn’t here yet, it just means it hasn’t shipped. No smoke and mirrors.

---

## Roadmap

**Short term (this goal):**

1. Finalize single-node architecture and config format.  
2. Ship `v0` reference runtime with Cold Mirror wired in as the first audit agent.  
3. Provide install docs and one working example for a typical builder machine.

**Next steps (after v0):**

- Add more audit / orchestration agents on top of the same runtime.  
- Begin **node-to-node sync** experiments (sharing vectors, tags, and behavior deltas over encrypted channels).  
- Explore **phone “neurons”** that sync back to a home / lab node.  
- Design the primitives for a **Bitcoin-backed AI mesh** (discovery, reputation, payments).

---

## Who this is for

- Indie builders who want **their own node**, not just another SaaS account.  
- Bitcoiners and cypherpunks who actually run their own infrastructure.  
- Small labs, shops, classrooms and collectives that need **local-first AI** with clear boundaries.

If that’s you, you’re the target user.

---

## Contributing

Right now the focus is:

- Tightening the architecture for `v0`
- Writing clear docs and examples
- Hardening the trap-aware gates and Cold Mirror integration

If you’re interested in contributing (code, docs, testing, or funding), open an issue or reach out via:

- GitHub Issues on this repo  
- Contact links on [shamanground.com](https://shamanground.com/) *(once live for Prime Node OS)*

---

## License

This project is released under the **MIT License**. See [`LICENSE`](./LICENSE) for details.
