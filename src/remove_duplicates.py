def remove_duplicates(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.

    Args:
        input_string (str): The input string from which duplicates should be removed.

    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence of each character.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a set to track seen characters while preserving order
    seen = set()
    result = []
    
    for char in input_string:
        # Check lowercase to track duplicates
        lower_char = char.lower()
        if lower_char not in seen:
            seen.add(lower_char)
            result.append(char)
    
    return ''.join(result)