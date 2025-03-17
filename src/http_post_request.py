import requests
from typing import Dict, Any, Optional

def send_http_post_request(
    url: str, 
    data: Optional[Dict[str, Any]] = None, 
    headers: Optional[Dict[str, str]] = None, 
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL to send the POST request to.
        data (dict, optional): The payload to send with the request. Defaults to None.
        headers (dict, optional): Custom headers to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.

    Raises:
        ValueError: If the URL is empty or None.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url:
        raise ValueError("URL cannot be empty")

    # Prepare headers (use empty dict if None)
    request_headers = headers or {}

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=request_headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return response details
        return {
            'status_code': response.status_code,
            'json': response.json() if response.content else {},
            'headers': dict(response.headers)
        }

    except requests.RequestException as e:
        # Handle and re-raise request-related exceptions
        raise requests.RequestException(f"POST request failed: {str(e)}") from e