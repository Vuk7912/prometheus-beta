def generate_primes(limit=100):
    """
    Generate all prime numbers from 2 to the given limit (inclusive).
    
    Args:
        limit (int, optional): The upper limit for prime number generation. 
                                Defaults to 100.
    
    Returns:
        list: A sorted list of prime numbers from 2 to limit.
    
    Raises:
        ValueError: If limit is less than 2.
    """
    # Validate input
    if limit < 2:
        raise ValueError("Limit must be at least 2")
    
    # Use Sieve of Eratosthenes algorithm for efficient prime generation
    # Create a boolean array "is_prime[0..limit]" and initialize 
    # all entries it as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve of Eratosthenes algorithm
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    # Collect and return prime numbers
    return [num for num in range(2, limit + 1) if is_prime[num]]