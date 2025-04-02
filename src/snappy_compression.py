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
    
    # Improved compression strategy
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for repeated sequences
        repeat_count = 1
        max_lookahead = min(255, len(data) - i)
        
        while (repeat_count < max_lookahead and 
               data[i] == data[i + repeat_count]):
            repeat_count += 1
        
        # If more than 3 repeated bytes, use run-length encoding
        if repeat_count > 3:
            # Special marker for run-length
            compressed.append(0xFE)  # Different marker to distinguish from previous implementation
            compressed.append(repeat_count - 1)  # Subtract 1 to allow 0-255 range
            compressed.append(data[i])
            i += repeat_count
        else:
            # Literal byte with a different marker
            compressed.append(0xFD)
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
        # Run-length encoding marker
        if compressed_data[i] == 0xFE:
            # Ensure we have enough bytes for run-length encoding
            if i + 2 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Extract repeat count and byte
            repeat_count = compressed_data[i + 1] + 1  # Add 1 back
            repeat_byte = compressed_data[i + 2]
            
            # Add repeated bytes
            decompressed.extend([repeat_byte] * repeat_count)
            
            # Move index
            i += 3
        
        # Literal byte marker 
        elif compressed_data[i] == 0xFD:
            # Ensure we have the literal byte
            if i + 1 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Add literal byte
            decompressed.append(compressed_data[i + 1])
            
            # Move index
            i += 2
        
        else:
            # If no marker is found, this indicates invalid compressed data
            raise ValueError("Invalid compressed data format")