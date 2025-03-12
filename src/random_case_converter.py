import random

def convert_to_random_case(input_string: str) -> str:
    """
    Convert a given string to random case, randomly making each character 
    either uppercase or lowercase.
    
    Args:
        input_string (str): The input string to be converted to random case.
    
    Returns:
        str: A new string with randomly cased characters.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_random_case("hello")
        # Possible output: "HeLlO" or "hELLo" etc.
        >>> convert_to_random_case("")
        ''
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert empty string directly
    if not input_string:
        return ""
    
    # Convert each character to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )