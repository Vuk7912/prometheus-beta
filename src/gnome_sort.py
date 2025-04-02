def gnome_sort(arr):
    """
    Implement the Gnome Sort (Stupid Sort) algorithm.
    
    Gnome Sort is a simple sorting algorithm that works similarly to how a gardener 
    sorts a line of flower pots. The gardener looks at each pot, and if it's out of order, 
    they swap it with the previous pot, then go back to check the previous pots.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains unsortable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Perform Gnome Sort
    index = 0
    while index < len(arr):
        # If at the start or current element is in the right place, move forward
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # Swap elements and move back to check previous elements
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    
    return arr