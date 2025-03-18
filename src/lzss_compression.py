"""
Lempel-Ziv-Storer-Szymanski (LZSS) Compression Algorithm Implementation

This module provides functions for LZSS compression and decompression.
LZSS is a dictionary-based compression algorithm that replaces repeated 
occurrences of data with references to a single copy of that data.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, min_match_length=3):
        """
        Initialize the LZSS Compressor
        
        Args:
            window_size (int): Size of the sliding window for searching matches
            min_match_length (int): Minimum length of match to be encoded
        """
        self.window_size = window_size
        self.min_match_length = min_match_length

    def compress(self, data):
        """
        Compress input data using LZSS algorithm
        
        Args:
            data (bytes or str): Input data to compress
        
        Returns:
            bytes: Compressed data
        
        Raises:
            TypeError: If input is not bytes or str
        """
        # Convert to bytes if input is string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes or str")
        
        compressed = bytearray()
        data_length = len(data)
        current_pos = 0
        
        while current_pos < data_length:
            # Look for the longest match in the window
            best_length = 0
            best_offset = 0
            
            # Define search range
            search_start = max(0, current_pos - self.window_size)
            search_end = current_pos
            
            # Search for longest match
            for search_pos in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match continues
                while (current_pos + match_length < data_length and
                       data[search_pos + match_length] == data[current_pos + match_length] and
                       match_length < 255):
                    match_length += 1
                
                # Update best match if needed
                if match_length > best_length and match_length >= self.min_match_length:
                    best_length = match_length
                    best_offset = current_pos - search_pos
            
            # Encode the result
            if best_length > 0:
                # Encode match (offset, length)
                compressed.append(0)  # Flag for match
                compressed.append(best_offset & 0xFF)  # Lower byte of offset
                compressed.append((best_offset >> 8) & 0xFF)  # Upper byte of offset
                compressed.append(best_length)
                current_pos += best_length
            else:
                # Encode literal byte
                compressed.append(1)  # Flag for literal
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress LZSS compressed data
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        
        Raises:
            TypeError: If input is not bytes
            ValueError: If compressed data is invalid
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check if we have enough data
            if i + 1 >= len(compressed_data):
                break
            
            # Check flag byte
            flag = compressed_data[i]
            i += 1
            
            if flag == 0:  # Match
                # Ensure we have enough bytes for offset and length
                if i + 3 > len(compressed_data):
                    raise ValueError("Incomplete match data")
                
                # Extract offset and length
                offset = compressed_data[i] | (compressed_data[i+1] << 8)
                length = compressed_data[i+2]
                i += 3
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        raise ValueError("Invalid offset in compressed data")
                    decompressed.append(decompressed[start + j])
            
            elif flag == 1:  # Literal
                if i >= len(compressed_data):
                    raise ValueError("Incomplete literal data")
                decompressed.append(compressed_data[i])
                i += 1
            
            else:
                raise ValueError(f"Invalid flag byte: {flag}")
        
        return bytes(decompressed)