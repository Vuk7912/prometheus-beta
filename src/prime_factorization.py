def prime_factorization(n):
    """
    Perform prime factorization on a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        tuple: A sorted tuple of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return (1,)
    
    # Prime factorization algorithm
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    # If n is a prime larger than the square root
    if n > 1:
        factors.append(n)
    
    return tuple(sorted(factors))