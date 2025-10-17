"""Configuration helpers for the daydreaming loop."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta


@dataclass(slots=True)
class DaydreamConfig:
    """Configuration for the daydreaming loop.

    Attributes:
        batch_size: Number of concept pairs to explore per iteration.
        novelty_threshold: Minimum novelty score to accept an idea.
        usefulness_threshold: Minimum usefulness score to accept an idea.
        coherence_threshold: Minimum coherence score to accept an idea.
        max_history: Maximum number of entries to keep in memory (oldest dropped).
        sleep_interval: Seconds to sleep between iterations when running continuously.
    """

    batch_size: int = 1
    novelty_threshold: float = 6.5
    usefulness_threshold: float = 5.0
    coherence_threshold: float = 6.0
    max_history: int | None = 10_000
    sleep_interval: timedelta = field(default=timedelta(seconds=5))

    def __post_init__(self) -> None:
        if self.batch_size < 1:
            raise ValueError("batch_size must be >= 1")
        for name in ("novelty_threshold", "usefulness_threshold", "coherence_threshold"):
            value = getattr(self, name)
            if not 0 <= value <= 10:
                raise ValueError(f"{name} must be between 0 and 10 inclusive; got {value}")
        if self.max_history is not None and self.max_history < 1:
            raise ValueError("max_history must be None or >= 1")
        if self.sleep_interval.total_seconds() < 0:
            raise ValueError("sleep_interval must be non-negative")
