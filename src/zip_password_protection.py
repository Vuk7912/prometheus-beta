import os
import zipfile
from typing import Union, List


def create_password_protected_zip(source_files: Union[str, List[str]], 
                                   output_zip_path: str, 
                                   password: str) -> bool:
    """
    Create a password-protected zip file from given source files.

    Args:
        source_files (Union[str, List[str]]): Path(s) to file(s) to be zipped
        output_zip_path (str): Path where the zip file will be created
        password (str): Password to protect the zip file

    Returns:
        bool: True if zip creation is successful, False otherwise

    Raises:
        ValueError: If source files are invalid or password is empty
        OSError: If there are issues with file access or writing
    """
    # Validate inputs
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Convert single file to list if needed
    if isinstance(source_files, str):
        source_files = [source_files]
    
    # Validate source files exist
    for file_path in source_files:
        if not os.path.exists(file_path):
            raise ValueError(f"Source file does not exist: {file_path}")
    
    try:
        # Create zip file with password protection
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in source_files:
                # Add file to zip with its basename to preserve directory structure
                zipf.write(file_path, os.path.basename(file_path))
                
            # Set password for the entire archive
            zipf.setpassword(password.encode('utf-8'))
        
        return True
    except (IOError, OSError) as e:
        # Log or handle specific file operation errors
        raise OSError(f"Error creating zip file: {str(e)}")