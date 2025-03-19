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
    
    # Use a dictionary to count occurrences
    from collections import Counter
    number_counts = Counter(numbers)
    
    # Find pairs with difference of 9 and sum them
    pair_sum = 0
    
    # Keep track of pairs we've already counted
    counted_pairs = set()
    
    for num in set(numbers):
        # Pairs in both a+9=b and b+9=a order
        if num + 9 in number_counts:
            # Avoid double-counting pairs
            pair = tuple(sorted((num, num + 9)))
            if pair not in counted_pairs:
                # Count pairs, carefully handling duplicate numbers
                count = min(number_counts[num], number_counts[num + 9])
                pair_sum += count * (pair[0] + pair[1])
                counted_pairs.add(pair)
    
    return pair_sum