def find_second_largest(arr):
    """
    Find the second largest number in an array.

    Args:
        arr (list): A list of numbers to search through.

    Returns:
        int or None: The second largest number in the array, 
                     or None if the array has fewer than 2 unique numbers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) < 2:
        return None
    
    # Check all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Remove duplicates and sort in descending order
    unique_nums = sorted(set(arr), reverse=True)
    
    # Return second largest if exists
    return unique_nums[1] if len(unique_nums) > 1 else None