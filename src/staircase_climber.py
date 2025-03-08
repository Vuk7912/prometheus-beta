def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given individual stair heights.
    
    A climber can take 1 or 2 steps at a time, matching the individual stair heights.
    Climbing must exactly match the total staircase length.
    
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
    
    # Total height is the cumulative sum of stair lengths
    total_height = sum(stair_lengths)
    
    # Dynamic programming to track valid climbing ways
    dp = [0] * (total_height + 1)
    dp[0] = 1  # Base case: 1 way to climb zero height
    
    # Compute possible ways to climb
    for height in range(1, total_height + 1):
        # Check 1-step climb if possible
        if height >= 1:
            dp[height] += dp[height - 1]
        
        # Check 2-step climb if possible
        if height >= 2:
            dp[height] += dp[height - 2]
    
    return dp[total_height]