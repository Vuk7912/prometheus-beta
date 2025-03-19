def find_common(list1, list2):
    """
    Find common elements between two input lists.

    Args:
        list1 (list): First input list
        list2 (list): Second input list

    Returns:
        list: A list of elements common to both input lists, without duplicates

    Raises:
        TypeError: If either input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")
    
    # Use set intersection to find common elements and convert back to list
    return list(set(list1) & set(list2))