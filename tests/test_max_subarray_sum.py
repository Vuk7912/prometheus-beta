import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test case with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test case with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test case with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test case with a single element."""
    assert max_subarray_sum([42]) == 42

def test_zero_elements():
    """Test case with zero."""
    assert max_subarray_sum([0, 0, 0]) == 0

def test_invalid_input_type():
    """Test raising TypeError for invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test raising ValueError for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])