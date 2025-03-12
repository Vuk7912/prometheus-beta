def select_kth_smallest(arr, k):
    """
    Finds the kth smallest element in an array using an iterative approach.
    
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
    # Create a copy of the array to avoid modifying the original
    arr = arr.copy()
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    # Adjust k to 0-based indexing
    k -= 1
    
    def partition(arr, low, high):
        """Partition the subarray and return the pivot index."""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_select(arr, k):
        """Iterative Quick Select algorithm."""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            # For very small arrays, use sorting
            if right - left <= 10:
                sorted_subarray = sorted(arr[left:right+1])
                return sorted_subarray[k - left]
            
            # Choose the last element as pivot
            pivot_index = partition(arr, left, right)
            
            # If pivot is in the right place
            if k == pivot_index:
                return arr[k]
            
            # If k is less than pivot index, search left
            if k < pivot_index:
                right = pivot_index - 1
            # If k is greater than pivot index, search right
            else:
                left = pivot_index + 1
        
        # Fallback to sorted method
        return sorted(arr)[k]
    
    return quick_select(arr, k)