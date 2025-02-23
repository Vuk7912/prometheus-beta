"""
Simple LZVN-like Compression Algorithm Implementation

This module provides a basic implementation of a compression technique 
inspired by LZ-style algorithms.
"""

def compress_lzvn(data):
    """
    Compress input data using a simplified LZ-style algorithm.
    
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
    
    # Compression variables
    compressed = bytearray()
    current_pos = 0
    
    while current_pos < len(data):
        # Look for the longest match in the previously seen data
        best_length = 0
        best_distance = 0
        
        # Search window (limit to 255 bytes back)
        search_start = max(0, current_pos - 255)
        
        for search_pos in range(search_start, current_pos):
            # Try to find the longest match
            match_length = 0
            while (current_pos + match_length < len(data) and 
                   match_length < 15 and  # Limit match length to 15
                   data[search_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if longer
            if match_length > best_length:
                best_length = match_length
                best_distance = current_pos - search_pos
        
        # Encode token based on match
        if best_length >= 3:
            # Compression token: [distance][length]
            token = ((min(best_distance, 15) << 4) | min(best_length, 15)) & 0xFF
            compressed.append(token)
            current_pos += best_length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def decompress_lzvn(compressed_data):
    """
    Decompress data compressed with the LZVN-like algorithm.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input is empty or appears to be invalid
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompression variables
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        token = compressed_data[current_pos]
        
        # Extract distance and length 
        distance = (token >> 4) & 0x0F
        length = token & 0x0F
        
        if length == 0:
            # Literal byte
            decompressed.append(token)
            current_pos += 1
        else:
            # Matched sequence
            if distance == 0:
                # Something went wrong, but continue with literal
                decompressed.append(token)
                current_pos += 1
                continue
            
            # Reconstruct the repeated sequence
            start_index = len(decompressed) - distance
            for i in range(length):
                # Ensure we can safely copy the sequence
                if start_index + i < 0 or start_index + i >= len(decompressed):
                    break
                decompressed.append(decompressed[start_index + i])
            
            current_pos += 1
    
    return decompressed