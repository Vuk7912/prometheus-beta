def sum_unique_elements(numbers):
    """
    Calculate the sum of unique elements in the given list of integers.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Sum of unique elements in the input list
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If the list contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    unique_sum = 0
    
    # Iterate through the list once to find unique elements and sum them
    for num in numbers:
        # If the number is not in the set, it's unique
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
        # If the number is already in the set, it's a duplicate, so we skip it
        else:
            continue
    
    return unique_sum