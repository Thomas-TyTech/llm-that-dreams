"""Optional decoders that can turn compressed tokens back into text."""

from __future__ import annotations

from dataclasses import dataclass

from .pipeline import VisionTokenSequence


@dataclass
class OptionalTesseractDecoder:
    """Attempt OCR with pytesseract if the binary is available.

    The dependency is optional; the class raises a RuntimeError if pytesseract
    or the `tesseract` binary are missing. This keeps the core scaffold lightweight
    while still showcasing how a decoder could be integrated.
    """

    language: str = "eng"

    def _import(self):
        try:
            import pytesseract  # type: ignore
        except ImportError as exc:  # pragma: no cover - executed when dependency missing
            raise RuntimeError(
                "pytesseract is not installed. Install it to enable OCR decoding."
            ) from exc
        return pytesseract

    def decode(self, sequence: VisionTokenSequence) -> str:
        pytesseract = self._import()
        image = sequence.rendered_image
        return pytesseract.image_to_string(image, lang=self.language)
