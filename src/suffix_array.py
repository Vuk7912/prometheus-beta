def create_suffix_array(text):
    """
    Create a suffix array for efficient string matching.
    
    A suffix array is a sorted array of all suffixes of a given string.
    This implementation helps in efficient string matching and searching.
    
    Args:
        text (str): The input string to create a suffix array for.
    
    Returns:
        list: A sorted list of suffix indices.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Time Complexity: O(n log n), where n is the length of the string
    Space Complexity: O(n)
    
    Example:
        >>> create_suffix_array("banana")
        [5, 3, 1, 0, 4, 2]
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Create a list of tuples: (suffix, original index)
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort suffixes lexicographically
    sorted_suffixes = sorted(suffixes)
    
    # Extract and return only the indices
    return [index for _, index in sorted_suffixes]


def search_in_suffix_array(text, pattern, suffix_array=None):
    """
    Search for a pattern within a text using the suffix array.
    
    Args:
        text (str): The full text to search in.
        pattern (str): The pattern to search for.
        suffix_array (list, optional): Precomputed suffix array. If None, 
                                       it will be created.
    
    Returns:
        list: Indices where the pattern starts in the text.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If text or pattern is empty.
    
    Time Complexity: O(m log n), where m is pattern length, n is text length
    
    Example:
        >>> search_in_suffix_array("banana", "ana")
        [1, 3]
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Create suffix array if not provided
    if suffix_array is None:
        suffix_array = create_suffix_array(text)
    
    # Binary search to find pattern occurrences
    results = []
    left, right = 0, len(suffix_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        suffix = text[suffix_array[mid]:]
        
        if suffix.startswith(pattern):
            # Find all matching indices
            start = mid
            while start >= 0 and text[suffix_array[start]:].startswith(pattern):
                start -= 1
            
            end = mid
            while end < len(suffix_array) and text[suffix_array[end]:].startswith(pattern):
                end += 1
            
            results = [suffix_array[i] for i in range(start + 1, end)]
            break
        
        elif pattern < suffix:
            right = mid - 1
        else:
            left = mid + 1
    
    return sorted(results)