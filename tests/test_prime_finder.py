import pytest
from src.prime_finder import find_primes_below_n

def test_primes_below_10():
    """Test prime numbers below 10."""
    assert find_primes_below_n(10) == [2, 3, 5, 7]

def test_primes_below_2():
    """Test case when input is less than 2."""
    assert find_primes_below_n(2) == []

def test_primes_below_20():
    """Test prime numbers below 20."""
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_invalid_input_negative():
    """Test handling of negative input."""
    assert find_primes_below_n(-5) == []

def test_invalid_input_type():
    """Test handling of non-integer input."""
    with pytest.raises(TypeError):
        find_primes_below_n(10.5)
    with pytest.raises(TypeError):
        find_primes_below_n("10")
    with pytest.raises(TypeError):
        find_primes_below_n(None)

def test_large_input():
    """Test functionality with a larger input."""
    primes = find_primes_below_n(100)
    # Validate some known primes
    assert 2 in primes
    assert 3 in primes
    assert 97 in primes
    assert 4 not in primes
    assert 25 not in primes
    assert len(primes) == 25  # There are 25 primes below 100