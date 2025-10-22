"""High-level orchestration for optical text compression."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from typing import Dict

import numpy as np
from PIL import Image

from .renderer import RenderConfig, TextRenderer
from .tokenizer import (
    TokenCompressor,
    TokenCompressorConfig,
    WindowEncoderConfig,
    WindowedFeatureEncoder,
)


_TOKEN_PATTERN = re.compile(r"\w+|[^\w\s]")


def _count_text_tokens(text: str) -> int:
    tokens = _TOKEN_PATTERN.findall(text)
    return max(1, len(tokens))


@dataclass
class CompressionConfig:
    """Bundle configuration for the compression scaffold."""

    renderer: RenderConfig = field(default_factory=RenderConfig)
    encoder: WindowEncoderConfig = field(default_factory=WindowEncoderConfig)
    compressor: TokenCompressorConfig = field(default_factory=TokenCompressorConfig)


@dataclass
class VisionTokenSequence:
    tokens: np.ndarray
    metadata: Dict[str, float]
    rendered_image: Image.Image
    text: str
    text_token_count: int

    @property
    def vision_token_count(self) -> int:
        return int(self.tokens.shape[0])

    @property
    def compression_ratio(self) -> float:
        return self.text_token_count / max(1, self.vision_token_count)

    def summary(self) -> Dict[str, float]:
        result = dict(self.metadata)
        result.update(
            {
                "vision_tokens": float(self.vision_token_count),
                "text_tokens": float(self.text_token_count),
                "compression_ratio": float(self.compression_ratio),
            }
        )
        return result


class OpticalTokenCompressor:
    """Coordinate rendering, tokenization, and statistical compression."""

    def __init__(self, config: CompressionConfig | None = None) -> None:
        self.config = config or CompressionConfig()
        self._renderer = TextRenderer(self.config.renderer)
        self._encoder = WindowedFeatureEncoder(self.config.encoder)
        self._compressor = TokenCompressor(self.config.compressor)

    def compress_text(self, text: str) -> VisionTokenSequence:
        image = self._renderer.render(text)
        tokens = self._encoder.encode(image)
        compressed, metadata = self._compressor.compress(tokens)
        text_tokens = _count_text_tokens(text)
        return VisionTokenSequence(
            tokens=compressed,
            metadata=metadata,
            rendered_image=image,
            text=text,
            text_token_count=text_tokens,
        )

    def estimate_required_tokens(self, text: str, target_ratio: float) -> int:
        token_count = _count_text_tokens(text)
        return int(math.ceil(token_count / target_ratio))

    def reconstruct_image(self, sequence: VisionTokenSequence) -> Image.Image:
        tokens = sequence.tokens
        tokens = np.clip(tokens, 0.0, 1.0) * 255.0
        tokens = tokens.astype(np.uint8)
        token_count, h, w = tokens.shape
        side = int(math.ceil(math.sqrt(token_count)))
        padded = np.full((side * h, side * w), 255, dtype=np.uint8)
        for idx in range(token_count):
            row = idx // side
            col = idx % side
            y0 = row * h
            x0 = col * w
            padded[y0 : y0 + h, x0 : x0 + w] = tokens[idx]
        return Image.fromarray(padded)
