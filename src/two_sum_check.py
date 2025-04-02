def two_sum_check(nums, target):
    """
    Check if any two unique numbers in the array sum to the target.

    Args:
        nums (list): A list of unique integers to check.
        target (int): The target sum to find.

    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise.

    Raises:
        TypeError: If input is not a list or if nums contains non-integer elements.
        ValueError: If the input list is empty.
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Check that all elements are integers
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All elements must be integers")
    
    # Check if the list has unique elements
    if len(set(nums)) != len(nums):
        raise ValueError("Input list must contain unique integers")
    
    # Use a set for O(n) time complexity
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False