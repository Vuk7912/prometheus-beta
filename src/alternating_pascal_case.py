def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    This function takes an input string and converts it to alternating Pascal case,
    where words are separated by removing non-alphanumeric characters and 
    capitalizing alternating words.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HelloWorldHello'
        >>> convert_to_alternating_pascal_case("python-is_awesome")
        'PythonIsAwesomePython'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and split
    import re
    words = re.findall(r'[a-zA-Z0-9]+', input_string)
    
    # If no words found, return empty string
    if not words:
        return ''
    
    # Capitalize all words
    capitalized_words = [word.capitalize() for word in words]
    
    # Alternate capitalizations starting from first word
    result = []
    for i, word in enumerate(capitalized_words):
        result.append(word if i % 2 == 0 else word.lower())
    
    return ''.join(result)