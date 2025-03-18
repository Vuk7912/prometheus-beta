import os
import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        datetime.datetime: The creation date of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Use platform-specific methods for creation time
        if os.name == 'nt':  # Windows
            creation_time = os.path.getctime(file_path)
        else:  # Unix-like systems
            stat = os.stat(file_path)
            try:
                creation_time = stat.st_birthtime  # macOS
            except AttributeError:
                creation_time = stat.st_mtime  # Fallback to modification time for Linux

        return datetime.datetime.fromtimestamp(creation_time)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot access {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error getting file creation date: {str(e)}")