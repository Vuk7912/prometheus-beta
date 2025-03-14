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
        # Calculate next term with special rule to ensure odd sum
        next_term = sequence[-1] + sequence[-2]
        
        # Adjust the next term to make the sum of last two terms odd
        if (sequence[-1] + sequence[-2]) % 2 == 0:
            next_term += 1
        
        sequence.append(next_term)
    
    return sequence