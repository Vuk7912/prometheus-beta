def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.

    Args:
        n (int): Number of terms to generate in the sequence.

    Returns:
        list: A list of n modified Fibonacci numbers.

    Raises:
        ValueError: If n is less than 0.
        TypeError: If input is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Handle special cases for small n
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Initialize the sequence with first two terms
    sequence = [0, 1]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Use the last two terms to generate the next term
        next_term = sequence[-1] + sequence[-2]
        
        # Ensure the sum of the last two terms is always odd
        if (sequence[-1] + sequence[-2]) % 2 == 0:
            # If sum is even, add 1 to the last term to make it odd
            next_term = sequence[-1] + 1
        
        sequence.append(next_term)
    
    return sequence