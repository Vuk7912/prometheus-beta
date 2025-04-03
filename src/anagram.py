def isAnagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The comparison is case-insensitive and 
    ignores whitespace and punctuation.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> isAnagram("listen", "silent")
        True
        >>> isAnagram("hello", "world")
        False
        >>> isAnagram("Astronomer", "Moon starer")
        True
    """
    # Normalize strings by converting to lowercase and removing non-alphanumeric characters
    def normalize(s: str) -> str:
        return ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized strings have the same sorted characters
    return sorted(normalize(str1)) == sorted(normalize(str2))