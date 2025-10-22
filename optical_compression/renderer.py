"""Utilities for rendering text into dense grayscale canvases."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Tuple

from PIL import Image, ImageDraw, ImageFont


@dataclass
class RenderConfig:
    """Configuration for turning text into a raster image.

    The defaults mirror the 1024x1024 base mode discussed in the DeepSeek-OCR
    report while remaining lightweight enough to run on CPU during tests.
    """

    max_width: int = 1024
    padding: int = 32
    font_size: int = 28
    line_spacing: int = 6
    background: int = 255
    foreground: int = 0
    font_path: str | None = None


class TextRenderer:
    """Render unicode text into a padded grayscale image.

    The component focuses on deterministic layout so that downstream tokenizers
    can reason about spatial structure. Words are wrapped based on character
    length which is sufficient for monospaced OCR style rendering.
    """

    def __init__(self, config: RenderConfig | None = None) -> None:
        self.config = config or RenderConfig()
        if self.config.font_path is None:
            self._font = ImageFont.load_default()
        else:
            self._font = ImageFont.truetype(self.config.font_path, self.config.font_size)

    def _wrap_lines(self, text: str) -> Iterable[str]:
        words = text.split()
        if not words:
            return [""]

        max_width = self.config.max_width - 2 * self.config.padding
        # Estimate the number of characters per line based on font metrics.
        char_width = self._font.getlength("M") or 1
        approx_chars = max(1, int(max_width // char_width))

        lines = []
        current: list[str] = []
        for word in words:
            tentative = " ".join(current + [word]) if current else word
            if len(tentative) > approx_chars:
                if current:
                    lines.append(" ".join(current))
                    current = [word]
                else:
                    # Word itself exceeds the limit; hard break it.
                    for idx in range(0, len(word), approx_chars):
                        lines.append(word[idx : idx + approx_chars])
                    current = []
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))
        return lines

    def render(self, text: str) -> Image.Image:
        lines = list(self._wrap_lines(text))
        if not lines:
            lines = [""]

        ascent, descent = self._font.getmetrics()
        line_height = ascent + descent + self.config.line_spacing
        image_height = line_height * len(lines) + 2 * self.config.padding
        image_width = self.config.max_width

        image = Image.new("L", (image_width, image_height), color=self.config.background)
        draw = ImageDraw.Draw(image)

        y = self.config.padding
        for line in lines:
            draw.text((self.config.padding, y), line, font=self._font, fill=self.config.foreground)
            y += line_height
        return image


def compute_image_token_grid(image: Image.Image, patch_size: int) -> Tuple[int, int]:
    """Return the number of patches that fit along each dimension."""

    width, height = image.size
    grid_w = math.ceil(width / patch_size)
    grid_h = math.ceil(height / patch_size)
    return grid_w, grid_h
