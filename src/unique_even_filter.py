def filter_unique_even_numbers(numbers):
    """
    Filter a list of integers to return only unique even numbers 
    while preserving their original order of appearance.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing unique even numbers in their original order.

    Examples:
        >>> filter_unique_even_numbers([1, 2, 3, 4, 2, 5, 6, 4, 7, 8])
        [2, 4, 6, 8]
        >>> filter_unique_even_numbers([1, 3, 5, 7])
        []
        >>> filter_unique_even_numbers([])
        []
    """
    # Use a set to track seen even numbers to maintain uniqueness
    seen_evens = set()
    # Use a list to preserve original order
    unique_even_result = []

    for num in numbers:
        # Check if the number is even and not seen before
        if num % 2 == 0 and num not in seen_evens:
            unique_even_result.append(num)
            seen_evens.add(num)

    return unique_even_result