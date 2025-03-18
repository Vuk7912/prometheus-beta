def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty")
    
    # Convert to list for easier manipulation
    chars = list(input_string)
    
    # Use set to store unique permutations
    unique_permutations = set()
    
    def backtrack(start):
        """
        Recursive backtracking to generate permutations.
        
        Args:
            start (int): Starting index for permutation generation.
        """
        # Base case: if we've reached the end of the string
        if start == len(chars):
            # Convert current permutation to string and add to set
            unique_permutations.add(''.join(chars))
            return
        
        # Try swapping current char with each subsequent char
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))