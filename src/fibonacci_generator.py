def generate_fibonacci(n):
    """
    Generate the nth Fibonacci number using recursion.

    Args:
        n (int): The position of the Fibonacci number to generate.
                 Must be a positive integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is less than 1.
    """
    # Handle invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be a positive integer")
    
    # Handle edge cases
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # Recursive case
    return generate_fibonacci(n - 1) + generate_fibonacci(n - 2)