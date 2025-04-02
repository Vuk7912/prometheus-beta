def get_char_frequency(input_string):
    """
    Calculate the frequency of characters in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Create a frequency dictionary
    char_freq = {}
    
    # Count frequency of each character
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    return char_freq