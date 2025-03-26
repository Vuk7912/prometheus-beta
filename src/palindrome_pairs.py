def find_palindrome_pairs(words):
    """
    Find indices of word pairs that form palindromes when concatenated.
    
    A palindrome pair is a pair of words (i, j) such that when concatenated 
    (words[i] + words[j] or words[j] + words[i]), the result is a palindrome.
    
    Args:
        words (List[str]): A list of words to check for palindrome pairs
    
    Returns:
        List[List[int]]: A list of index pairs that form palindrome pairs
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the length of the longest word
    Space Complexity: O(1) extra space (not counting the output list)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-string elements
    """
    # Input validation
    if not isinstance(words, list):
        raise TypeError("Input must be a list of words")
    
    if any(not isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    # Function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    
    # Find palindrome pairs
    palindrome_pairs = []
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip pairing a word with itself
            if i == j:
                continue
            
            # Check both concatenation orders
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            if is_palindrome(concat1):
                palindrome_pairs.append([i, j])
    
    return palindrome_pairs