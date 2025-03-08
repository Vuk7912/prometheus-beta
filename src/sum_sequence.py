def sum_to_n(n: int) -> int:
    """
    Calculate the sum of all integers from 1 to n using a constant time formula.

    Args:
        n (int): A positive integer representing the upper bound of the sequence.

    Returns:
        int: The sum of all integers from 1 to n.

    Raises:
        ValueError: If n is negative.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    return (n * (n + 1)) // 2