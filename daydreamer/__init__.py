"""Core package for the LLM daydreaming prototype."""

from .config import DaydreamConfig
from .loop import DaydreamingLoop
from .memory import MemoryStore, MemoryEntry
from .llm import LLMClient, MockLLM
from .generator import IdeaGenerator
from .critic import IdeaCritic, IdeaScore

__all__ = [
    "DaydreamConfig",
    "DaydreamingLoop",
    "MemoryStore",
    "MemoryEntry",
    "LLMClient",
    "MockLLM",
    "IdeaGenerator",
    "IdeaCritic",
    "IdeaScore",
]
