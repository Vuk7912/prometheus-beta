def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string is a valid IP address in the format "A.B.C.D"
    where A, B, C, and D are single-digit numeric characters between 0 and 9.

    Args:
        ip_string (str): The input string to validate as an IP address

    Returns:
        bool: True if the string is a valid IP address, False otherwise

    Examples:
        >>> validate_ip_address("1.2.3.4")
        True
        >>> validate_ip_address("9.9.9.9")
        True
        >>> validate_ip_address("0.0.0.0")
        True
        >>> validate_ip_address("10.20.30.40")
        False
        >>> validate_ip_address("1.2.3.4.")
        False
        >>> validate_ip_address(".1.2.3.4")
        False
        >>> validate_ip_address("1.2.3")
        False
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the string by dots
    parts = ip_string.split('.')
    
    # Check if exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Check each part
    for part in parts:
        # Check if part is a single digit
        if len(part) != 1:
            return False
        
        # Check if part is a digit between 0 and 9
        if not part.isdigit():
            return False
    
    return True