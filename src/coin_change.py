def min_coins(coins, amount):
    """
    Compute the minimum number of coins needed to make up a given amount.
    
    Args:
        coins (list): List of available coin denominations
        amount (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed to make up the amount
             Returns -1 if the amount cannot be made up exactly
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values
    """
    # Validate input
    if not coins:
        raise ValueError("Coin denominations list cannot be empty")
    
    if any(coin <= 0 for coin in coins):
        raise ValueError("All coin denominations must be positive")
    
    # Special case: amount is 0
    if amount == 0:
        return 0
    
    # If amount is negative, it's impossible
    if amount < 0:
        return -1
    
    # Initialize dynamic programming array
    # dp[i] will store the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make 0 amount
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # Update minimum coins if using this coin leads to fewer total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result, or -1 if amount cannot be made exactly
    return dp[amount] if dp[amount] != float('inf') else -1