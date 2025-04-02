"""
Tests for Snappy Compression Algorithm Implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress, decompress

def test_compress_decompress_basic():
    """Test basic compression and decompression"""
    original = b"hello world"
    compressed = compress(original)
    assert compressed != original
    
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_decompress_repeated_bytes():
    """Test compression with repeated bytes"""
    original = b"aaaaaaaaaa"
    compressed = compress(original)
    assert len(compressed) < len(original)
    
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_decompress_mixed_data():
    """Test compression with mixed data"""
    original = b"hello world" * 10
    compressed = compress(original)
    assert compressed != original
    
    decompressed = decompress(compressed)
    assert decompressed == original

def test_compress_empty_input():
    """Test compression with empty input"""
    with pytest.raises(ValueError):
        compress(b"")

def test_decompress_empty_input():
    """Test decompression with empty input"""
    with pytest.raises(ValueError):
        decompress(b"")

def test_compress_invalid_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        compress(123)

def test_decompress_invalid_type():
    """Test decompression with invalid input type"""
    with pytest.raises(TypeError):
        decompress(123)

def test_string_input():
    """Test compression and decompression with string input"""
    original = "hello world"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_unicode_input():
    """Test compression and decompression with unicode input"""
    original = "こんにちは世界"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_edge_case_single_byte():
    """Test compression with a single byte"""
    original = b"a"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original