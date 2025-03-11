import os
import pytest
import tempfile
import pathlib

from src.file_operations import delete_file

def test_delete_file_success():
    """Test successful file deletion."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"test content")
        temp_file.close()
        
        # Verify file exists before deletion
        assert os.path.exists(temp_path)
        
        # Delete the file
        delete_file(temp_path)
        
        # Verify file is deleted
        assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    """Test deleting a file that does not exist."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_file = os.path.join(temp_dir, "nonexistent.txt")
        
        with pytest.raises(FileNotFoundError):
            delete_file(nonexistent_file)

def test_delete_empty_path():
    """Test deleting with an empty path."""
    with pytest.raises(ValueError):
        delete_file("")
    
    with pytest.raises(ValueError):
        delete_file(None)

def test_delete_directory():
    """Test attempting to delete a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

def test_relative_path_deletion():
    """Test deletion using a relative path."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"test content")
        temp_file.close()
        
        # Get relative path
        relative_path = os.path.relpath(temp_path)
        
        # Delete using relative path
        delete_file(relative_path)
        
        # Verify file is deleted
        assert not os.path.exists(temp_path)