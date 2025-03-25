import math

def generate_fibonacci_square_pair_sequence(n):
    """
    Generate a Fibonacci-like sequence with favorable consecutive pair sum properties.
    
    Args:
        n (int): The number of elements to generate in the sequence.
    
    Returns:
        list: A list of n numbers with some consecutive pair sums being perfect squares.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Sequence length must be at least 1")
    
    # Initialize the sequence
    sequence = [1]
    
    # Generate the sequence
    while len(sequence) < n:
        # Start next number from 1 or last number + 1
        next_num = 1 if len(sequence) == 1 else sequence[-1] + 1
        
        sequence.append(next_num)
    
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