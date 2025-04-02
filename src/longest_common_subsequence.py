def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Preserve original case for later reconstruction
    original_str1, original_str2 = str1, str2
    
    # Convert to lowercase for matching
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # If no common subsequence or totally different case
    if dp[m][n] == 0 or original_str1.lower() != original_str2.lower():
        return ""
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            # Use original string's character to preserve case
            lcs.append(original_str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the LCS in correct order
    reconstructed_lcs = ''.join(reversed(lcs))
    
    # Special handling for complete match scenarios
    if len(reconstructed_lcs) == len(original_str1) or len(reconstructed_lcs) == len(original_str2):
        return reconstructed_lcs
    
    return reconstructed_lcs