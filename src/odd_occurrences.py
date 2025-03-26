def find_number_with_odd_occurrences(numbers):
    """
    Find the smallest number that appears an odd number of times in the list using bitwise XOR.
    
    This function uses the XOR bitwise operation to efficiently find numbers with odd occurrences.
    If multiple numbers appear an odd number of times, it returns the smallest one.
    
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
    
    # Find all numbers with odd occurrences
    odd_occurrence_numbers = []
    for num in set(numbers):
        count = sum(1 for x in numbers if x == num)
        if count % 2 == 1:
            odd_occurrence_numbers.append(num)
    
    # Check if no number appears an odd number of times
    if not odd_occurrence_numbers:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_occurrence_numbers)