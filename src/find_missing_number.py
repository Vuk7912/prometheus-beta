def find_missing_number(arr):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        arr (list): A list of integers containing numbers from 1 to n, 
                    with one number missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty list, not a list of integers, etc.).
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Validate that input contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Array must contain only integers")
    
    # Calculate the expected sum of numbers from 1 to n+1
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum