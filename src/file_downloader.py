import os
import requests
from urllib.parse import urlparse

def download_file(url, destination_folder=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        destination_folder (str, optional): The folder where the file will be saved. 
                                            Defaults to current working directory.

    Returns:
        str: The full path to the downloaded file.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.RequestException: If there's an error downloading the file.
        IOError: If there are issues writing the file.
    """
    # Validate URL
    if not url or not url.strip():
        raise ValueError("URL cannot be empty")

    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Determine the destination folder
        if destination_folder is None:
            destination_folder = os.getcwd()
        
        # Ensure destination folder exists
        os.makedirs(destination_folder, exist_ok=True)
        
        # Extract filename from URL or Content-Disposition header
        filename = _extract_filename(response, url)
        
        # Create full file path
        file_path = os.path.join(destination_folder, filename)
        
        # Write the file
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        return file_path

    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")

def _extract_filename(response, url):
    """
    Extract filename from response headers or URL.

    Args:
        response (requests.Response): The response object.
        url (str): The original URL.

    Returns:
        str: Extracted filename.
    """
    # Try to get filename from Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition')
    if content_disposition:
        import re
        filename_match = re.findall('filename=(.+)', content_disposition)
        if filename_match:
            return filename_match[0].strip('"\'')
    
    # If no header, parse from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename found, use a default
    if not filename or filename == '/':
        filename = 'downloaded_file'
    
    return filename