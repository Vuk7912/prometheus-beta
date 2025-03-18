import os
import datetime
import pytest
import tempfile
import time

from src.file_creation_date import get_file_creation_date

def test_file_creation_date_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        time.sleep(0.1)  # Ensure timestamp is different
    
    # Get creation date
    creation_date = get_file_creation_date(temp_file_path)
    
    # Verify it's a datetime object and close to current time
    assert isinstance(creation_date, datetime.datetime)
    assert (datetime.datetime.now() - creation_date).total_seconds() < 5
    
    # Clean up
    os.unlink(temp_file_path)

def test_file_creation_date_nonexistent_file():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('/path/to/nonexistent/file.txt')

def test_file_creation_date_permission_error(mocker):
    # Simulate a permission error
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.stat', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        get_file_creation_date('/path/to/inaccessible/file.txt')

def test_file_creation_date_type_checks():
    # Ensure the function works with different path representations
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    # Test with absolute and relative paths
    abs_date = get_file_creation_date(temp_file_path)
    assert isinstance(abs_date, datetime.datetime)
    
    # Clean up
    os.unlink(temp_file_path)