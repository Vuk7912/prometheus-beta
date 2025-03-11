import os
import pathlib

def delete_file(file_path):
    """
    Delete a file from the given path.

    Args:
        file_path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
        ValueError: If the file_path is None or an empty string.
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be None or empty")
    
    # Convert to absolute path and resolve any symbolic links
    abs_path = str(pathlib.Path(file_path).resolve())
    
    # Check if file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")
    
    # Ensure it's a file, not a directory
    if os.path.isdir(abs_path):
        raise IsADirectoryError(f"Path is a directory, not a file: {abs_path}")
    
    # Attempt to delete the file
    try:
        os.remove(abs_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete file {abs_path}")