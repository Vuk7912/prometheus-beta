def sum_pairs_with_diff_nine(file_path):
    """
    Read numbers from a text file and return the sum of all pairs 
    of numbers that have a difference of exactly 9.
    
    Args:
        file_path (str): Path to the text file containing numbers
    
    Returns:
        int: Sum of all pairs of numbers with a difference of 9
    
    Raises:
        FileNotFoundError: If the specified file cannot be found
        ValueError: If the file contains non-numeric content
    """
    # Read numbers from the file
    try:
        with open(file_path, 'r') as file:
            # Convert file contents to a list of integers
            numbers = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError:
        raise ValueError("File contains non-numeric content")
    
    # Find pairs with difference of 9 and sum them
    pair_sum = 0
    
    # Use a set for O(n) lookup time
    number_set = set(numbers)
    
    for num in numbers:
        # Check if num+9 or num-9 exists in the set
        # Use both to avoid double-counting pairs
        if num + 9 in number_set:
            pair_sum += num + (num + 9)
        elif num - 9 in number_set:
            pair_sum += num + (num - 9)
    
    # Divide by 2 to avoid double-counting pairs
    return pair_sum // 2