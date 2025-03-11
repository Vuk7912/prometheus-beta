import os
import zipfile
import pytest
from src.zip_password_protection import create_password_protected_zip


@pytest.fixture
def sample_file(tmp_path):
    """Create a sample text file for testing"""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("This is a test file")
    return str(test_file)


def test_create_single_file_zip(sample_file, tmp_path):
    """Test creating a zip with a single file"""
    output_zip = str(tmp_path / "protected.zip")
    password = "secret123"
    
    # Create zip
    result = create_password_protected_zip(sample_file, output_zip, password)
    
    # Verify zip creation
    assert result is True
    assert os.path.exists(output_zip)
    
    # Verify zip contents and password protection
    with zipfile.ZipFile(output_zip) as zf:
        # Check password
        try:
            zf.extractall(pwd=password.encode('utf-8'))
        except RuntimeError:
            pytest.fail("Password protection failed")
        
        # Verify file contents
        extracted_file = zf.namelist()[0]
        assert extracted_file == os.path.basename(sample_file)


def test_create_multiple_files_zip(sample_file, tmp_path):
    """Test creating a zip with multiple files"""
    # Create a second test file
    second_file = tmp_path / "second_test_file.txt"
    second_file.write_text("Another test file")
    
    output_zip = str(tmp_path / "multiple_files.zip")
    password = "secure456"
    
    # Create zip with multiple files
    result = create_password_protected_zip(
        [str(sample_file), str(second_file)], 
        output_zip, 
        password
    )
    
    # Verify zip creation
    assert result is True
    assert os.path.exists(output_zip)
    
    # Verify zip contents and password protection
    with zipfile.ZipFile(output_zip) as zf:
        # Check password
        try:
            zf.extractall(pwd=password.encode('utf-8'))
        except RuntimeError:
            pytest.fail("Password protection failed")
        
        # Verify file names
        file_names = zf.namelist()
        assert len(file_names) == 2
        assert os.path.basename(sample_file) in file_names
        assert os.path.basename(str(second_file)) in file_names


def test_empty_password_raises_error(sample_file, tmp_path):
    """Test that empty password raises ValueError"""
    output_zip = str(tmp_path / "invalid.zip")
    
    with pytest.raises(ValueError, match="Password cannot be empty"):
        create_password_protected_zip(sample_file, output_zip, "")


def test_nonexistent_file_raises_error(tmp_path):
    """Test that nonexistent file raises ValueError"""
    output_zip = str(tmp_path / "invalid.zip")
    
    with pytest.raises(ValueError, match="Source file does not exist"):
        create_password_protected_zip("/path/to/nonexistent/file.txt", output_zip, "password")