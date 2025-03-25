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
    
    # If only one word, return capitalized
    if len(words) == 1:
        return words[0].capitalize()
    
    # Capitalize all words, preserving original casing where possible
    capitalized_words = [
        word.capitalize() if not word.isupper() 
        else word for word in words
    ]
    
    # Construct the final alternating pattern
    result = []
    for i, word in enumerate(capitalized_words):
        # Even indices (0, 2, 4...) keep original word
        # Odd indices (1, 3, 5...) get lowercased
        result.append(word if i % 2 == 0 else word.lower())
    
    # Always add the first word (fully capitalized) at the end
    result.append(capitalized_words[0])
    
    return ''.join(result)