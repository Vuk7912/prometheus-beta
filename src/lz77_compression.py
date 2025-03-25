class LZ77Compressor:
    """
    Implements the LZ77 compression algorithm.
    
    LZ77 is a dictionary coding compression algorithm that replaces 
    repeated occurrences of data with references to a single copy of that data.
    """
    
    def compress(self, data):
        """
        Compress the input data using LZ77 compression algorithm.
        
        Args:
            data (str or bytes): The input data to compress
        
        Returns:
            list: Compressed data as a list of tuples (offset, length, next_char)
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return []
        
        compressed = []
        window_size = 4096  # Standard sliding window size
        
        # Start of the data, no previous matches
        start_index = 0
        current_index = 0
        
        while current_index < len(data):
            # Find the longest match in the search window
            best_length = 0
            best_offset = 0
            
            # Look back in the window for the longest match
            search_start = max(0, current_index - window_size)
            for offset in range(current_index - search_start, 0, -1):
                match_length = 0
                
                # Check how long the match continues
                while (current_index + match_length < len(data) and 
                       match_length < 255 and 
                       data[current_index - offset + match_length] == data[current_index + match_length]):
                    match_length += 1
                
                # Update best match if needed
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset
            
            # If no match found, output the current character
            if best_length == 0:
                compressed.append((0, 0, data[current_index]))
                current_index += 1
            else:
                # Output the match
                compressed.append((best_offset, best_length, 
                                   data[current_index + best_length] 
                                   if current_index + best_length < len(data) 
                                   else 0))
                current_index += best_length + 1
        
        return compressed
    
    def decompress(self, compressed):
        """
        Decompress data compressed with the LZ77 algorithm.
        
        Args:
            compressed (list): Compressed data as list of tuples 
                               (offset, length, next_char)
        
        Returns:
            bytes: Decompressed data
        """
        # Validate input
        if not compressed:
            return b''
        
        decompressed = bytearray()
        
        for offset, length, next_char in compressed:
            if offset == 0 and length == 0:
                # Literal character
                decompressed.append(next_char)
            else:
                # Copy from previous data
                start = len(decompressed) - offset
                
                # Copy the matched sequence
                for _ in range(length):
                    decompressed.append(decompressed[start])
                    start += 1
                
                # Append the next character if it's not a null terminator
                if next_char != 0:
                    decompressed.append(next_char)
        
        return bytes(decompressed)