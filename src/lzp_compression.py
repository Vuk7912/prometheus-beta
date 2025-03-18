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
    
    # Handle very short inputs
    if len(data) <= 3:
        return data
    
    # Compression variables
    compressed = bytearray()
    context_dict = {}
    context_size = 3  # Initial context size
    
    # Add initial context to compressed data
    compressed.extend(data[:context_size])
    
    # Compress the data
    predicted_len = 0
    i = context_size
    while i < len(data):
        # Create context as tuple of bytes (hashable)
        current_context = tuple(data[i-context_size:i])
        
        # Check if context is in dictionary
        if current_context in context_dict:
            # If context predicted correctly, update prediction count
            if context_dict[current_context] == data[i]:
                predicted_len += 1
                compressed.append(1)  # Match flag
            else:
                # Mismatch, output 0 flag and the actual byte
                compressed.append(0)
                compressed.append(data[i])
                predicted_len = 0
        else:
            # New context, output 0 flag and the actual byte
            compressed.append(0)
            compressed.append(data[i])
            predicted_len = 0
        
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
    
    # Handle very short inputs
    if len(compressed_data) <= 3:
        return compressed_data
    
    # Decompression variables
    decompressed = bytearray()
    context_dict = {}
    context_size = 3  # Must match compression context size
    
    # Add initial context to decompressed data
    context = compressed_data[:context_size]
    decompressed.extend(context)
    
    # Decompress the data
    i = context_size
    while i < len(compressed_data):
        # Check match flag
        if compressed_data[i] == 1:
            # Prediction match, use context dictionary
            current_context = tuple(decompressed[len(decompressed)-context_size:len(decompressed)])
            
            # Attempt to fetch previous prediction
            if current_context in context_dict:
                predicted_byte = context_dict[current_context]
                decompressed.append(predicted_byte)
            else:
                # If no prediction, fallback to previous context
                if i + 1 >= len(compressed_data):
                    break
                current_byte = compressed_data[i+1]
                decompressed.append(current_byte)
                current_context = tuple(decompressed[len(decompressed)-context_size:len(decompressed)])
                context_dict[current_context] = current_byte
                i += 1
        else:
            # Mismatch or new context
            if i + 1 >= len(compressed_data):
                break
            
            # Get the actual byte
            actual_byte = compressed_data[i+1]
            decompressed.append(actual_byte)
            
            # Update context dictionary
            current_context = tuple(decompressed[len(decompressed)-context_size:len(decompressed)])
            context_dict[current_context] = actual_byte
            
            # Skip the byte we just processed
            i += 1
        
        # Move to next byte
        i += 1
    
    return bytes(decompressed)