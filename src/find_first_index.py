def find_first_index(arr, target):
    """
    Find the index of the first occurrence of a target value in an array.

    Args:
        arr (list): The input array to search through
        target: The value to find in the array

    Returns:
        int: The index of the first occurrence of the target, 
             or -1 if the target is not found

    Examples:
        >>> find_first_index([1, 2, 3, 2, 1], 2)
        1
        >>> find_first_index([1, 2, 3], 4)
        -1
        >>> find_first_index([], 1)
        -1
    """
    # Handle empty array case
    if not arr:
        return -1
    
    # Iterate through the array
    for index, value in enumerate(arr):
        # Use strict equality for better type handling
        if value is target or (type(value) == type(target) and value == target):
            return index
    
    # Target not found
    return -1