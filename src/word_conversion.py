def can_convert_by_deleting_one_char(word1: str, word2: str) -> bool:
    """
    Determine if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first word to check
        word2 (str): The target word
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting one character, False otherwise
    
    Examples:
        >>> can_convert_by_deleting_one_char('abc', 'ac')
        True
        >>> can_convert_by_deleting_one_char('abc', 'ab')
        True
        >>> can_convert_by_deleting_one_char('abc', 'abc')
        False
    """
    # Check for invalid inputs
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Inputs must be strings")
    
    # If the words are the same length, conversion is impossible
    if len(word1) == len(word2):
        return False
    
    # If the length difference is not exactly 1, conversion is impossible
    if abs(len(word1) - len(word2)) != 1:
        return False
    
    # If word1 is longer, we check if it can be converted to word2
    if len(word1) > len(word2):
        for i in range(len(word1)):
            # Try removing each character
            candidate = word1[:i] + word1[i+1:]
            if candidate == word2:
                return True
    
    # If word2 is longer, it's not possible with this function's logic
    return False