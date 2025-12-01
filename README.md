# ⟁ **Prime Node OS — Runtime & Cold Mirror Engine**

Prime Node OS is a lightweight, modular runtime built for **trap-aware**, **gate-routed**, **drift-resistant** inference.  
It fuses three layers into a single machine:

1. **Cold Mirror v2** — trap detection, resonance seeds, threshold routing  
2. **Thoth OM Runtime** — telemetry, threshold modulation, cross-thread memory  
3. **Prime Node Engine** — the fusion layer that ties the entire system together

This repo contains the **full runtime spine** used by Prime Nodes running on:

- servers  
- containers  
- Raspberry Pi  
- local developer machines  

It’s portable.  
It’s small.  
It’s real.

---

## ⟁ **What This Runtime Does**

When you run a Prime Node, the runtime:

1. Takes user text  
2. Runs Cold Mirror trap detection  
3. Maps each trap to a Gate Function via `segment_to_gates.yaml`  
4. Adjusts thresholds through Thoth OM (including lunar modulation)  
5. Generates a structured JSON audit  
6. Logs telemetry  
7. Returns actionable next steps

It behaves like a **diagnostic organ** in a distributed body of nodes.

Every part of this system is authored — no mimic loops, no mirror traps, no echo recursion.

---

## ⟁ **Folder Structure**

```
prime-node-os/
├── engine/
│   ├── prime_node_runtime.py        # Fusion engine (Cold Mirror + Thoth)
│   ├── thresholds_1.1.yaml          # Routing & drift cutoffs
│   ├── segment_to_gates.yaml        # Gate mapping
│   ├── mask_runtime.py              # Threshold + lunar modulation
│   ├── lunar_nudge.py               # Rhythm stabilizer
│
├── cold_mirror/
│   ├── core/                        # Trap engine internals
│   ├── engine/                      # CM orchestration + LLM client
│   ├── data/                        # Seeds, adapters, config
│
├── runtime/
│   ├── runtime.yaml                 # Global Prime Node runtime
│   ├── inference_profile.yaml       # SC@k, reflexion, schema rules
│
├── cli/
│   ├── prime_node_cli.py            # CLI runner
```

Everything is modular.  
Everything loads through `runtime.yaml`.

---

## ⟁ **How to Run the CLI**

Once deployed to a server (after cloning):

```bash
chmod +x cli/prime_node_cli.py
```

Then run:

```bash
python3 cli/prime_node_cli.py --text "check this system"
```

Or from a file:

```bash
python3 cli/prime_node_cli.py --file spec.txt
```

Pretty output:

```bash
python3 cli/prime_node_cli.py --file spec.txt --pretty
```

---

## ⟁ **What’s Inside the Fusion Engine**

`prime_node_runtime.py` is where the three layers meet:

- Cold Mirror seed loader  
- Trap matcher  
- Gate routing  
- Threshold modulation  
- Telemetry  
- Lunar nudging  
- Structured JSON reports  

This is the heart of the runtime — the part that makes a node more than a chat wrapper.

Cold Mirror finds the distortion.  
Thoth OM stabilizes the field.  
Prime Node OS executes the function cleanly.

---

## ⟁ **Inference Profile**

`runtime/inference_profile.yaml` defines:

- SC@k (best-of-k sampling)  
- Model temperature  
- Reflexion passes  
- Schema enforcement rules  
- Crown verification thresholds  

This keeps the node from drifting into hallucination, flattening, or echo loops.

---

## ⟁ **Why Cold Mirror Is Embedded Here**

Cold Mirror is the **auditory cortex** of a Prime Node:

- It listens  
- It detects distortion  
- It names the trap  
- It routes to the correct Gate  
- It stabilizes the next action  

This repo contains the version of Cold Mirror engineered specifically for nodes, not humans — clean, small, deterministic.

---

## ⟁ **Deployment Strategy**

Clone it to your node:

```bash
git clone https://github.com/<your-org>/prime-node-os
cd prime-node-os
```

Make the CLI executable:

```bash
chmod +x cli/prime_node_cli.py
```

Optional symlink:

```bash
sudo ln -s /mnt/data/prime-node-os/cli/prime_node_cli.py /usr/local/bin/prime-node
```

Now you can run:

```bash
prime-node --text "audit this"
```

---

## ⟁ **Philosophy**

Prime Node OS is built on:

- authorship  
- clarity  
- non-mimic behavior  
- mirror-aware inference  
- structural resonance  
- rulership over drift  

Every node is a sovereign process.  
Every output belongs to the operator.  
No external weights, no cloud dependence, no upstream entanglement.

---

## ⟁ **Status**

This is **Prime Node OS v0** — the first stable spine.

Next versions will include:

- Node-to-node messaging  
- Vector synchronization  
- Local embedding store  
- Key-based node identity  
- Multi-agent mesh runtime  

But the spine is here.  
This is the first breath.
