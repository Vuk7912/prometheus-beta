def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of unique even numbers in the input array.
    
    Args:
        numbers (list): An array of integers to process.
    
    Returns:
        int: Sum of even numbers that appear only once in the array.
        Returns 0 if no unique even numbers exist or all even numbers are repeated.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate list contents
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Count occurrences of each unique even number
    even_num_set = {}
    for num in numbers:
        if num % 2 == 0:
            even_num_set[num] = even_num_set.get(num, 0) + 1
    
    # Sum only the unique even numbers 
    unique_even_numbers = [num for num, count in even_num_set.items() if count == 1]
    
    return sum(unique_even_numbers)