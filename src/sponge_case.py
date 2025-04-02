def to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case (alternating uppercase and lowercase).
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello world")
        'HeLlO WoRlD'
        >>> to_sponge_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Track alpha character count to determine case
    alpha_count = 0
    result = []
    
    for char in text:
        if char.isalpha():
            # Alternate case for alphabetic characters
            result.append(char.upper() if alpha_count % 2 == 0 else char.lower())
            alpha_count += 1
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)