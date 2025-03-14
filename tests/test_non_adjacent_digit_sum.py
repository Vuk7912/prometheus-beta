import pytest
from src.non_adjacent_digit_sum import max_non_adjacent_digit_sum

def test_single_digit():
    """Test with a single digit number."""
    assert max_non_adjacent_digit_sum(5) == 5

def test_two_digit_number():
    """Test with a two digit number."""
    assert max_non_adjacent_digit_sum(12) == 2
    assert max_non_adjacent_digit_sum(21) == 3

def test_multiple_digit_number():
    """Test with multi-digit numbers."""
    assert max_non_adjacent_digit_sum(123) == 4
    assert max_non_adjacent_digit_sum(1234) == 5
    assert max_non_adjacent_digit_sum(1010) == 2
    assert max_non_adjacent_digit_sum(1111) == 2

def test_zero():
    """Test with zero."""
    assert max_non_adjacent_digit_sum(0) == 0

def test_large_number():
    """Test with a larger number."""
    assert max_non_adjacent_digit_sum(98765) == 20

def test_invalid_input():
    """Test error cases."""
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(-1)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum("123")
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(3.14)