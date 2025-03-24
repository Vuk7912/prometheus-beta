import pytest
import requests
from unittest.mock import patch
from src.http_get_request import send_http_get_request

# Use a test API endpoint that's reliable for testing
TEST_URL = "https://jsonplaceholder.typicode.com/posts/1"
INVALID_URL = "http://invalid-url-that-does-not-exist.xyz"

def test_successful_get_request():
    """Test a successful GET request"""
    result = send_http_get_request(TEST_URL)
    
    assert result['status_code'] == 200
    assert 'id' in result['json']
    assert len(result['content']) > 0
    assert isinstance(result['headers'], dict)

def test_request_with_headers():
    """Test GET request with custom headers"""
    headers = {'User-Agent': 'TestAgent'}
    result = send_http_get_request(TEST_URL, headers=headers)
    
    assert result['status_code'] == 200

def test_invalid_url_raises_error():
    """Test that an invalid URL raises a ValueError"""
    with pytest.raises(ValueError):
        send_http_get_request("")
    
    with pytest.raises(ValueError):
        send_http_get_request(None)

@patch('requests.get')
def test_network_error_handling(mock_get):
    """Test handling of network-related exceptions"""
    mock_get.side_effect = requests.ConnectionError("Connection failed")
    
    with pytest.raises(requests.RequestException):
        send_http_get_request(INVALID_URL)

def test_timeout_handling():
    """Test request timeout"""
    with pytest.raises(requests.RequestException):
        send_http_get_request(INVALID_URL, timeout=1)

def test_json_parsing():
    """Test JSON parsing with non-JSON response"""
    # Using a text endpoint
    text_url = "https://httpbin.org/get"
    result = send_http_get_request(text_url)
    
    assert result['status_code'] == 200
    assert result['json'] is not None  # httpbin returns JSON