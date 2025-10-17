from __future__ import annotations

import json

from daydreamer import DaydreamConfig, DaydreamingLoop, IdeaCritic, IdeaGenerator, MemoryStore
from daydreamer.llm import LLMClient, LLMRequest, LLMResponse


class FixedLLM(LLMClient):
    def __init__(self) -> None:
        self.calls: list[str] = []

    def generate(self, request: LLMRequest) -> LLMResponse:
        self.calls.append(request.prompt)
        if "Evaluate the following hypothesis" in request.prompt:
            payload = {
                "novelty": 9.0,
                "coherence": 8.5,
                "usefulness": 7.5,
                "justification": "Promising synthesis",
            }
            return LLMResponse(text=json.dumps(payload))
        return LLMResponse(text="Fuse sleep-inspired consolidation with online fine-tuning to enable continual self-improvement.")


def test_daydream_loop_accepts_ideas() -> None:
    memory = MemoryStore()
    memory.add_entry("Focused gradient descent training", kind="concept")
    memory.add_entry("Hippocampal replay during sleep", kind="concept")

    config = DaydreamConfig(batch_size=1, novelty_threshold=5.0, coherence_threshold=5.0, usefulness_threshold=5.0)
    llm = FixedLLM()
    generator = IdeaGenerator(llm)
    critic = IdeaCritic(llm)

    loop = DaydreamingLoop(config=config, memory=memory, generator=generator, critic=critic)
    results = loop.run_iteration()

    assert len(results) == 1
    result = results[0]
    assert result.accepted is True
    assert "continual self-improvement" in result.proposal.text
    assert len(memory) == 3  # the new idea has been stored
    assert memory.get_recent(1)[0].kind == "idea"
