"""
LZVN (Lempel-Ziv Variable-length Not) Compression Algorithm Implementation

This module provides a basic implementation of the LZVN compression algorithm.
LZVN is a variant of LZ compression used in some compression scenarios.

Key characteristics:
- Variable-length encoding
- Simple compression technique
- Designed for efficiency and speed
"""

def compress_lzvn(data):
    """
    Compress input data using a simplified LZVN compression algorithm.
    
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
        # Look-ahead buffer to find repeated sequences
        best_length = 0
        best_distance = 0
        
        # Search back for potential matches (up to 255 bytes)
        search_start = max(0, current_pos - 255)
        for search_pos in range(search_start, current_pos):
            match_length = 0
            
            # Check for repeated sequence
            while (current_pos + match_length < len(data) and 
                   match_length < 15 and  # Max match length
                   data[search_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_distance = current_pos - search_pos
        
        # Encode the current token
        if best_length >= 3:
            # Compression token: [distance][length]
            # Ensure distance and length are within 4-bit ranges
            distance = min(best_distance, 255)
            length = min(best_length, 15)
            token = ((distance & 0x0F) << 4) | (length & 0x0F)
            compressed.append(token)
            current_pos += length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return compressed

def decompress_lzvn(compressed_data):
    """
    Decompress data compressed with the LZVN algorithm.
    
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
            if distance == 0 and length == 0:
                # Invalid token
                raise ValueError("Invalid compression token")
            
            # Calculate actual distance in the decompressed buffer
            actual_distance = len(decompressed) - distance
            
            # Copy repeated sequence
            for i in range(length):
                if actual_distance < 0:
                    raise ValueError("Invalid compression token")
                decompressed.append(decompressed[actual_distance + i])
            
            current_pos += 1
    
    return decompressed