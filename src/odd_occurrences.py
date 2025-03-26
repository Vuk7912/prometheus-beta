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
    Space Complexity: O(n)
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use Counter to track occurrences more efficiently
    from collections import Counter
    
    # Count occurrences
    count = Counter(numbers)
    
    # Find all numbers with odd occurrences
    odd_nums = [num for num, freq in count.items() if freq % 2 == 1]
    
    if not odd_nums:
        raise ValueError("No number appears an odd number of times")
    
    # Explicitly sort to match expected order
    return min(odd_nums)