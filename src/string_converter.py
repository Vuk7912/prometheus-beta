def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.

    This function takes a string and converts it to CONSTANT_CASE by:
    1. Removing leading/trailing whitespaces
    2. Converting camelCase or PascalCase to snake_case first
    3. Replacing non-alphanumeric characters with underscores
    4. Converting the string to uppercase
    5. Removing consecutive underscores

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
    
    import re
    
    # Convert camelCase/PascalCase to snake_case
    # Insert underscore before any uppercase letter that follows a lowercase letter or number
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    s2 = re.sub('([a-z])([0-9])', r'\1_\2', s1)  # Separate letters from numbers
    s3 = re.sub('([0-9])([A-Z])', r'\1_\2', s2)  # Separate numbers from uppercase letters
    s4 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s3)
    
    # Replace non-alphanumeric characters with underscores
    converted = re.sub(r'[^a-zA-Z0-9]+', '_', s4)
    
    # Convert to uppercase
    converted = converted.upper()
    
    # Remove consecutive underscores
    converted = re.sub(r'_+', '_', converted)
    
    # Remove leading or trailing underscores
    converted = converted.strip('_')
    
    return converted