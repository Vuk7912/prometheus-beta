def find_longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): The input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
        
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> find_longest_palindromic_substring("babad")
        'bab'
        >>> find_longest_palindromic_substring("cbbd")
        'bb'
        >>> find_longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s:
        return ""
    
    if len(s) == 1:
        return s
    
    start, max_length = 0, 1
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    # Check all possible centers
    for i in range(len(s)):
        # Odd length palindromes
        left1, len1 = expand_around_center(i, i)
        if len1 > max_length:
            start = left1
            max_length = len1
        
        # Even length palindromes
        left2, len2 = expand_around_center(i, i + 1)
        if len2 > max_length:
            start = left2
            max_length = len2
    
    return s[start:start + max_length]