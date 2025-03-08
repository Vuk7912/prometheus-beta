def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given individual stair heights.
    
    A climber can take 1 or 2 steps exactly matching the given stair lengths.
    Climbing must exactly match the total staircase sequence.
    
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
    
    n = len(stair_lengths)
    
    # Dynamic programming tracking valid climbing ways
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to climb zero stairs
    
    for i in range(1, n + 1):
        # 1-step climb
        if i >= 1:
            dp[i] += dp[i-1]
        
        # 2-step climb if allowed
        if i >= 2:
            dp[i] += dp[i-2]
    
    return dp[n]