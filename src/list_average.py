def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The arithmetic mean of the input list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate and return the average
    return sum(numbers) / len(numbers)