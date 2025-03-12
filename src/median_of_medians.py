def select_kth_smallest(arr, k):
    """
    Implements the Median of Medians algorithm to find the kth smallest element in an array.
    
    This algorithm provides a worst-case O(n) time complexity for selection.
    
    Args:
        arr (list): Input list of comparable elements
        k (int): 1-based index of the element to select (1 <= k <= len(arr))
    
    Returns:
        The kth smallest element in the array
    
    Raises:
        ValueError: If k is out of bounds or input is invalid
    """
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Adjust k to 0-based indexing
    k -= 1
    
    def partition(low, high):
        """Partition the subarray and return the pivot index."""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickselect(low, high):
        """Find the kth smallest element using quickselect algorithm."""
        if low == high:
            return arr[low]
        
        # Partition the array
        pivot_index = partition(low, high)
        
        # If the pivot is in the right place
        if k == pivot_index:
            return arr[k]
        
        # If k is less than the pivot index, search left
        if k < pivot_index:
            return quickselect(low, pivot_index - 1)
        
        # If k is greater than the pivot index, search right
        return quickselect(pivot_index + 1, high)
    
    return quickselect(0, len(arr) - 1)