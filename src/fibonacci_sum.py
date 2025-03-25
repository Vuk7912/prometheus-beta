def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to sum.
    
    Returns:
        int: The sum of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return 0  # First Fibonacci number is 0
    if n == 2:
        return 1  # Sum of first two Fibonacci numbers (0 + 1)
    
    # Initialize Fibonacci sequence variables
    a, b = 0, 1
    fibonacci_sum_result = a + b
    
    # Iterate to calculate sum of first n Fibonacci numbers
    for _ in range(3, n + 1):
        a, b = b, a + b
        fibonacci_sum_result += b
    
    return fibonacci_sum_result