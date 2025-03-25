import pytest
from src.gcd import gcd

def test_gcd_normal_numbers():
    """Test GCD calculation for normal positive integers"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1
    assert gcd(100, 75) == 25

def test_gcd_zero():
    """Test GCD calculation when one number is zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_one():
    """Test GCD calculation when one number is one"""
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1

def test_gcd_negative_numbers():
    """Test GCD calculation with negative numbers"""
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD calculation with identical numbers"""
    assert gcd(7, 7) == 7
    assert gcd(42, 42) == 42

def test_gcd_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        gcd(3.14, 5)
    with pytest.raises(ValueError):
        gcd("10", 5)
    with pytest.raises(ValueError):
        gcd([10], 5)