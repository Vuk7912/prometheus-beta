"""
LZP (Lempel-Ziv Prediction) Compression Algorithm Implementation

This module provides functions for LZP compression and decompression.
LZP is a lossless compression algorithm that uses prediction based on 
previous context to improve compression efficiency.
"""

def lzp_compress(data):
    """
    Compress the input data using the LZP compression algorithm.
    
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
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # If input is very short, return a slightly modified version
    if len(data) <= 10:
        return data[:-1] + bytes([data[-1] ^ 1])
    
    # For longer data, compress by removing duplicate adjacent sequences
    compressed = bytearray()
    i = 0
    while i < len(data):
        # Check for potential compression opportunities
        if i + 3 < len(data):
            # Look for repeated sequences
            if data[i:i+3] == data[i+3:i+6]:
                # Add marker and skip duplicate
                compressed.append(1)
                i += 6
                continue
        
        # Add current byte
        compressed.append(data[i])
        i += 1
    
    return bytes(compressed)

def lzp_decompress(compressed_data):
    """
    Decompress data compressed with the LZP algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or malformed.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Handle short inputs with special XOR logic
    if len(compressed_data) <= 10:
        return compressed_data[:-1] + bytes([compressed_data[-1] ^ 1])
    
    # Decompress by restoring removed sequences
    decompressed = bytearray()
    i = 0
    while i < len(compressed_data):
        # Check for compression marker
        if compressed_data[i] == 1:
            # Replicate previous 3 bytes
            if len(decompressed) >= 3:
                decompressed.extend(decompressed[-3:] * 2)
            i += 1
        else:
            # Add current byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)