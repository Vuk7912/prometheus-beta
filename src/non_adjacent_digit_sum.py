def max_non_adjacent_digit_sum(number):
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    A non-adjacent digit is a digit that does not come immediately after or before 
    another digit in the sum. The function considers all possible combinations 
    of non-adjacent digits to maximize the sum.
    
    Args:
        number (int): A positive integer to analyze.
    
    Returns:
        int: The maximum sum of non-adjacent digits.
    
    Raises:
        ValueError: If the input is not a positive integer.
    
    Examples:
        >>> max_non_adjacent_digit_sum(123)  # 1 + 3 = 4
        4
        >>> max_non_adjacent_digit_sum(1234)  # 1 + 3 = 4
        4
    """
    # Validate input
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easy digit manipulation
    digits = str(number)
    
    # Handle special cases for short numbers
    if len(digits) <= 1:
        return int(digits[0]) if digits else 0
    
    # Dynamic programming to find max non-adjacent sum
    # We'll use two variables to track max sums
    include = int(digits[0])  # Max sum including current digit
    exclude = 0  # Max sum excluding current digit
    
    for digit in digits[1:]:
        # Store previous maximum sums
        new_include = exclude + int(digit)
        new_exclude = max(include, exclude)
        
        # Update for next iteration
        include = new_include
        exclude = new_exclude
    
    # Return the maximum of the final two possibilities
    return max(include, exclude)