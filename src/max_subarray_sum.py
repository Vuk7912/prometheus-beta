def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with a given length k in an array of integers.

    Args:
        arr (list): Input array of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a subarray of length k

    Raises:
        ValueError: If k is invalid (non-positive or larger than array length)
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than array length")
    
    # If array is empty or k is 0, return 0
    if not arr or k == 0:
        return 0
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add next element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum