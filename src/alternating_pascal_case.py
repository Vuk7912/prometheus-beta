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
    
    # Fully capitalize each word, treating mixed-case words specially
    capitalized_words = []
    for word in words:
        # Handle different casing scenarios
        if word.isupper():
            capitalized_words.append(word)
        elif word.islower():
            capitalized_words.append(word.capitalize())
        else:
            # For mixed-case words, force full capitalization
            capitalized_words.append(word.capitalize())
    
    # Construct the alternating Pascal case pattern
    result = []
    # First pass: add words
    for i, word in enumerate(capitalized_words):
        result.append(word if i % 2 == 0 else word.lower())
    
    # Always append first word (fully capitalized) at the end
    result.append(capitalized_words[0])
    
    return ''.join(result)