import pytest
from src.list_average import calculate_average

def test_calculate_average_positive_numbers():
    """Test average calculation with positive numbers"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_negative_numbers():
    """Test average calculation with negative numbers"""
    assert calculate_average([-1, -2, -3, -4, -5]) == -3.0

def test_calculate_average_mixed_numbers():
    """Test average calculation with mixed positive and negative numbers"""
    assert calculate_average([-1, 0, 1]) == 0.0

def test_calculate_average_floats():
    """Test average calculation with float numbers"""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_single_number():
    """Test average calculation with a single number"""
    assert calculate_average([42]) == 42.0

def test_empty_list_raises_value_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_list_input_raises_type_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")

def test_non_numeric_list_raises_type_error():
    """Test that a list with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, "three", 4, 5])