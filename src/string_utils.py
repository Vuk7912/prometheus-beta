def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotate a string by a specified number of positions and then reverse it.
    
    Args:
        string (str): The input string to be rotated and reversed.
        rotations (int): Number of positions to rotate the string.
    
    Returns:
        str: The rotated and reversed string.
    
    Raises:
        TypeError: If input is not a string or rotations is not an integer.
        ValueError: If rotations is negative.
    
    Examples:
        >>> rotate_and_reverse("hello", 2)
        'olleh'
        >>> rotate_and_reverse("python", 3)
        'nohtyp'
    """
    # Validate inputs
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(rotations, int):
        raise TypeError("Rotations must be an integer")
    
    if rotations < 0:
        raise ValueError("Rotations cannot be negative")
    
    # If string is empty, return empty string
    if not string:
        return ""
    
    # First reverse the entire string
    reversed_string = string[::-1]
    
    # Normalize rotations to be within string length
    effective_rotations = rotations % len(string)
    
    # Then rotate the reversed string
    rotated = reversed_string[effective_rotations:] + reversed_string[:effective_rotations]
    
    return rotated