def remove_char_length(string: str, char: str) -> int:
    """
    Remove all instances of a specified character from a string and return its length.

    Args:
        string (str): The input string to process
        char (str): The character to remove from the string

    Returns:
        int: The length of the string after removing all instances of the specified character

    Raises:
        TypeError: If input is not a string or character is not a single character
        ValueError: If multiple characters are provided as character to remove
    """
    # Validate inputs
    if not isinstance(string, str) or not isinstance(char, str):
        raise TypeError("Both string and char must be strings")
    
    # Validate character input
    if len(char) != 1:
        raise ValueError("Character to remove must be a single character")
    
    # Remove the specified character and return the length
    return len(string.replace(char, ''))