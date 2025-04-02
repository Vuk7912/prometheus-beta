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
    
    # Create 'noodles' - pairs of (value, original_index)
    try:
        noodles = [(val, idx) for idx, val in enumerate(arr)]
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Sort the noodles based on their length (value)
    sorted_noodles = sorted(noodles, key=lambda x: x[0])
    
    # Return the sorted elements preserving original values
    return [noodle[0] for noodle in sorted_noodles]