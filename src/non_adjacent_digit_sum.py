def max_non_adjacent_digit_sum(number):
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    A non-adjacent digit is a digit that does not come immediately after or before 
    another digit in the sum. The function considers all possible combinations 
    of non-adjacent digits to maximize the sum.
    
    Args:
        number (int): A positive integer to analyze.
    
    Returns:
        int: The maximum sum of non-adjacent digits.
    
    Raises:
        ValueError: If the input is not a positive integer.
    
    Examples:
        >>> max_non_adjacent_digit_sum(123)  # 1 + 3 = 4
        4
        >>> max_non_adjacent_digit_sum(1234)  # 1 + 3 = 4
        4
    """
    # Validate input
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easy digit manipulation
    digits = str(number)
    
    # Handle special cases for short numbers
    if len(digits) <= 1:
        return int(digits[0]) if digits else 0
    
    # Initialize DP array
    n = len(digits)
    dp = [0] * n
    
    # First digit case
    dp[0] = int(digits[0])
    
    # Second digit case
    dp[1] = max(int(digits[0]), int(digits[1]))
    
    # Dynamic programming to find max non-adjacent sum
    for i in range(2, n):
        # Max of either:
        # 1. Current digit + max sum up to two positions before
        # 2. Max sum from previous position
        dp[i] = max(int(digits[i]) + dp[i-2], dp[i-1])
    
    # Return the final max sum
    return dp[-1]