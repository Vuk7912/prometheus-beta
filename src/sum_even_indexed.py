def sum_even_indexed_elements(numbers):
    """
    Calculate the sum of elements at even indices in a given list of integers.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: Sum of elements at even indices (0, 2, 4, ...).
             Returns 0 if the list is empty.

    Examples:
        >>> sum_even_indexed_elements([1, 2, 3, 4, 5])
        9  # 1 + 3 + 5
        >>> sum_even_indexed_elements([-1, 10, -2, 20, -3])
        -6  # -1 + -2 + -3
        >>> sum_even_indexed_elements([])
        0
    """
    # Handle empty list case
    if not numbers:
        return 0
    
    # Sum elements at even indices (0, 2, 4, ...)
    return sum(numbers[::2])