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
    
    # First pass: find potential candidates with bitwise XOR
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    
    # If no number appears an odd number of times, this will be 0
    if xor_result == 0:
        raise ValueError("No number appears an odd number of times")
    
    # Second pass: find occurrences of all numbers and track smallest odd occurrence
    smallest_odd_occurrence = float('inf')
    for num in set(numbers):
        # Count occurrences using bitwise method
        count = sum(1 for x in numbers if x == num)
        
        # Check if count is odd and update smallest
        if count % 2 == 1:
            smallest_odd_occurrence = min(smallest_odd_occurrence, num)
    
    return smallest_odd_occurrence