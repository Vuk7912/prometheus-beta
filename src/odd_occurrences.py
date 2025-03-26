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
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Iterate through unique numbers in order
    for num in sorted(set(numbers)):
        # Count occurrences of this number
        count = sum(1 for x in numbers if x == num)
        
        # If count is odd, return this number
        if count % 2 == 1:
            return num
    
    # If no number appears odd times
    raise ValueError("No number appears an odd number of times")