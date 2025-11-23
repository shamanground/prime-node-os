# prime-node-os

**Prime Node OS** is a local-first AI runtime for sovereign users.

Run your own AI stack on a laptop, mini-PC, or home server – **no SaaS lock-in, no rented brain**. Prime Node OS puts trap-aware gates and audit agents in front of your model so you keep control of your compute, your data, and your roadmap.

> **Status:** Early R&D / pre-v0. This repo currently holds docs, design notes, and example layouts for the first single-node release.

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
