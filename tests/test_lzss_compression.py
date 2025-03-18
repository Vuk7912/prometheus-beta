"""
Test suite for LZSS Compression Algorithm
"""

import pytest
import sys
import os

# Ensure src directory is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzss_compression import LZSSCompressor

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    test_data = b"hello world hello world"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_repeated_patterns():
    """Test compression of highly repetitive data"""
    compressor = LZSSCompressor()
    test_data = b"AAAAAAAAAAAAAAAAAAAAAA"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_mixed_patterns():
    """Test compression of mixed patterns"""
    compressor = LZSSCompressor()
    test_data = b"abcabcabcabcabcabcabcabc"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_empty_input():
    """Test compression and decompression of empty input"""
    compressor = LZSSCompressor()
    test_data = b""
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_string_input():
    """Test compression with string input"""
    compressor = LZSSCompressor()
    test_data = "hello world hello world"
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data.encode('utf-8')

def test_invalid_input_type():
    """Test handling of invalid input types"""
    compressor = LZSSCompressor()
    
    with pytest.raises(TypeError):
        compressor.compress(123)
    
    with pytest.raises(TypeError):
        compressor.decompress(123)

def test_long_input():
    """Test compression of longer input"""
    compressor = LZSSCompressor()
    test_data = b"This is a longer test string with some repeated patterns " * 100
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_custom_window_size():
    """Test compression with custom window size"""
    compressor = LZSSCompressor(window_size=1024, min_match_length=4)
    test_data = b"abcabcabcabcabcabcabcabc" * 10
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data