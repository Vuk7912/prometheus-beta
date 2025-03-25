def sort_comma_separated_integers(input_string: str) -> list[int]:
    """
    Sorts a string of comma-separated integers.

    Args:
        input_string (str): A string containing integers separated by commas.
    
    Returns:
        list[int]: A sorted list of unique integers extracted from the input string.
    
    Notes:
        - Discards any non-integer characters
        - Handles strings with varying numbers of integers
        - Returns an empty list if no valid integers are found
    
    Examples:
        >>> sort_comma_separated_integers("3,1,4,1,5,9")
        [1, 1, 3, 4, 5, 9]
        >>> sort_comma_separated_integers("10,abc,20,def,30")
        [10, 20, 30]
        >>> sort_comma_separated_integers("hello")
        []
    """
    # Extract only integer characters 
    try:
        # Split by comma, strip whitespace, filter out non-integers, convert to integers
        integers = [
            int(item.strip()) 
            for item in input_string.split(',') 
            if item.strip().lstrip('-').isdigit()
        ]
        
        # Return sorted list
        return sorted(integers)
    
    except (ValueError, TypeError):
        # Return empty list if any conversion fails
        return []