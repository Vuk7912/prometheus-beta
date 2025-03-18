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
    
    # Compression variables
    compressed = bytearray()
    context_dict = {}
    context_size = 3  # Initial context size
    
    # Sliding window for context
    context = data[:context_size]
    
    # Compress the data
    i = context_size
    while i < len(data):
        # Look up the current context
        current_context = data[i-context_size:i]
        
        # Check if context is in dictionary
        if current_context in context_dict:
            # If context predicted correctly, output a match flag
            if context_dict[current_context] == data[i]:
                compressed.append(1)  # Match flag
            else:
                # Mismatch, output 0 flag and the actual byte
                compressed.append(0)
                compressed.append(data[i])
        else:
            # New context, output 0 flag and the actual byte
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
    
    # Decompression variables
    decompressed = bytearray()
    context_dict = {}
    context_size = 3  # Must match compression context size
    
    # Initial context (first three bytes if available)
    if len(compressed_data) < context_size:
        return compressed_data
    
    context = compressed_data[:context_size]
    decompressed.extend(context)
    
    # Decompress the data
    i = context_size
    while i < len(compressed_data):
        # Check match flag
        if compressed_data[i] == 1:
            # Prediction match, use context dictionary
            current_context = decompressed[len(decompressed)-context_size:len(decompressed)]
            predicted_byte = context_dict.get(current_context)
            
            if predicted_byte is None:
                raise ValueError("Corrupted compressed data")
            
            decompressed.append(predicted_byte)
        else:
            # Mismatch or new context
            if i + 1 >= len(compressed_data):
                raise ValueError("Corrupted compressed data")
            
            # Get the actual byte
            actual_byte = compressed_data[i+1]
            decompressed.append(actual_byte)
            
            # Update context dictionary
            current_context = decompressed[len(decompressed)-context_size:len(decompressed)]
            context_dict[current_context] = actual_byte
            
            # Skip the byte we just processed
            i += 1
        
        # Move to next byte
        i += 1
    
    return bytes(decompressed)