"""
Snappy Compression Algorithm Implementation

This module provides a simplified implementation of the Snappy compression algorithm.
Snappy is a fast compression/decompression library developed by Google.

Note: This is a basic implementation and may not be as performant as the 
official Snappy library.
"""

def compress(data):
    """
    Compress the input data using a simplified Snappy-like compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Simplified compression strategy
    compressed = bytearray()
    
    # Basic run-length encoding
    i = 0
    while i < len(data):
        # Look for repeated sequences
        repeat_count = 1
        while (i + repeat_count < len(data) and 
               repeat_count < 255 and 
               data[i] == data[i + repeat_count]):
            repeat_count += 1
        
        # If more than 3 repeated bytes, use run-length encoding
        if repeat_count > 3:
            compressed.append(0xFF)  # Special marker for run-length
            compressed.append(repeat_count)
            compressed.append(data[i])
            i += repeat_count
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed with the simplified Snappy-like algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or compressed data is invalid.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompression process
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check for run-length encoding marker
        if compressed_data[i] == 0xFF:
            # Ensure we have enough bytes for run-length encoding
            if i + 2 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Extract repeat count and byte
            repeat_count = compressed_data[i + 1]
            repeat_byte = compressed_data[i + 2]
            
            # Add repeated bytes
            decompressed.extend([repeat_byte] * repeat_count)
            
            # Move index
            i += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)