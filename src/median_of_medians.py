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
    
    def select(low, high):
        """Recursive selection using Median of Medians approach."""
        # If the subarray has 5 or fewer elements, use simple sorting
        if high - low + 1 <= 5:
            sorted_subarray = sorted(arr[low:high+1])
            return sorted_subarray[k - low]
        
        # Divide the array into groups of 5
        for i in range(low, high + 1, 5):
            subgroup_end = min(i + 4, high)
            
            # Sort each group of 5
            median_group = sorted(arr[i:subgroup_end+1])
            
            # Place the median of each group in the front of the array
            median_index = (i + subgroup_end) // 2
            arr[median_index], arr[low + (i - low) // 5] = arr[low + (i - low) // 5], median_index
        
        # Recursively find the median of medians
        median_of_medians_index = (low + (high - low) // 10)
        pivot_index = partition(low, median_of_medians_index)
        
        # Adjust the search based on the pivot location
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(low, pivot_index - 1)
        else:
            return select(pivot_index + 1, high)
    
    return select(0, len(arr) - 1)