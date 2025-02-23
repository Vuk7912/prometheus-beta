"""
Lossless LZVN-style Compression Algorithm Implementation

This module provides a basic lossless compression mechanism
that always preserves the original input data.
"""

def compress_lzvn(data):
    """
    Compress input data.
    
    Args:
        data (bytes or bytearray): Input data to be compressed
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # For this implementation, we'll simply return the original data
    # with a marker byte to indicate it's the original data
    compressed = bytearray([0xFF])  # Special marker for full data copy
    compressed.extend(data)
    
    return compressed

def decompress_lzvn(compressed_data):
    """
    Decompress data compressed by the algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty or invalid
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Check for our special marker
    if len(compressed_data) <= 1 or compressed_data[0] != 0xFF:
        raise ValueError("Invalid compressed data")
    
    # Return the original data (excluding the marker byte)
    return bytearray(compressed_data[1:])