def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.

    This function takes a string and converts it to CONSTANT_CASE by:
    1. Removing leading/trailing whitespaces
    2. Replacing non-alphanumeric characters with underscores
    3. Converting the string to uppercase
    4. Removing consecutive underscores

    Args:
        input_string (str): The input string to convert

    Returns:
        str: The input string converted to CONSTANT_CASE

    Raises:
        TypeError: If the input is not a string
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading and trailing whitespaces
    input_string = input_string.strip()
    
    # If input is empty after stripping, return empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric characters with underscores
    import re
    converted = re.sub(r'[^a-zA-Z0-9]+', '_', input_string)
    
    # Convert to uppercase
    converted = converted.upper()
    
    # Remove consecutive underscores
    converted = re.sub(r'_+', '_', converted)
    
    # Remove leading or trailing underscores
    converted = converted.strip('_')
    
    return converted