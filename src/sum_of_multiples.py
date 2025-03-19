def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of all multiples of 2 and 3 within the given inclusive range.

    Args:
        min (int): The lower bound of the range (inclusive)
        max (int): The upper bound of the range (inclusive)

    Returns:
        int: The sum of all numbers within the range that are multiples of 2 or 3

    Raises:
        ValueError: If min is greater than max
    """
    # Validate input
    if min > max:
        raise ValueError("Minimum value must be less than or equal to maximum value")

    # Ensure we only count numbers exactly divisible by 2 or 3
    start = max(1, min)  # Start from 1 or the min value, whichever is larger
    multiples_sum = sum(
        num for num in range(start, max + 1) 
        if num % 2 == 0 or num % 3 == 0
    )

    return multiples_sum