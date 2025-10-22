from optical_compression import CompressionConfig, OpticalTokenCompressor


SAMPLE_TEXT = """DeepSeek-OCR proposes using a vision encoder as a compression stage.
This scaffold ensures we can render a long passage and condense it into a
smaller number of vision tokens for downstream decoding experiments."""


def test_compression_ratio_below_ten_to_one():
    config = CompressionConfig()
    config.encoder.patch_size = 16
    config.compressor.reduction = 16
    compressor = OpticalTokenCompressor(config)

    sequence = compressor.compress_text(SAMPLE_TEXT)

    assert sequence.vision_token_count < sequence.text_token_count
    assert sequence.compression_ratio > 1.0
    assert sequence.compression_ratio >= 1.2


def test_summary_reports_expected_fields():
    compressor = OpticalTokenCompressor()
    sequence = compressor.compress_text("Optical compression scaffolding")
    summary = sequence.summary()

    assert "vision_tokens" in summary
    assert "text_tokens" in summary
    assert "compression_ratio" in summary
