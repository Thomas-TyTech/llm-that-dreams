"""Tokenization utilities for the optical compression scaffold."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Tuple

import numpy as np
from PIL import Image

from .renderer import compute_image_token_grid


@dataclass
class WindowEncoderConfig:
    patch_size: int = 16
    normalize: bool = True


class WindowedFeatureEncoder:
    """Simplified stand-in for the window-attention encoder in DeepEncoder."""

    def __init__(self, config: WindowEncoderConfig | None = None) -> None:
        self.config = config or WindowEncoderConfig()

    def _pad_image(self, image: Image.Image) -> np.ndarray:
        patch = self.config.patch_size
        grid_w, grid_h = compute_image_token_grid(image, patch)
        padded_w = grid_w * patch
        padded_h = grid_h * patch
        arr = np.array(image, dtype=np.float32)
        padded = np.full((padded_h, padded_w), fill_value=255, dtype=np.float32)
        padded[: arr.shape[0], : arr.shape[1]] = arr
        return padded

    def encode(self, image: Image.Image) -> np.ndarray:
        padded = self._pad_image(image)
        patch = self.config.patch_size
        grid_h = padded.shape[0] // patch
        grid_w = padded.shape[1] // patch
        tokens = padded.reshape(grid_h, patch, grid_w, patch)
        tokens = tokens.transpose(0, 2, 1, 3)
        flat_tokens = tokens.reshape(grid_h * grid_w, patch, patch)
        if self.config.normalize:
            flat_tokens = flat_tokens / 255.0
        return flat_tokens


@dataclass
class TokenCompressorConfig:
    reduction: int = 4
    keep_statistics: bool = True


class TokenCompressor:
    """Down-sample vision tokens by strided average pooling."""

    def __init__(self, config: TokenCompressorConfig | None = None) -> None:
        self.config = config or TokenCompressorConfig()

    def compress(self, tokens: np.ndarray) -> Tuple[np.ndarray, dict]:
        reduction = self.config.reduction
        if reduction <= 1:
            return tokens, {}

        token_count, h, w = tokens.shape
        side = int(math.sqrt(token_count))
        if side * side != token_count:
            # fall back to linear grouping when not a perfect square
            trimmed = token_count - (token_count % reduction)
            kept = tokens[:trimmed]
            pooled = kept.reshape(trimmed // reduction, reduction, h, w).mean(axis=1)
        else:
            grid = tokens.reshape(side, side, h, w)
            stride = int(math.sqrt(reduction))
            if stride * stride != reduction:
                stride = reduction
            pooled = grid.reshape(side // stride, stride, side // stride, stride, h, w).mean(axis=(1, 3))
            pooled = pooled.reshape(-1, h, w)

        metadata = {}
        if self.config.keep_statistics:
            metadata = {
                "mean_intensity": float(tokens.mean()),
                "std_intensity": float(tokens.std()),
                "reduction": reduction,
            }
        return pooled, metadata
