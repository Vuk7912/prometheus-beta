"""
Unit tests for LZP compression algorithm.
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzp_compression import lzp_compress, lzp_decompress

def test_compress_decompress_basic():
    """Test basic compression and decompression of a simple string."""
    original_data = b"hello world hello world"
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data

def test_compress_decompress_repeated_patterns():
    """Test compression of data with repeated patterns."""
    original_data = b"abcabcabcabcabc" * 10
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data

def test_compress_decompress_random_data():
    """Test compression of random data."""
    import random
    random.seed(42)
    original_data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data

def test_string_input():
    """Test compression and decompression with string input."""
    original_data = "hello world hello world"
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_empty_input_error():
    """Test error handling for empty input."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzp_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzp_decompress(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzp_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzp_decompress(123)

def test_single_byte_data():
    """Test compression and decompression of single byte data."""
    original_data = b"a"
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data

def test_small_repeated_data():
    """Test compression of small repeated data."""
    original_data = b"aaaaaaaaaa"
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original_data

def test_compression_ratio():
    """Verify that compression reduces data size."""
    original_data = b"hello world " * 100
    compressed = lzp_compress(original_data)
    assert len(compressed) < len(original_data)