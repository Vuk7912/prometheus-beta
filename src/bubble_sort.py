def bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    The optimization includes:
    1. Early stopping when no swaps occur in a pass
    2. Reducing the number of comparisons in subsequent passes
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Create a copy to avoid modifying the original list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the input list
    sorted_arr = arr.copy()
    
    # Track the last unsorted element
    last_unsorted = len(sorted_arr)
    
    while last_unsorted > 1:
        # Flag to optimize - if no swaps occur, list is already sorted
        swapped = False
        
        # Reduce number of comparisons in each pass
        for i in range(1, last_unsorted):
            # Compare adjacent elements
            if sorted_arr[i-1] > sorted_arr[i]:
                # Swap elements
                sorted_arr[i-1], sorted_arr[i] = sorted_arr[i], sorted_arr[i-1]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
        
        # Reduce the range of comparisons
        last_unsorted -= 1
    
    return sorted_arr