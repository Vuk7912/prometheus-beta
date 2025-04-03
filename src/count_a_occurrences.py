def count_a_occurrences(input_string: str) -> int:
    """
    Count the number of times the character 'a' appears in the given string, 
    ignoring case sensitivity.

    Args:
        input_string (str): The input string to search for 'a' occurrences.

    Returns:
        int: The number of 'a' characters in the string (case-insensitive).

    Examples:
        >>> count_a_occurrences("Apple")
        1
        >>> count_a_occurrences("banana")
        3
        >>> count_a_occurrences("JAVA")
        0
    """
    # Convert the string to lowercase and count 'a' occurrences
    return input_string.lower().count('a')