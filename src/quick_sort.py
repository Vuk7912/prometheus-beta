def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element
    from the array and partitioning the other elements into two sub-arrays according to 
    whether they are less than or greater than the pivot.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list or contains incomparable elements
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element list is already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        """
        Recursive helper function to perform in-place quick sort
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        """
        if low < high:
            # Partition the array
            partition_index = _partition(low, high)
            
            # Recursively sort the left and right subarrays
            _quick_sort(low, partition_index - 1)
            _quick_sort(partition_index + 1, high)
    
    def _partition(low, high):
        """
        Choose the rightmost element as pivot and partition the array
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        
        Returns:
            int: The partition index
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the quick sort process
    _quick_sort(0, len(arr) - 1)
    
    return arr