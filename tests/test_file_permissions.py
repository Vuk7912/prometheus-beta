import os
import pytest
import stat
import tempfile

from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file():
    # Create a temporary file with specific permissions
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Change file permissions to 644
        os.chmod(temp_file.name, 0o644)
        
        # Get file permissions
        perms = get_file_permissions(temp_file.name)
        
        # Assertions
        assert perms['numeric'] == 0o644
        assert perms['readable'] == 'rw-r--r--'
        assert perms['owner_read'] is True
        assert perms['owner_write'] is True
        assert perms['owner_execute'] is False
        assert perms['group_read'] is True
        assert perms['group_write'] is False
        assert perms['group_execute'] is False
        assert perms['others_read'] is True
        assert perms['others_write'] is False
        assert perms['others_execute'] is False
    
    # Clean up the temporary file
    os.unlink(temp_file.name)

def test_get_file_permissions_all_permissions():
    # Create a temporary file with all permissions
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Change file permissions to 777
        os.chmod(temp_file.name, 0o777)
        
        # Get file permissions
        perms = get_file_permissions(temp_file.name)
        
        # Assertions
        assert perms['numeric'] == 0o777
        assert perms['readable'] == 'rwxrwxrwx'
        assert perms['owner_read'] is True
        assert perms['owner_write'] is True
        assert perms['owner_execute'] is True
        assert perms['group_read'] is True
        assert perms['group_write'] is True
        assert perms['group_execute'] is True
        assert perms['others_read'] is True
        assert perms['others_write'] is True
        assert perms['others_execute'] is True
    
    # Clean up the temporary file
    os.unlink(temp_file.name)

def test_get_file_permissions_no_permissions():
    # Create a temporary file with no permissions
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Change file permissions to 000
        os.chmod(temp_file.name, 0o000)
        
        # Get file permissions
        perms = get_file_permissions(temp_file.name)
        
        # Assertions
        assert perms['numeric'] == 0o000
        assert perms['readable'] == '---------'
        assert perms['owner_read'] is False
        assert perms['owner_write'] is False
        assert perms['owner_execute'] is False
        assert perms['group_read'] is False
        assert perms['group_write'] is False
        assert perms['group_execute'] is False
        assert perms['others_read'] is False
        assert perms['others_write'] is False
        assert perms['others_execute'] is False
    
    # Clean up the temporary file
    os.unlink(temp_file.name)

def test_get_file_permissions_non_existent_file():
    # Test for non-existent file
    with pytest.raises(FileNotFoundError, match="File not found"):
        get_file_permissions('/path/to/non/existent/file.txt')

def test_get_file_permissions_unreadable_file(mocker):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Patch os.stat to raise a PermissionError
        mocker.patch('os.stat', side_effect=PermissionError("Permission denied"))
        
        # Expect a PermissionError to be raised
        with pytest.raises(PermissionError, match="Permission denied"):
            get_file_permissions(temp_file.name)
    
    # Clean up the temporary file
    os.unlink(temp_file.name)