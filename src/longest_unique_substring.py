def longest_unique_substring_length(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with unique characters
    
    Examples:
        >>> longest_unique_substring_length("abcabcbb")
        3
        >>> longest_unique_substring_length("bbbbb")
        1
        >>> longest_unique_substring_length("")
        0
    """
    # Handle empty string edge case
    if not s:
        return 0
    
    # Use sliding window technique
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If current character is already in the set, 
        # remove characters from the left until unique again
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to the set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length