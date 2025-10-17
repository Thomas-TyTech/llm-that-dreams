"""Idea generation utilities."""

from __future__ import annotations

from dataclasses import dataclass

from .llm import LLMClient, LLMRequest, LLMResponse
from .memory import MemoryEntry

_DEFAULT_PROMPT = """You are a creative synthesizer. Your task is to find deep, non-obvious, and potentially groundbreaking connections between the two following concepts. Do not state the obvious. Generate a hypothesis, a novel analogy, a potential research question, or a creative synthesis. Be speculative but ground your reasoning.\n\nConcept 1: {concept_a}\nConcept 2: {concept_b}\n\nThink step-by-step to explore potential connections:\n1. Are these concepts analogous in some abstract way?\n2. Could one concept be a metaphor for the other?\n3. Do they represent a similar problem or solution in different domains?\n4. Could they be combined to create a new idea or solve a problem?\n5. What revealing contradiction or tension exists between them?\n\nSynthesize your most interesting finding below."""


@dataclass(slots=True)
class IdeaProposal:
    """Represents a raw idea synthesized by the generator."""

    text: str
    prompt: str
    response: LLMResponse


class IdeaGenerator:
    """Wraps an LLM to propose ideas from concept pairs."""

    def __init__(self, client: LLMClient, *, prompt_template: str | None = None, temperature: float = 0.8) -> None:
        self._client = client
        self._prompt_template = prompt_template or _DEFAULT_PROMPT
        self._temperature = temperature

    def propose(self, concept_a: MemoryEntry, concept_b: MemoryEntry) -> IdeaProposal:
        prompt = self._prompt_template.format(concept_a=concept_a.content, concept_b=concept_b.content)
        request = LLMRequest(prompt=prompt, temperature=self._temperature)
        response = self._client.generate(request)
        return IdeaProposal(text=response.text.strip(), prompt=prompt, response=response)


__all__ = ["IdeaGenerator", "IdeaProposal"]
