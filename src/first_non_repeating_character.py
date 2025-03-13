def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a given string.

    Args:
        s (str): Input string containing only lowercase letters.

    Returns:
        str | None: The first non-repeating character, or None if no such character exists.

    Raises:
        ValueError: If the input contains characters other than lowercase letters.
    """
    # Validate input 
    if not s.islower():
        raise ValueError("Input string must contain only lowercase letters")
    
    # Count occurrences of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the first character with count 1
    for char in s:
        if char_counts[char] == 1:
            return char
    
    # If no non-repeating character found
    return None