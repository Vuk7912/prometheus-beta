def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of unique characters in the string.
    
    Notes:
        - Characters are case-sensitive ('a' and 'A' are different)
        - Empty strings and whitespace-only strings return 0
    
    Examples:
        >>> count_unique_characters('hello')
        4
        >>> count_unique_characters('aAaA')
        2
        >>> count_unique_characters('')
        0
        >>> count_unique_characters('   ')
        0
    """
    # Handle empty or whitespace-only strings
    if not input_string or input_string.isspace():
        return 0
    
    # Use a set to count unique characters (preserves case sensitivity)
    return len(set(input_string))