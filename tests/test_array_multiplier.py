import pytest
from src.array_multiplier import multiply_array_elements

def test_multiply_numeric_arrays():
    """Test multiplication of numeric arrays"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert multiply_array_elements(arr1, arr2) == [4, 10, 18]

def test_multiply_float_arrays():
    """Test multiplication of float arrays"""
    arr1 = [1.5, 2.0, 3.5]
    arr2 = [2.0, 3.0, 1.5]
    assert multiply_array_elements(arr1, arr2) == [3.0, 6.0, 5.25]

def test_multiply_mixed_type_arrays():
    """Test multiplication of mixed type arrays"""
    arr1 = [2, 'hello', 3.5]
    arr2 = [3, 2, 2.0]
    assert multiply_array_elements(arr1, arr2) == [6, 'hellohello', 7.0]

def test_empty_arrays():
    """Test multiplication of empty arrays"""
    assert multiply_array_elements([], []) == []

def test_different_length_arrays():
    """Test that different length arrays raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_array_elements([1, 2], [1, 2, 3])

def test_incompatible_multiplication():
    """Test that truly incompatible types raise TypeError"""
    with pytest.raises(TypeError):
        multiply_array_elements([1, object()], [2, 3])