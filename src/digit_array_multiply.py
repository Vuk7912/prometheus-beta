def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.
    
    Args:
        A (list): First array of digits 
        B (list): Second array of digits of the same length as A
    
    Returns:
        list: Array of digits representing the product of the two input numbers
    
    Raises:
        ValueError: If input arrays are not of equal length or contain non-digit values
    """
    # Validate input
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Validate digits
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise ValueError("All elements must be single digits (0-9)")
    
    # Convert arrays to integers
    num_a = int(''.join(map(str, A)))
    num_b = int(''.join(map(str, B)))
    
    # Multiply and convert back to array of digits
    product = num_a * num_b
    
    # Convert product to array of digits
    return [int(digit) for digit in str(product)]