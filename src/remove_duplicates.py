def remove_duplicates(arr):
    """
    Remove duplicates from an array of integers while preserving the original order.

    Args:
        arr (list): A list of integers that may contain duplicates.

    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Use a set to track seen values while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result