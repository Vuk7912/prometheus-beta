def bubble_sort(arr):
    """
    Perform bubble sort on the input list with an optimization to reduce unnecessary swaps.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    n = len(arr)
    if n <= 1:
        return arr
    
    # Perform bubble sort with swapped flag optimization
    for i in range(n):
        # Flag to track if any swaps were made in this pass
        swapped = False
        
        # Last i elements are already in place, so reduce the range
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set swapped flag to True
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr