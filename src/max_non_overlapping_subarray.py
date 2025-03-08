def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray.
    
    A non-overlapping subarray is a contiguous subarray where no two elements 
    are from adjacent indices.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of a non-overlapping subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5])
        9
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element list
    if len(arr) == 1:
        return arr[0]
    
    # Handle two element list
    if len(arr) == 2:
        return max(arr[0], arr[1])
    
    # Dynamic programming solution
    # dp[i] represents the max sum of non-overlapping subarray up to index i
    dp = [0] * len(arr)
    
    # Base cases
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    # Fill dp table
    for i in range(2, len(arr)):
        # Two choices at each step:
        # 1. Include current element and the max sum two steps back
        # 2. Skip current element and take previous max sum
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])
    
    return dp[-1]