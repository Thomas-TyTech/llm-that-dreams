# LLM Daydreaming Prototype

This repository implements a working scaffold for the "day-dreaming loop" (DDL) hypothesis described in the accompanying essay. The goal is to give large language models a persistent background process for speculative synthesis, mirroring the human default-mode network.

## Components

- **Memory store** (`daydreamer.memory.MemoryStore`): persistent knowledge base that tracks concepts and generated ideas.
- **Generator** (`daydreamer.generator.IdeaGenerator`): prompts an LLM to explore surprising connections between concept pairs.
- **Critic** (`daydreamer.critic.IdeaCritic`): filters generated ideas by scoring novelty, coherence, and usefulness.
- **Loop orchestrator** (`daydreamer.loop.DaydreamingLoop`): continuously samples concepts, generates candidate ideas, and feeds accepted discoveries back into memory, creating a compounding feedback cycle.

The orchestration matches the DDL proposal:

1. Sample two concepts from memory.
2. Ask a generator model to synthesize an imaginative hypothesis relating them.
3. Ask a critic model to evaluate the synthesis using a rubric.
4. If the idea exceeds configured thresholds, store it as a new memory item so that future loops can combine it with other concepts.

The loop can run indefinitely in the background and the thresholds create a controllable "daydreaming tax"—higher thresholds yield fewer but more curated ideas.

## Quickstart

```bash
pip install -e .[dev]
python daydream.py --iterations 3
```

The CLI seeds an initial set of concepts and uses a deterministic mock LLM so it can run offline. To run against Anthropic's Claude models, install the package with the base extras, export an API key, and pass the desired model name:

```bash
pip install -e .
export ANTHROPIC_API_KEY=sk-ant-...
python daydream.py --iterations 3 --anthropic-model claude-3-haiku-20240307
```

You can optionally provide `--anthropic-system-prompt` to set a global system message.

All generated ideas are appended to the memory store (default `memory.json`). They become eligible for future pairings, enabling the recombinatorial dynamics described in the paper.

## Testing

```bash
pytest
```

This suite exercises the core loop with a scripted LLM to verify that accepted ideas are persisted.
