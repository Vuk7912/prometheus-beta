def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray within the given array of integers.
    
    This function uses Kadane's algorithm to find the maximum subarray sum,
    which works efficiently for arrays containing both positive and negative numbers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Check for invalid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_ending_here = max_so_far = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Kadane's algorithm: either start a new subarray or extend existing one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far