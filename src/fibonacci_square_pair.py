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
        # Ensure the last two numbers' sum is a perfect square
        while not is_perfect_square(sequence[-1] + sequence[-2]):
            # Generate next Fibonacci-like number
            next_num = sequence[-1] + sequence[-2]
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
    root = int(math.sqrt(num))
    return root * root == num