import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test a normal array with multiple unique numbers."""
    assert find_second_largest([1, 5, 2, 8, 3]) == 5

def test_array_with_duplicates():
    """Test an array with duplicate numbers."""
    assert find_second_largest([1, 5, 5, 8, 3]) == 3

def test_all_same_numbers():
    """Test an array with all same numbers."""
    assert find_second_largest([4, 4, 4, 4]) is None

def test_two_unique_numbers():
    """Test an array with exactly two unique numbers."""
    assert find_second_largest([1, 2]) == 1

def test_single_element_array():
    """Test an array with a single element."""
    assert find_second_largest([1]) is None

def test_empty_array():
    """Test an empty array."""
    assert find_second_largest([]) is None

def test_negative_numbers():
    """Test an array with negative numbers."""
    assert find_second_largest([-1, -5, -2, -8, -3]) == -2

def test_mixed_number_types():
    """Test an array with mixed integer and float types."""
    assert find_second_largest([1.5, 2, 3.7, 1]) == 2

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        find_second_largest("not a list")

def test_non_numeric_elements():
    """Test that a list with non-numeric elements raises a ValueError."""
    with pytest.raises(ValueError):
        find_second_largest([1, 2, 'a', 3])