def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence of distinct integers in strictly increasing order.

    Args:
        arr (list): The input list of integers to validate.

    Returns:
        bool: True if the sequence is valid, False otherwise.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(arr) <= 1:
        return True
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Check for strict increasing order and distinct values
    for i in range(1, len(arr)):
        # Check if current element is strictly greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True