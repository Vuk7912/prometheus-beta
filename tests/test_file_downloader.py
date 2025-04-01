import os
import pytest
import requests
import tempfile
from unittest.mock import MagicMock
from src.file_downloader import download_file

def test_download_file_success(monkeypatch):
    """Test successful file download."""
    # Create a temp directory for downloads
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a mock response
        mock_response = MagicMock()
        mock_response.content = b'Hello, World!'
        mock_response.iter_content.return_value = [b'Hello, ', b'World!']
        mock_response.headers = {}
        mock_response.raise_for_status = MagicMock()
        
        # Patch requests.get to return the mock response
        def mock_get(url, stream=True):
            return mock_response
        
        monkeypatch.setattr(requests, 'get', mock_get)

        # Perform download
        test_url = 'https://example.com/test.txt'
        downloaded_file = download_file(test_url, destination_folder=tmpdir)

        # Verify file was downloaded correctly
        assert os.path.exists(downloaded_file)
        with open(downloaded_file, 'rb') as f:
            assert f.read() == b'Hello, World!'

def test_download_file_empty_url():
    """Test that an empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        download_file("")
    with pytest.raises(ValueError, match="URL cannot be empty"):
        download_file("  ")

def test_download_file_invalid_url(monkeypatch):
    """Test handling of invalid URLs."""
    # Create a mock response that raises an exception
    def mock_get(url, stream=True):
        response = MagicMock()
        response.raise_for_status.side_effect = requests.RequestException("Invalid URL")
        return response
    
    monkeypatch.setattr(requests, 'get', mock_get)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_url = 'https://nonexistent.example.com/file.txt'
        with pytest.raises(requests.RequestException):
            download_file(test_url, destination_folder=tmpdir)

def test_download_file_default_destination(monkeypatch):
    """Test download with default destination."""
    # Create a temp directory as current working directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change current working directory
        original_cwd = os.getcwd()
        os.chdir(tmpdir)

        try:
            # Create a mock response
            mock_response = MagicMock()
            mock_response.content = b'Hello, World!'
            mock_response.iter_content.return_value = [b'Hello, ', b'World!']
            mock_response.headers = {}
            mock_response.raise_for_status = MagicMock()
            
            # Patch requests.get to return the mock response
            def mock_get(url, stream=True):
                return mock_response
            
            monkeypatch.setattr(requests, 'get', mock_get)

            # Perform download
            test_url = 'https://example.com/test.txt'
            downloaded_file = download_file(test_url)

            # Verify file was downloaded to current directory
            assert os.path.exists(downloaded_file)
            assert os.path.dirname(downloaded_file) == tmpdir
        finally:
            # Restore original working directory
            os.chdir(original_cwd)

def test_download_file_filename_extraction(monkeypatch):
    """Test filename extraction from different sources."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Track which response to use
        mock_responses = []
        
        # Test URL-based filename
        url1 = 'https://example.com/files/document.pdf'
        mock_response1 = MagicMock()
        mock_response1.content = b'PDF content'
        mock_response1.iter_content.return_value = [b'PDF content']
        mock_response1.headers = {}
        mock_response1.raise_for_status = MagicMock()
        mock_responses.append(mock_response1)
        
        # Test Content-Disposition filename
        url2 = 'https://example.com/download'
        mock_response2 = MagicMock()
        mock_response2.content = b'Attachment content'
        mock_response2.iter_content.return_value = [b'Attachment content']
        mock_response2.headers = {'Content-Disposition': 'attachment; filename="custom.txt"'}
        mock_response2.raise_for_status = MagicMock()
        mock_responses.append(mock_response2)
        
        # Patch requests.get to return mock responses
        def mock_get(url, stream=True):
            return mock_responses.pop(0)
        
        monkeypatch.setattr(requests, 'get', mock_get)

        # URL-based filename
        file1 = download_file(url1, destination_folder=tmpdir)
        assert os.path.basename(file1) == 'document.pdf'

        # Content-Disposition filename
        file2 = download_file(url2, destination_folder=tmpdir)
        assert os.path.basename(file2) == 'custom.txt'