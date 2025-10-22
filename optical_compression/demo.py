"""Run a small compression demo from the command line."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import CompressionConfig, OpticalTokenCompressor


EXAMPLE_TEXT = """DeepSeek-OCR explores optical context compression by rendering text
into high-resolution vision tokens and reconstructing it with a lightweight
decoder. This demo simulates the encoder stage to showcase token counts and
compression ratios."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--text",
        type=str,
        default=None,
        help="Text to compress. Defaults to a built-in excerpt inspired by the paper.",
    )
    parser.add_argument(
        "--patch-size",
        type=int,
        default=16,
        help="Spatial patch size used for vision tokens.",
    )
    parser.add_argument(
        "--reduction",
        type=int,
        default=16,
        help="How many tokens to merge in the compressor stage.",
    )
    parser.add_argument(
        "--save-image",
        type=Path,
        default=None,
        help="Optional path to save the rendered document image.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    text = args.text or EXAMPLE_TEXT

    config = CompressionConfig()
    config.encoder.patch_size = args.patch_size
    config.compressor.reduction = args.reduction
    compressor = OpticalTokenCompressor(config)

    sequence = compressor.compress_text(text)
    summary = sequence.summary()
    print(json.dumps(summary, indent=2))

    if args.save_image:
        sequence.rendered_image.save(args.save_image)
        print(f"Saved rendered image to {args.save_image}")


if __name__ == "__main__":
    main()
