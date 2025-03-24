import requests
from typing import Dict, Any, Optional

def send_http_get_request(url: str, 
                           headers: Optional[Dict[str, str]] = None, 
                           timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): Optional headers to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.
            - 'status_code': HTTP status code of the response
            - 'content': Response content as text
            - 'headers': Response headers
            - 'json': JSON response if applicable (None otherwise)

    Raises:
        ValueError: If the URL is empty or invalid
        requests.RequestException: For network-related errors
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: Must be a non-empty string")

    try:
        # Send GET request
        response = requests.get(
            url, 
            headers=headers or {}, 
            timeout=timeout
        )
        
        # Raise exception for bad HTTP status codes
        response.raise_for_status()

        # Attempt to parse JSON, return None if not possible
        try:
            json_response = response.json()
        except ValueError:
            json_response = None

        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers),
            'json': json_response
        }

    except requests.RequestException as e:
        # Catch and re-raise network-related exceptions
        raise requests.RequestException(f"HTTP GET request failed: {str(e)}") from e