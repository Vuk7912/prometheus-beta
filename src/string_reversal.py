def reverse_string_in_place(s: list) -> None:
    """
    Reverses a string in-place without creating a new string.
    
    This function modifies the input list of characters directly,
    achieving O(1) space complexity and O(n) time complexity.
    
    Args:
        s (list): A mutable list of characters to be reversed.
    
    Raises:
        TypeError: If input is not a list.
    
    Examples:
        >>> chars = list('hello')
        >>> reverse_string_in_place(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check for invalid input
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    
    # Handle empty or single-character lists
    if len(s) <= 1:
        return
    
    # Two-pointer technique to swap characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers towards center
        left += 1
        right -= 1