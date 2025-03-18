def fibonacci(max_num):
    """
    Generate Fibonacci sequence up to a given maximum number.
    
    Args:
        max_num (int): The maximum number to generate Fibonacci sequence up to.
    
    Returns:
        list: A list of Fibonacci numbers less than or equal to max_num.
    
    Raises:
        ValueError: If max_num is negative.
    """
    if max_num < 0:
        raise ValueError("Maximum number must be non-negative")
    
    # Handle special cases
    if max_num == 0:
        return []
    if max_num == 1:
        return [1]
    
    # Generate Fibonacci sequence
    fib_seq = [1, 1]
    while True:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > max_num:
            break
        fib_seq.append(next_num)
    
    return fib_seq

def fibonacci_sum(numbers):
    """
    Calculate the sum of Fibonacci sequence up to the largest number in the input array.
    
    Args:
        numbers (list): A list of positive integers.
    
    Returns:
        int: Sum of Fibonacci numbers up to the largest number in the input.
    
    Raises:
        ValueError: If the input contains non-positive numbers.
    """
    # Validate input
    if not numbers:
        return 0
    
    # Check for non-positive numbers
    if any(num <= 0 for num in numbers):
        raise ValueError("All input numbers must be positive")
    
    # Find the largest number
    max_num = max(numbers)
    
    # Generate Fibonacci sequence and sum it
    fib_seq = fibonacci(max_num)
    return sum(fib_seq)