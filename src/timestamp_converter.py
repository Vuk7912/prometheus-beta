from datetime import datetime, timezone

def timestamp_to_human_readable(timestamp):
    """
    Convert a numeric timestamp to a human-readable date string.

    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)

    Returns:
        str: Formatted date string in the format 'YYYY-MM-DD HH:MM:SS UTC'

    Raises:
        TypeError: If timestamp is not a number
        ValueError: If timestamp is negative or out of valid range
    """
    # Validate input type
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number")
    
    # Validate timestamp value
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    try:
        # Convert timestamp to datetime object in UTC
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        
        # Format the datetime as a human-readable string
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    except (OSError, OverflowError):
        raise ValueError("Timestamp is out of valid range")