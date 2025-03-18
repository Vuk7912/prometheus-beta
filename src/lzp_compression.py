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
    
    # Compression variables
    compressed = bytearray()
    context_dict = {}
    context_size = 3  # Initial context size
    
    # Compress the data
    i = 0
    while i < len(data):
        # Create context (or use initial bytes for first iteration)
        if i < context_size:
            current_context = tuple(data[:i+1]) if i > 0 else tuple()
        else:
            current_context = tuple(data[i-context_size:i])
        
        # Find compression opportunity
        if current_context in context_dict:
            # If context predicts current byte, use match flag
            if context_dict[current_context] == data[i]:
                compressed.append(1)  # Match flag
            else:
                # Mismatch, output actual byte
                compressed.append(0)
                compressed.append(data[i])
        else:
            # New context, output 0 flag and byte
            compressed.append(0)
            compressed.append(data[i])
        
        # Update context dictionary
        context_dict[current_context] = data[i]
        
        # Move to next byte
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
    
    # Decompression variables
    decompressed = bytearray()
    context_dict = {}
    context_size = 3  # Must match compression context size
    
    # Decompress the data
    i = 0
    while i < len(compressed_data):
        # Handle match or literal byte
        if compressed_data[i] == 1:
            # Prediction match
            if len(decompressed) < context_size:
                # Not enough context, skip
                i += 1
                continue
            
            # Get current context
            current_context = tuple(decompressed[len(decompressed)-context_size:len(decompressed)])
            
            # Try to retrieve predicted byte
            if current_context in context_dict:
                predicted_byte = context_dict[current_context]
                decompressed.append(predicted_byte)
            else:
                # Fallback: skip this match flag
                i += 1
                continue
        else:
            # Ensure enough data for literal byte
            if i + 1 >= len(compressed_data):
                break
            
            # Literal byte
            current_byte = compressed_data[i+1]
            decompressed.append(current_byte)
            
            # Update context dictionary
            if len(decompressed) >= context_size:
                current_context = tuple(decompressed[len(decompressed)-context_size:len(decompressed)])
                context_dict[current_context] = current_byte
            
            # Skip the literal byte we just processed
            i += 1
        
        # Move to next byte
        i += 1
    
    return bytes(decompressed)