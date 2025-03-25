import pytest
from src.multiply import multiply

def test_multiply_basic():
    """Test basic multiplication of array elements."""
    assert multiply([2, 3, 4]) == [2, 6, 24]

def test_multiply_single_element():
    """Test multiplication with a single element."""
    assert multiply([5]) == [5]

def test_multiply_with_floats():
    """Test multiplication with floating point numbers."""
    assert multiply([1.5, 2, 3]) == [1.5, 3.0, 9.0]

def test_multiply_with_zero():
    """Test multiplication involving zero."""
    assert multiply([1, 0, 5]) == [1, 0, 0]

def test_multiply_negative_numbers():
    """Test multiplication with negative numbers."""
    assert multiply([-2, 3, -4]) == [-2, -6, 24]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        multiply([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        multiply("not a list")

def test_non_numeric_input_raises_error():
    """Test that list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        multiply([1, 2, "three"])

def test_mixed_numeric_types():
    """Test multiplication with mixed numeric types (int and float)."""
    assert multiply([2, 3.5, 4]) == [2, 7.0, 28.0]