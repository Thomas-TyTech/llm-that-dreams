"""Implementation of the daydreaming loop described in the whitepaper."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Callable, Iterable, List, Sequence

from .config import DaydreamConfig
from .critic import IdeaCritic, IdeaScore
from .generator import IdeaGenerator, IdeaProposal
from .memory import MemoryEntry, MemoryStore

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class DaydreamResult:
    """Represents the outcome of evaluating a single idea."""

    concept_a: MemoryEntry
    concept_b: MemoryEntry
    proposal: IdeaProposal
    score: IdeaScore
    accepted: bool


class DaydreamingLoop:
    """Core orchestrator that runs the daydreaming process."""

    def __init__(
        self,
        *,
        config: DaydreamConfig,
        memory: MemoryStore,
        generator: IdeaGenerator,
        critic: IdeaCritic,
    ) -> None:
        self._config = config
        self._memory = memory
        self._generator = generator
        self._critic = critic

    def run_iteration(self) -> Sequence[DaydreamResult]:
        pairs = self._memory.sample_pairs(self._config.batch_size)
        if not pairs:
            logger.debug("No concept pairs available; skipping iteration.")
            return []

        results: List[DaydreamResult] = []
        for concept_a, concept_b in pairs:
            proposal = self._generator.propose(concept_a, concept_b)
            score = self._critic.score(proposal.text)
            accepted = self._should_accept(score)
            if accepted:
                metadata = {
                    "sources": (concept_a.id, concept_b.id),
                    "scores": {
                        "novelty": score.novelty,
                        "coherence": score.coherence,
                        "usefulness": score.usefulness,
                    },
                    "justification": score.justification,
                }
                self._memory.add_entry(proposal.text, kind="idea", metadata=metadata)
                if self._config.max_history:
                    self._memory.prune(self._config.max_history)
            results.append(
                DaydreamResult(
                    concept_a=concept_a,
                    concept_b=concept_b,
                    proposal=proposal,
                    score=score,
                    accepted=accepted,
                )
            )
        return results

    def run_forever(
        self,
        *,
        callback: Callable[[Sequence[DaydreamResult]], None] | None = None,
        max_iterations: int | None = None,
    ) -> None:
        """Repeatedly execute the loop, optionally invoking a callback."""

        iteration = 0
        while True:
            results = self.run_iteration()
            if callback:
                callback(results)
            iteration += 1
            if max_iterations is not None and iteration >= max_iterations:
                return
            time.sleep(self._config.sleep_interval.total_seconds())

    # ------------------------------------------------------------------
    def _should_accept(self, score: IdeaScore) -> bool:
        return (
            score.novelty >= self._config.novelty_threshold
            and score.coherence >= self._config.coherence_threshold
            and score.usefulness >= self._config.usefulness_threshold
        )


__all__ = ["DaydreamingLoop", "DaydreamResult"]
