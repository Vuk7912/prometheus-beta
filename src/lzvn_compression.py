"""
Simplified LZV-style Compression Algorithm Implementation

This module provides a basic implementation of a compression technique 
inspired by LZ-style algorithms with a focus on data preservation.
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
        # Look for longest repeating sequence
        best_length = 0
        best_distance = 0
        
        # Limit search window to 255 bytes back
        search_start = max(0, current_pos - 255)
        
        for search_pos in range(search_start, current_pos):
            match_length = 0
            
            # Find match length
            while (current_pos + match_length < len(data) and 
                   match_length < 15 and
                   data[search_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_distance = current_pos - search_pos
        
        # Encode tokens
        if best_length >= 3:
            # Compression token: high 4 bits for distance, low 4 bits for length
            token = ((best_distance & 0x0F) << 4) | (best_length & 0x0F)
            compressed.append(token)
            
            # Add actual bytes skipped
            for _ in range(best_length):
                compressed.append(data[current_pos])
                current_pos += 1
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
                decompressed.append(token)
                current_pos += 1
                continue
            
            # Ensure there's enough data to copy
            if len(decompressed) < distance:
                decompressed.append(token)
                current_pos += 1
                continue
            
            # Prepare to copy
            start = len(decompressed) - distance
            
            # Get the repeat bytes 
            repeat_bytes = compressed_data[current_pos+1:current_pos+1+length]
            decompressed.extend(repeat_bytes)
            
            current_pos += 1 + length
    
    return decompressed