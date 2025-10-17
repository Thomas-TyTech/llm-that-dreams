"""Idea evaluation using a critic LLM."""

from __future__ import annotations

import json
from dataclasses import dataclass

from .llm import LLMClient, LLMRequest, LLMResponse

_CRITIC_PROMPT = """You are a discerning critic. Evaluate the following hypothesis on a scale of 1--10 for each of the following criteria:\n- Novelty: Is this idea surprising and non-obvious? (1=obvious, 10=paradigm-shifting)\n- Coherence: Is the reasoning logical and well-formed? (1=nonsense, 10=rigorous)\n- Usefulness: Could this idea lead to a testable hypothesis, a new product, or a solution to a problem? (1=useless, 10=highly applicable)\n\nHypothesis:\n"""  # noqa: E501

_CRITIC_SUFFIX = """\n\nRespond in compact JSON with the following shape:\n{\n  "novelty": <float>,\n  "coherence": <float>,\n  "usefulness": <float>,\n  "justification": "<1-2 sentences summary>"\n}"""


@dataclass(slots=True)
class IdeaScore:
    novelty: float
    coherence: float
    usefulness: float
    justification: str

    @property
    def average(self) -> float:
        return (self.novelty + self.coherence + self.usefulness) / 3


class IdeaCritic:
    """Scores ideas according to structured rubric."""

    def __init__(self, client: LLMClient, *, prompt_prefix: str | None = None) -> None:
        self._client = client
        self._prompt_prefix = prompt_prefix or _CRITIC_PROMPT

    def score(self, idea: str) -> IdeaScore:
        prompt = f"{self._prompt_prefix}{idea.strip()}{_CRITIC_SUFFIX}"
        response = self._client.generate(LLMRequest(prompt=prompt, temperature=0.2))
        payload = self._parse_response(response)
        return IdeaScore(
            novelty=payload["novelty"],
            coherence=payload["coherence"],
            usefulness=payload["usefulness"],
            justification=payload.get("justification", ""),
        )

    def _parse_response(self, response: LLMResponse) -> dict[str, float | str]:
        text = response.text.strip()
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            # Fall back to heuristic parsing when the critic misbehaves.
            payload = self._fallback_parse(text)
        for key in ("novelty", "coherence", "usefulness"):
            value = float(payload.get(key, 0.0))
            payload[key] = max(0.0, min(10.0, value))
        payload.setdefault("justification", text)
        return payload

    @staticmethod
    def _fallback_parse(text: str) -> dict[str, float | str]:
        numbers = []
        for token in text.replace("/", " ").split():
            try:
                numbers.append(float(token))
            except ValueError:
                continue
        values = (numbers + [0.0, 0.0, 0.0])[:3]
        return {
            "novelty": values[0],
            "coherence": values[1],
            "usefulness": values[2],
            "justification": text,
        }


__all__ = ["IdeaCritic", "IdeaScore"]
