def filter_even_numbers(sorted_nums):
    """
    Filter even numbers from a sorted list of unique integers while maintaining their original order.
    
    Args:
        sorted_nums (list): A sorted list of unique integers.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the input list is not sorted or contains duplicates.
    """
    # Type checking
    if not isinstance(sorted_nums, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted and has unique elements
    if len(sorted_nums) > 1:
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] <= sorted_nums[i-1]:
                raise ValueError("Input list must be sorted with unique elements")
    
    # Filter even numbers with O(n) time complexity
    return [num for num in sorted_nums if num % 2 == 0]