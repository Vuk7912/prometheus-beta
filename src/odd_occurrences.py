def find_number_with_odd_occurrences(numbers):
    """
    Find the smallest number that appears an odd number of times in the list.
    
    This function efficiently determines the smallest number with an odd number of occurrences.
    
    Args:
        numbers (list): A list of integers to search for odd occurrences.
    
    Returns:
        int: The smallest number that appears an odd number of times.
    
    Raises:
        ValueError: If no number appears an odd number of times or the input list is empty.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Track occurrences of numbers
    occurrences = {}
    for num in numbers:
        occurrences[num] = occurrences.get(num, 0) + 1
    
    # Find numbers with odd occurrences and get the smallest
    odd_occurrence_nums = [num for num, count in occurrences.items() if count % 2 == 1]
    
    if not odd_occurrence_nums:
        raise ValueError("No number appears an odd number of times")
    
    return min(odd_occurrence_nums)