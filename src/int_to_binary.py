def int_to_binary(number):
    """
    Convert a non-negative integer to its binary representation as a string.

    Args:
        number (int): A non-negative integer to convert to binary.

    Returns:
        str: A string representation of the binary number.

    Raises:
        ValueError: If the input is a negative integer.
        TypeError: If the input is not an integer.
    """
    # Validate input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Validate non-negative input
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for zero
    if number == 0:
        return "0"
    
    # Convert to binary
    binary = []
    while number > 0:
        binary.insert(0, str(number % 2))
        number //= 2
    
    return "".join(binary)