def climb_stairs(n: int) -> int:
    """
    Calculate the number of ways to climb a staircase using 1 or 2 steps.
    
    Args:
        n (int): Total number of steps in the staircase.
    
    Returns:
        int: Number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If n is negative.
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Number of steps cannot be negative")
    
    # Base cases
    if n <= 1:
        return 1
    
    # Recursive solution
    return climb_stairs(n - 1) + climb_stairs(n - 2)