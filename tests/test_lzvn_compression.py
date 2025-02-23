"""
Unit tests for LZVN Compression Algorithm

This test suite covers various scenarios for compression and decompression,
including edge cases and error handling.
"""

import pytest
import random
import string
from src.lzvn_compression import compress_lzvn, decompress_lzvn

def test_simple_compression_decompression():
    """Test basic compression and decompression of a simple string"""
    original_data = b"hello world hello world"
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_repeated_pattern_compression():
    """Test compression of data with repeated patterns"""
    original_data = b"ABCABCABCABCABC"
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_random_data_compression():
    """Test compression and decompression of random data"""
    # Generate random bytes
    random_data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = compress_lzvn(random_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == random_data

def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lzvn(b"")
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        decompress_lzvn(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        compress_lzvn("not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes or bytearray"):
        decompress_lzvn("not bytes")

def test_single_byte_compression():
    """Test compression and decompression of a single byte"""
    original_data = b"A"
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_long_repeated_sequence():
    """Test compression of a long repeated sequence"""
    original_data = b"HELLO" * 100
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_mixed_pattern_compression():
    """Test compression of data with mixed patterns"""
    original_data = b"abcdefghijklmnopqrstuvwxyz" * 10
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_compression_preserves_data_consistency():
    """Ensure multiple compression-decompression cycles produce same result"""
    original_data = bytes(random.randint(0, 255) for _ in range(500))
    
    # First pass
    compressed1 = compress_lzvn(original_data)
    decompressed1 = decompress_lzvn(compressed1)
    assert decompressed1 == original_data
    
    # Second pass on decompressed data
    compressed2 = compress_lzvn(decompressed1)
    decompressed2 = decompress_lzvn(compressed2)
    assert decompressed2 == original_data