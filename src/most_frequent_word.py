def most_frequent_word(text: str) -> str:
    """
    Find the most frequently occurring word in a given text.

    Args:
        text (str): A string of lowercase words separated by spaces.
              Contains only lowercase letters.

    Returns:
        str: The most frequently occurring word in the text.
             If multiple words have the same highest frequency,
             returns any one of them.

    Raises:
        ValueError: If the input text is empty or contains invalid characters.
    """
    # Validate input
    if not text:
        raise ValueError("Input text cannot be empty")
    
    # Check for invalid characters (only lowercase letters and spaces allowed)
    if not all(char.isalpha() or char.isspace() for char in text):
        raise ValueError("Input text must contain only lowercase letters and spaces")
    
    # Split the text into words
    words = text.split()
    
    # If no words, raise an error
    if not words:
        raise ValueError("No words found in the input text")
    
    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the most frequent word
    return max(word_counts, key=word_counts.get)