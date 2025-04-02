import lzma
import os
from typing import Union

def compress_xz(input_data: Union[str, bytes], output_path: str = None) -> Union[bytes, None]:
    """
    Compress data using XZ compression algorithm.

    Args:
        input_data (Union[str, bytes]): Data to be compressed. 
            Can be a string or bytes object.
        output_path (str, optional): Path to save compressed file. 
            If None, returns compressed bytes.

    Returns:
        Union[bytes, None]: Compressed data as bytes if no output_path, 
        otherwise None (file is saved directly)

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
        IOError: If there's an issue writing to the output file
    """
    # Validate input
    if not isinstance(input_data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert string to bytes if needed
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Check for empty input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data
    compressed_data = lzma.compress(input_data)
    
    # If output path is provided, save to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
            return None
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    
    return compressed_data

def decompress_xz(input_data: Union[str, bytes], output_path: str = None) -> Union[bytes, str]:
    """
    Decompress XZ compressed data.

    Args:
        input_data (Union[str, bytes]): Compressed data to decompress. 
            Can be bytes or path to a compressed file.
        output_path (str, optional): Path to save decompressed file. 
            If None, returns decompressed data.

    Returns:
        Union[bytes, str]: Decompressed data as bytes or saved to file

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
        lzma.LZMAError: If data cannot be decompressed
        IOError: If there's an issue writing to the output file
    """
    # Handle file input
    if isinstance(input_data, str) and os.path.isfile(input_data):
        try:
            with open(input_data, 'rb') as f:
                input_data = f.read()
        except IOError as e:
            raise IOError(f"Error reading file {input_data}: {e}")
    
    # Validate input
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or a valid file path")
    
    # Check for empty input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompress the data
    try:
        decompressed_data = lzma.decompress(input_data)
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Cannot decompress data: {e}")
    
    # If output path is provided, save to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
            return None
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    
    # Try to decode to string if possible, otherwise return bytes
    try:
        return decompressed_data.decode('utf-8')
    except UnicodeDecodeError:
        return decompressed_data