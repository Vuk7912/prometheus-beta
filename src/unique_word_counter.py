import re
import unicodedata

def count_unique_words(text: str) -> int:
    """
    Count the number of unique words in a given text, ignoring case and punctuation.
    
    Args:
        text (str): The input text to analyze
    
    Returns:
        int: The number of unique words in the text
    
    Examples:
        >>> count_unique_words("Hello, hello! How are you?")
        4
        >>> count_unique_words("")
        0
        >>> count_unique_words("  ")
        0
    """
    # Handle None or empty input
    if not text:
        return 0
    
    # Normalize Unicode characters and convert to lowercase
    normalized_text = unicodedata.normalize('NFKD', text.lower())
    
    # Remove accents
    text_without_accents = ''.join(c for c in normalized_text if not unicodedata.combining(c))
    
    # Remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text_without_accents)
    
    # Split into words and remove extra whitespace
    words = cleaned_text.split()
    
    # Return the number of unique words
    return len(set(words))