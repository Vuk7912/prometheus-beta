import pytest
from src.even_sum_odd_count import process_number_list

def test_mixed_numbers():
    """Test with a list of mixed even and odd numbers."""
    result = process_number_list([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_all_even_numbers():
    """Test with a list of only even numbers."""
    result = process_number_list([2, 4, 6, 8])
    assert result == (20, 0)

def test_all_odd_numbers():
    """Test with a list of only odd numbers."""
    result = process_number_list([1, 3, 5, 7])
    assert result == (0, 4)

def test_empty_list():
    """Test with an empty list."""
    result = process_number_list([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with negative numbers."""
    result = process_number_list([-1, -2, -3, -4, -5])
    assert result == (-6, 3)

def test_zero_included():
    """Test with zero included in the list."""
    result = process_number_list([0, 1, 2, 3])
    assert result == (2, 2)

def test_invalid_input_not_list():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError, match="Input must be a list"):
        process_number_list("not a list")

def test_invalid_input_non_integers():
    """Test that a TypeError is raised when list contains non-integers."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        process_number_list([1, 2, "3", 4])