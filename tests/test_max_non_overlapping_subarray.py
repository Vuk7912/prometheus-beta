import pytest
from src.max_non_overlapping_subarray import max_non_overlapping_subarray_sum

def test_basic_positive_array():
    """Test with a simple positive array"""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9

def test_array_with_negatives():
    """Test array with negative numbers"""
    assert max_non_overlapping_subarray_sum([-1, 2, -3, 4, 5]) == 9

def test_single_element_array():
    """Test array with single element"""
    assert max_non_overlapping_subarray_sum([5]) == 5

def test_two_element_array():
    """Test array with two elements"""
    assert max_non_overlapping_subarray_sum([1, 2]) == 2
    assert max_non_overlapping_subarray_sum([3, 1]) == 3

def test_all_negative_array():
    """Test array with all negative numbers"""
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum("not a list")
    
    with pytest.raises(TypeError):
        max_non_overlapping_subarray_sum(123)

def test_empty_list():
    """Test empty list input"""
    with pytest.raises(ValueError):
        max_non_overlapping_subarray_sum([])

def test_complex_scenarios():
    """Test more complex scenarios"""
    assert max_non_overlapping_subarray_sum([5, -2, 3, 4, -1, 2]) == 9
    assert max_non_overlapping_subarray_sum([1, 20, 3, 4, 5, 6]) == 26
    assert max_non_overlapping_subarray_sum([10, -3, -4, 7, 6, -2]) == 23