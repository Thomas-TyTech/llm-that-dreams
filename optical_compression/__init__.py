"""Scaffold for optical text compression inspired by the DeepSeek-OCR paper."""

from .pipeline import OpticalTokenCompressor, CompressionConfig, VisionTokenSequence
from .decoder import OptionalTesseractDecoder

__all__ = [
    "OpticalTokenCompressor",
    "CompressionConfig",
    "VisionTokenSequence",
    "OptionalTesseractDecoder",
]
