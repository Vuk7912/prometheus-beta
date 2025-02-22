def replace_vowels(input_string):
    """
    Replace each vowel with the next vowel in the alphabet, preserving case.
    
    Args:
        input_string (str): The input string to modify
    
    Returns:
        str: A new string with vowels replaced
    """
    # Define vowel sequences (both lowercase and uppercase)
    vowel_map = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    # Replace each character if it's a vowel
    return ''.join(vowel_map.get(char, char) for char in input_string)