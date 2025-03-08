def get_unique_pairs(input_list):
    """
    Returns all unique pairs of elements from the given list of integers.
    
    A unique pair means each pair is only listed once, regardless of order.
    
    Args:
        input_list (list): A list of integers
    
    Returns:
        list: A list of tuples representing unique pairs of elements
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    
    Examples:
        >>> get_unique_pairs([1, 2, 3])
        [(1, 2), (1, 3), (2, 3)]
        >>> get_unique_pairs([])
        []
    """
    # Validate input
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if input_list and not all(isinstance(x, int) for x in input_list):
        raise ValueError("All list elements must be integers")
    
    # If list is too short to form pairs, return empty list
    if len(input_list) < 2:
        return []
    
    # Generate unique pairs
    unique_pairs = []
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            unique_pairs.append((input_list[i], input_list[j]))
    
    return unique_pairs