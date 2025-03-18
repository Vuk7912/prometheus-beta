def longest_increasing_subsequence_length(arr):
    """
    Calculate the length of the longest continuous increasing subsequence in an array.
    
    A continuous increasing subsequence is a sequence of consecutive elements 
    where each element is strictly greater than the previous one.
    
    Args:
        arr (list): A list of integers to analyze.
    
    Returns:
        int: Length of the longest continuous increasing subsequence.
        Returns 0 for empty input, 1 for single-element input.
    
    Examples:
        >>> longest_increasing_subsequence_length([1,3,5,4,7])
        3
        >>> longest_increasing_subsequence_length([2,2,2,2])
        1
        >>> longest_increasing_subsequence_length([])
        0
    """
    # Handle edge cases
    if not arr:
        return 0
    if len(arr) == 1:
        return 1
    
    # Initialize variables
    max_length = 1
    current_length = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If current element is greater than previous, extend the subsequence
        if arr[i] > arr[i-1]:
            current_length += 1
            # Update max_length if current subsequence is longer
            max_length = max(max_length, current_length)
        else:
            # Reset current subsequence length
            current_length = 1
    
    return max_length