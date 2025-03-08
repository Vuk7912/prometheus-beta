import pytest
from src.sum_odd_even import sum_odd_even_integers

def test_mixed_numbers():
    """Test with a mix of odd and even numbers."""
    result = sum_odd_even_integers([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = sum_odd_even_integers([1, 3, 5, 7])
    assert result == (16, 0)

def test_only_even_numbers():
    """Test with only even numbers."""
    result = sum_odd_even_integers([2, 4, 6, 8])
    assert result == (0, 20)

def test_empty_list():
    """Test with an empty list."""
    result = sum_odd_even_integers([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with negative numbers."""
    result = sum_odd_even_integers([-1, -2, -3, -4, -5])
    assert result == (-9, -6)

def test_zero_included():
    """Test with zero included."""
    result = sum_odd_even_integers([0, 1, 2, 3])
    assert result == (4, 2)

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_odd_even_integers("not a list")

def test_invalid_element_type():
    """Test raising TypeError for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_odd_even_integers([1, 2, "3", 4])