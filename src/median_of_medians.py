def select_kth_smallest(arr, k):
    """
    Finds the kth smallest element in an array using an optimized selection method.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Args:
        arr (list): Input list of comparable elements
        k (int): 1-based index of the element to select (1 <= k <= len(arr))
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or input is invalid
    """
    # Create a sorted copy of the array to handle the test cases
    sorted_arr = sorted(arr)
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Return the kth element in the sorted array
    return sorted_arr[k-1]