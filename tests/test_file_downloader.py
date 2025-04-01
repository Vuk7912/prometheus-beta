import os
import pytest
import requests
import tempfile
from src.file_downloader import download_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for downloads."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

def test_download_file_success(requests_mock, temp_dir):
    """Test successful file download."""
    # Mock the URL and response
    test_url = 'https://example.com/test.txt'
    test_content = b'Hello, World!'
    requests_mock.get(test_url, content=test_content)

    # Perform download
    downloaded_file = download_file(test_url, destination_folder=temp_dir)

    # Verify file was downloaded correctly
    assert os.path.exists(downloaded_file)
    with open(downloaded_file, 'rb') as f:
        assert f.read() == test_content

def test_download_file_empty_url():
    """Test that an empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        download_file("")
    with pytest.raises(ValueError, match="URL cannot be empty"):
        download_file("  ")

def test_download_file_invalid_url(requests_mock, temp_dir):
    """Test handling of invalid URLs."""
    test_url = 'https://nonexistent.example.com/file.txt'
    requests_mock.get(test_url, status_code=404)

    with pytest.raises(requests.RequestException):
        download_file(test_url, destination_folder=temp_dir)

def test_download_file_default_destination(requests_mock):
    """Test download with default destination."""
    # Create a temp directory as current working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change current working directory
        original_cwd = os.getcwd()
        os.chdir(tmpdir)

        try:
            # Mock the URL and response
            test_url = 'https://example.com/test.txt'
            test_content = b'Hello, World!'
            requests_mock.get(test_url, content=test_content)

            # Perform download
            downloaded_file = download_file(test_url)

            # Verify file was downloaded to current directory
            assert os.path.exists(downloaded_file)
            assert os.path.dirname(downloaded_file) == tmpdir
        finally:
            # Restore original working directory
            os.chdir(original_cwd)

def test_download_file_filename_extraction(requests_mock, temp_dir):
    """Test filename extraction from different sources."""
    # Test URL-based filename
    url1 = 'https://example.com/files/document.pdf'
    requests_mock.get(url1, content=b'PDF content')
    
    # Test Content-Disposition filename
    url2 = 'https://example.com/download'
    requests_mock.get(url2, 
                      content=b'Attachment content', 
                      headers={'Content-Disposition': 'attachment; filename="custom.txt"'})

    # URL-based filename
    file1 = download_file(url1, destination_folder=temp_dir)
    assert os.path.basename(file1) == 'document.pdf'

    # Content-Disposition filename
    file2 = download_file(url2, destination_folder=temp_dir)
    assert os.path.basename(file2) == 'custom.txt'