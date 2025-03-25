def get_unique_sorted_integers(input_list):
    """
    Return a unique and sorted list of integers from the input list.

    Args:
        input_list (list): A list of integers to process.

    Returns:
        list: A new list containing unique integers, sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in input_list):
        raise TypeError("All elements must be integers")
    
    # Remove duplicates and sort
    return sorted(set(input_list))