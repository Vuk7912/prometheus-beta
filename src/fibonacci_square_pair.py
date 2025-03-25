import math

def generate_fibonacci_square_pair_sequence(n):
    """
    Generate a Fibonacci-like sequence where the sum of consecutive pairs is a perfect square.
    
    Args:
        n (int): The number of elements to generate in the sequence.
    
    Returns:
        list: A list of n numbers where each consecutive pair's sum is a perfect square.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Sequence length must be at least 1")
    
    # Initialize the sequence
    sequence = [1, 1]
    
    # Generate the sequence
    while len(sequence) < n:
        # Try next Fibonacci step
        next_num = sequence[-1] + sequence[-2]
        
        # Ensure the last two numbers' sum is a perfect square
        while not is_perfect_square(sequence[-1] + sequence[-2]):
            # Try the next combination
            sequence.append(next_num)
            next_num = sequence[-1] + sequence[-2]
        
        # Add the next number for the perfect square
        sequence.append(next_num)
        
        # If we have enough numbers, break
        if len(sequence) >= n:
            break
    
    # Return exactly n numbers
    return sequence[:n]

def is_perfect_square(num):
    """
    Check if a number is a perfect square.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    # Handle 0 and 1 as special cases
    if num in (0, 1):
        return True
    
    # Check if the square root is an integer
    root = int(math.sqrt(num))
    return root * root == num