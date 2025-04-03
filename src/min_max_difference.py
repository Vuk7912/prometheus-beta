def find_min_max_difference(number_string):
    """
    Calculate the difference between the largest and smallest numbers in a comma-separated string of integers.

    Args:
        number_string (str): A string of comma-separated integers.

    Returns:
        int: The absolute difference between the largest and smallest numbers.

    Raises:
        ValueError: If the input string is empty or contains non-integer values.
    """
    # Check if the input string is empty
    if not number_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the string and convert to integers
    try:
        numbers = [int(num.strip()) for num in number_string.split(',') if num.strip()]
    except ValueError:
        raise ValueError("Input must be a comma-separated string of integers")
    
    # Check if the list is empty after parsing
    if not numbers:
        raise ValueError("No valid integers found in the input string")
    
    # Find and return the absolute difference between max and min
    return abs(max(numbers) - min(numbers))