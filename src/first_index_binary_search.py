def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a target number in a sorted array using binary search.
    
    Args:
        arr (list): A sorted list of positive integers 
        target (int): The number to search for
    
    Returns:
        int: Index of the first occurrence of the target, or -1 if not found
    
    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If arr contains non-positive integers
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    if any(not isinstance(x, int) or x <= 0 for x in arr):
        raise ValueError("Array must contain only positive integers")
    
    # Empty array case
    if not arr:
        return -1
    
    # Binary search to find first occurrence
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Found a match, but continue searching left for first occurrence
            if mid == 0 or arr[mid-1] < target:
                return mid
            right = mid - 1
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
    
    return -1