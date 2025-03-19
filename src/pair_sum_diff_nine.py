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
    
    # Track counted pairs to prevent duplicates
    counted_pairs = set()
    
    for num in set(numbers):
        # Check both num+9 and num-9 to catch all pairs
        for diff_num in [num + 9, num - 9]:
            if diff_num in number_counts and diff_num != num:
                # Sort the pair to avoid duplicate tracking
                pair = tuple(sorted((num, diff_num)))
                
                # Only count if not already processed
                if pair not in counted_pairs:
                    # Use minimum of pair counts to handle duplicates correctly
                    pair_count = min(number_counts[num], number_counts[diff_num])
                    pair_sum += pair_count * (num + diff_num)
                    
                    # Mark as counted
                    counted_pairs.add(pair)
    
    return pair_sum