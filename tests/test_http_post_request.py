import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

def test_send_http_post_request_success():
    """Test successful POST request"""
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_response.headers = {'Content-Type': 'application/json'}
        
        # Call the function
        result = send_http_post_request('https://example.com', {'test': 'data'})
        
        # Verify result
        assert result['status_code'] == 200
        assert result['json'] == {'key': 'value'}
        assert 'Content-Type' in result['headers']

def test_send_http_post_request_empty_url():
    """Test raising ValueError for empty URL"""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        send_http_post_request('')

def test_send_http_post_request_network_error():
    """Test handling network-related exceptions"""
    with patch('requests.post') as mock_post:
        # Simulate a network error
        mock_post.side_effect = requests.RequestException("Network error")
        
        with pytest.raises(requests.RequestException, match="POST request failed"):
            send_http_post_request('https://example.com')

def test_send_http_post_request_custom_headers():
    """Test sending custom headers"""
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        
        # Call with custom headers
        send_http_post_request(
            'https://example.com', 
            headers={'Authorization': 'Bearer token'}
        )
        
        # Verify headers were passed correctly
        mock_post.assert_called_once_with(
            'https://example.com', 
            json=None, 
            headers={'Authorization': 'Bearer token'}, 
            timeout=10
        )

def test_send_http_post_request_no_json_response():
    """Test handling responses without JSON content"""
    with patch('requests.post') as mock_post:
        # Mock a response without JSON
        mock_response = mock_post.return_value
        mock_response.status_code = 204
        mock_response.json.side_effect = ValueError()
        mock_response.content = b''
        
        result = send_http_post_request('https://example.com')
        
        assert result['status_code'] == 204
        assert result['json'] == {}