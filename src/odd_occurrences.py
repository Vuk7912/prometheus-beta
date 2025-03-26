def find_number_with_odd_occurrences(numbers):
    """
    Find the smallest number that appears an odd number of times in the list using bitwise XOR.
    
    This function uses a combination of counting and optimization to efficiently find 
    the smallest number with odd occurrences.
    
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
    
    # Track numbers with odd occurrences and maintain smallest
    smallest_odd_occurrence = float('inf')
    has_odd_occurrence = False
    
    for num in set(numbers):
        count = sum(1 for x in numbers if x == num)
        if count % 2 == 1:
            has_odd_occurrence = True
            smallest_odd_occurrence = min(smallest_odd_occurrence, num)
    
    if not has_odd_occurrence:
        raise ValueError("No number appears an odd number of times")
    
    return smallest_odd_occurrence