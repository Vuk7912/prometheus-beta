def calculate_extremes_average(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in an array.
    
    Args:
        numbers (list): A list of six real numbers.
    
    Returns:
        float: The average of the three smallest and three largest numbers.
    
    Raises:
        ValueError: If the input list does not contain exactly 6 numbers.
    """
    # Validate input
    if len(numbers) != 6:
        raise ValueError("Input must be a list of exactly 6 numbers")
    
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Take the first 3 (smallest) and last 3 (largest) numbers
    smallest_three = sorted_numbers[:3]
    largest_three = sorted_numbers[3:]
    
    # Calculate and return the average with precision
    return round((sum(smallest_three) + sum(largest_three)) / 6, 2)