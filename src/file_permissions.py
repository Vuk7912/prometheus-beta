import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions of a given file.

    Args:
        file_path (str): Path to the file whose permissions are to be retrieved.

    Returns:
        dict: A dictionary containing file permission details including:
            - 'numeric': Numeric representation of file permissions (e.g., 644)
            - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
            - 'owner_read': Boolean indicating if owner can read
            - 'owner_write': Boolean indicating if owner can write
            - 'owner_execute': Boolean indicating if owner can execute
            - 'group_read': Boolean indicating if group can read
            - 'group_write': Boolean indicating if group can write
            - 'group_execute': Boolean indicating if group can execute
            - 'others_read': Boolean indicating if others can read
            - 'others_write': Boolean indicating if others can write
            - 'others_execute': Boolean indicating if others can execute

    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If the file cannot be accessed
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Get file stats
        file_stats = os.stat(file_path)
        
        # Extract permission mode
        mode = file_stats.st_mode
        
        # Convert to numeric permissions (e.g., 644)
        numeric_perms = stat.S_IMODE(mode)
        
        # Create readable permission string
        readable_perms = '-' * 9
        perms_list = list(readable_perms)
        
        # Owner permissions
        perms_list[0] = 'r' if mode & stat.S_IRUSR else '-'
        perms_list[1] = 'w' if mode & stat.S_IWUSR else '-'
        perms_list[2] = 'x' if mode & stat.S_IXUSR else '-'
        
        # Group permissions
        perms_list[3] = 'r' if mode & stat.S_IRGRP else '-'
        perms_list[4] = 'w' if mode & stat.S_IWGRP else '-'
        perms_list[5] = 'x' if mode & stat.S_IXGRP else '-'
        
        # Others permissions
        perms_list[6] = 'r' if mode & stat.S_IROTH else '-'
        perms_list[7] = 'w' if mode & stat.S_IWOTH else '-'
        perms_list[8] = 'x' if mode & stat.S_IXOTH else '-'
        
        readable_perms = ''.join(perms_list)
        
        return {
            'numeric': numeric_perms,
            'readable': readable_perms,
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file permissions: {str(e)}")