def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given lengths.
    
    A climber can take 1 or 2 steps at a time.
    
    Args:
        stair_lengths (list): A list of integers representing stair heights.
    
    Returns:
        int: The total number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If stair_lengths is None, empty, or contains non-positive values.
    """
    # Validate input 
    if stair_lengths is None or len(stair_lengths) == 0:
        raise ValueError("Stair lengths must be a non-empty list")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Total length of the staircase (sum of all stair heights)
    total_length = sum(stair_lengths)
    
    # Dynamic programming solution to count ways
    # Using 1 or 2 step sizes
    dp = [0] * (total_length + 1)
    dp[0] = 1  # Base case: 1 way to climb 0 height
    
    # Compute ways to climb different heights
    for length in range(1, total_length + 1):
        if length >= 1:
            dp[length] += dp[length - 1]
        if length >= 2:
            dp[length] += dp[length - 2]
    
    return dp[total_length]