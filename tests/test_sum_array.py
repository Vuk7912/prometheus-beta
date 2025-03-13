import pytest
from src.sum_array import sum_integer_array

def test_sum_basic_array():
    """Test summing a basic list of positive integers."""
    assert sum_integer_array([1, 2, 3, 4]) == 10

def test_sum_negative_integers():
    """Test summing an array with negative integers."""
    assert sum_integer_array([-1, -2, -3, -4]) == -10

def test_sum_mixed_integers():
    """Test summing an array with positive and negative integers."""
    assert sum_integer_array([-1, 0, 1]) == 0

def test_sum_empty_array():
    """Test summing an empty array."""
    assert sum_integer_array([]) == 0

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integer_array("not a list")

def test_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integer_array([1, 2, "3", 4])

def test_large_integers():
    """Test summing large integers."""
    assert sum_integer_array([10**6, 10**6]) == 2 * 10**6