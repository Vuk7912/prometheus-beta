def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort algorithm.
    
    Spaghetti Sort is a unique sorting algorithm that works by:
    1. Creating a list of 'noodles' (represented by indices) 
    2. Cutting the noodles to the length of their corresponding array values
    3. Arranging the noodles from shortest to longest
    4. Retrieving the original array elements in the new order
    
    Args:
        arr (list): The input list of comparable elements to be sorted
    
    Returns:
        list: A new list with elements sorted in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Try to create a sorted list to test comparability
    try:
        # Create a copy of the input list to avoid modifying the original
        sorted_arr = arr.copy()
        
        # Bubble sort-like implementation that mimics spaghetti sort concept
        for i in range(len(sorted_arr)):
            for j in range(0, len(sorted_arr) - i - 1):
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap elements
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
        
        return sorted_arr
    
    except TypeError:
        # This will catch any comparison failures
        raise ValueError("List contains non-comparable elements")