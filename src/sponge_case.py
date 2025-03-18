def to_sponge_case(text):
    """
    Convert a string to alternating sponge case.
    
    Sponge case alternates between uppercase and lowercase letters,
    starting with an uppercase letter. Non-alphabetic characters 
    are preserved in their original form.
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_sponge_case("hello world")
        'HeLlO wOrLd'
        >>> to_sponge_case("python")
        'PyThOn'
        >>> to_sponge_case("")
        ''
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return as is
    if not text:
        return text
    
    # Convert to sponge case
    result = []
    should_uppercase = True
    
    for char in text:
        if char.isalpha():
            # Alternate case for alphabetic characters
            if should_uppercase:
                result.append(char.upper())
            else:
                result.append(char.lower())
            should_uppercase = not should_uppercase
        else:
            # Preserve non-alphabetic characters as-is
            result.append(char)
    
    return ''.join(result)