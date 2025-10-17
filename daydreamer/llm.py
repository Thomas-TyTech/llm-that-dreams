"""Interfaces for integrating external LLMs."""

from __future__ import annotations

import hashlib
import itertools
import os
from importlib import import_module, util
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Iterable, TYPE_CHECKING, cast

if TYPE_CHECKING:  # pragma: no cover - import for type checking only
    from anthropic import Anthropic as AnthropicClient
else:  # pragma: no cover - placeholder type when anthropic isn't installed at runtime
    AnthropicClient = Any
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


class AnthropicLLM(LLMClient):
    """LLM client backed by Anthropic's Messages API."""

    def __init__(
        self,
        client: AnthropicClient | None = None,
        *,
        model: str = "claude-3-opus-20240229",
        system_prompt: str | None = None,
    ) -> None:
        self._client = client or self._default_client()
        self._model = model
        self._system_prompt = system_prompt

    def _default_client(self) -> AnthropicClient:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY environment variable must be set when no client is provided."
            )
        if util.find_spec("anthropic") is None:
            raise RuntimeError(
                "The 'anthropic' package is required to use AnthropicLLM. Install it via 'pip install anthropic'."
            )
        module = import_module("anthropic")
        client_cls = getattr(module, "Anthropic")
        return cast("AnthropicClient", client_cls(api_key=api_key))

    def generate(self, request: LLMRequest) -> LLMResponse:
        message = self._client.messages.create(
            model=self._model,
            system=self._system_prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            messages=[{"role": "user", "content": request.prompt}],
        )
        text_parts: list[str] = []
        for item in message.content:
            if item.type == "text":
                text_parts.append(item.text)
        return LLMResponse(text="".join(text_parts).strip())


def batched_generate(client: LLMClient, requests: Iterable[LLMRequest]) -> list[LLMResponse]:
    """Sequentially execute a batch of requests.

    This helper keeps the surface compatible with async implementations.
    """

    return [client.generate(req) for req in requests]


__all__ = [
    "LLMClient",
    "LLMRequest",
    "LLMResponse",
    "MockLLM",
    "AnthropicLLM",
    "batched_generate",
]
__all__ = ["LLMClient", "LLMRequest", "LLMResponse", "MockLLM", "batched_generate"]
