def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given individual stair heights.
    
    A climber can take 1 or 2 steps at a time, matching the individual stair heights.
    
    Args:
        stair_lengths (list): A list of integers representing individual stair heights.
    
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
    
    # The problem requires tracking ways to climb the SPECIFIC sequence of stairs
    # Use dynamic programming with ways counting
    n = len(stair_lengths)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to climb no stairs
    
    for i in range(1, n + 1):
        # Try 1-step climb for the current stair if possible
        if i >= 1 and sum(stair_lengths[:i]) <= sum(stair_lengths):
            dp[i] += dp[i-1]
        
        # Try 2-step climb for the current stair if possible
        if i >= 2 and sum(stair_lengths[:i]) <= sum(stair_lengths):
            dp[i] += dp[i-2]
    
    return dp[n]