"""Command line entry point for the daydreaming loop prototype."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from daydreamer import (
    AnthropicLLM,
    DaydreamConfig,
    DaydreamingLoop,
    IdeaCritic,
    IdeaGenerator,
    MemoryStore,
    MockLLM,
)

logger = logging.getLogger("daydream.cli")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the LLM daydreaming loop")
    parser.add_argument("--memory", type=Path, default=Path("memory.json"), help="Path to persistent memory store")
    parser.add_argument("--iterations", type=int, default=1, help="Number of iterations to execute (0 for infinite)")
    parser.add_argument("--batch-size", type=int, default=1, help="Number of concept pairs per iteration")
    parser.add_argument("--novelty", type=float, default=6.5, help="Novelty threshold for accepting ideas")
    parser.add_argument("--coherence", type=float, default=6.0, help="Coherence threshold for accepting ideas")
    parser.add_argument("--usefulness", type=float, default=5.0, help="Usefulness threshold for accepting ideas")
    parser.add_argument("--log-level", default="INFO", help="Logging level")
    parser.add_argument(
        "--anthropic-model",
        default=None,
        help=(
            "Name of the Anthropic model to use. If provided, the CLI will invoke Anthropic instead of the mock LLM. "
            "Requires ANTHROPIC_API_KEY to be set."
        ),
    )
    parser.add_argument(
        "--anthropic-system-prompt",
        default=None,
        help="Optional system prompt to send with Anthropic requests.",
    )
    return parser.parse_args(argv)


def _configure_logging(level: str) -> None:
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO), format="%(asctime)s [%(levelname)s] %(message)s")


def _bootstrap_memory(store: MemoryStore) -> None:
    if len(store) > 0:
        return
    logger.info("Memory is empty; seeding with default concepts.")
    seed_concepts = [
        "Self-supervised language model pretraining",
        "Default mode network in neuroscience",
        "Latent space interpolation in diffusion models",
        "Economic theory of combinatorial innovation",
        "Dream incubation techniques",
    ]
    for concept in seed_concepts:
        store.add_entry(concept, kind="concept", metadata={"seed": True})


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(list(argv) if argv is not None else sys.argv[1:])
    _configure_logging(args.log_level)

    config = DaydreamConfig(
        batch_size=args.batch_size,
        novelty_threshold=args.novelty,
        coherence_threshold=args.coherence,
        usefulness_threshold=args.usefulness,
    )

    memory = MemoryStore(persistence_path=args.memory)
    _bootstrap_memory(memory)

    if args.anthropic_model:
        llm_client = AnthropicLLM(
            model=args.anthropic_model,
            system_prompt=args.anthropic_system_prompt,
        )
    else:
        llm_client = MockLLM()
    generator = IdeaGenerator(llm_client)
    critic = IdeaCritic(llm_client)

    loop = DaydreamingLoop(config=config, memory=memory, generator=generator, critic=critic)

    def report(results):
        for result in results:
            status = "ACCEPTED" if result.accepted else "rejected"
            logger.info(
                "[%s] %s | novelty=%.1f coherence=%.1f usefulness=%.1f",
                status,
                result.proposal.text,
                result.score.novelty,
                result.score.coherence,
                result.score.usefulness,
            )

    iterations = None if args.iterations == 0 else args.iterations
    loop.run_forever(callback=report, max_iterations=iterations)
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(main())
