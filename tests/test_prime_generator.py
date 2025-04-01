import pytest
from src.prime_generator import generate_primes

def test_generate_primes_default():
    """Test prime generation with default limit of 100."""
    primes = generate_primes()
    # Expected primes up to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert primes == expected_primes, "Default prime generation failed"

def test_generate_primes_small_limit():
    """Test prime generation with a small limit."""
    primes = generate_primes(10)
    assert primes == [2, 3, 5, 7], "Prime generation for small limit failed"

def test_generate_primes_edge_cases():
    """Test edge cases for prime generation."""
    # Test with minimum valid input
    assert generate_primes(2) == [2], "Failed to handle minimum limit"
    
    # Test with larger prime limit
    assert 101 not in generate_primes(100), "Primes above limit should not be included"

def test_generate_primes_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Limit must be at least 2"):
        generate_primes(1)
    
    with pytest.raises(ValueError, match="Limit must be at least 2"):
        generate_primes(0)
    
    with pytest.raises(ValueError, match="Limit must be at least 2"):
        generate_primes(-5)

def test_generate_primes_type_error():
    """Test type checking for input."""
    with pytest.raises(TypeError):
        generate_primes("not a number")
    
    with pytest.raises(TypeError):
        generate_primes(None)