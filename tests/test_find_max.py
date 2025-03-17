import pytest
from src.find_max import find_max

def test_find_max_positive_numbers():
    """Test finding max in an array of positive numbers."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 5, 8, 12, 3]) == 12

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers."""
    assert find_max([-1, 0, 5, -10, 3]) == 5
    assert find_max([-5, -3, -1, -10]) == -1

def test_find_max_floating_point():
    """Test finding max in an array with floating-point numbers."""
    assert find_max([1.5, 2.7, 0.3, 4.1]) == 4.1
    assert find_max([-1.5, -2.7, -0.3]) == -0.3

def test_find_max_single_element():
    """Test finding max in a single-element array."""
    assert find_max([42]) == 42

def test_find_max_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max([])

def test_find_max_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max(123)

def test_find_max_non_numeric_elements_raises_error():
    """Test that arrays with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max([1, 2, None])