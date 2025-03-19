def reverse_substring(string: str, start: int, end: int) -> str:
    """
    Reverse a substring within a given string.

    Args:
        string (str): The input string to modify.
        start (int): The starting index of the substring to reverse (inclusive).
        end (int): The ending index of the substring to reverse (exclusive).

    Returns:
        str: A new string with the specified substring reversed.

    Raises:
        ValueError: If start or end indices are out of bounds.
        ValueError: If start index is greater than end index.
    """
    # Handle empty string as a special case
    if not string:
        if start == 0 and end == 0:
            return ""
        raise ValueError("Indices out of string bounds")
    
    # Validate input indices
    if start < 0 or end < 0:
        raise ValueError("Indices must be non-negative")
    
    if start >= len(string) or end > len(string):
        raise ValueError("Indices out of string bounds")
    
    if start > end:
        raise ValueError("Start index must be less than or equal to end index")
    
    # If no reversal needed, return original string
    if start == end:
        return string
    
    # Split the string into three parts and reconstruct
    prefix = string[:start]
    substring = string[start:end]
    suffix = string[end:]
    
    # Reverse the specified substring
    reversed_substring = substring[::-1]
    
    # Combine the parts
    return prefix + reversed_substring + suffix