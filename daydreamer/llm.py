"""Interfaces for integrating external LLMs."""

from __future__ import annotations

import hashlib
import itertools
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


@dataclass(slots=True)
class LLMRequest:
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 512


@dataclass(slots=True)
class LLMResponse:
    text: str


class LLMClient(ABC):
    """Abstract base class for language model backends."""

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """Execute a completion request."""


class MockLLM(LLMClient):
    """Simple deterministic mock used for tests and demos.

    The mock generates pseudo-creative outputs by hashing the prompt.
    """

    def __init__(self, scripted: dict[str, str] | None = None) -> None:
        self._scripted = scripted or {}
        self._counter = itertools.count(1)

    def generate(self, request: LLMRequest) -> LLMResponse:
        if request.prompt in self._scripted:
            return LLMResponse(text=self._scripted[request.prompt])
        digest = hashlib.sha1(request.prompt.encode("utf-8")).hexdigest()[:12]
        idx = next(self._counter)
        text = (
            f"Idea {idx}: blend-{digest[:4]} {digest[4:8]} {digest[8:]} | "
            f"Prompt length {len(request.prompt)}"
        )
        return LLMResponse(text=text)


def batched_generate(client: LLMClient, requests: Iterable[LLMRequest]) -> list[LLMResponse]:
    """Sequentially execute a batch of requests.

    This helper keeps the surface compatible with async implementations.
    """

    return [client.generate(req) for req in requests]


__all__ = ["LLMClient", "LLMRequest", "LLMResponse", "MockLLM", "batched_generate"]
