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
            if diff_num in number_counts:
                # Sort the pair to avoid duplicate tracking
                pair = tuple(sorted((num, diff_num)))
                
                # Skip if already processed or same number
                if pair not in counted_pairs and pair[0] != pair[1]:
                    # Use minimum of pair counts to handle duplicates correctly
                    pair_count = min(number_counts[pair[0]], number_counts[pair[1]])
                    pair_sum += pair_count * (pair[0] + pair[1])
                    
                    # Mark as counted
                    counted_pairs.add(pair)
                
                # Special handling for same number pairs (must occur at least twice)
                if pair[0] == pair[1] and number_counts[pair[0]] >= 2:
                    # Number of full pairs is integer division of count by 2
                    same_pair_count = number_counts[pair[0]] // 2
                    pair_sum += same_pair_count * 2 * pair[0]
    
    return pair_sum