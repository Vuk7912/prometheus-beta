import pytest
from src.digit_array_multiply import multiply_digit_arrays

def test_basic_multiplication():
    """Test basic digit array multiplication"""
    assert multiply_digit_arrays([1,2,3], [4,5,6]) == [5, 6, 0, 8, 8]

def test_zero_multiplication():
    """Test multiplication with zero"""
    assert multiply_digit_arrays([0,0,0], [1,2,3]) == [0]
    assert multiply_digit_arrays([1,2,3], [0,0,0]) == [0]

def test_single_digit():
    """Test multiplication with single-digit numbers"""
    assert multiply_digit_arrays([5], [7]) == [3, 5]

def test_unequal_length_raises_error():
    """Test that unequal length arrays raise an error"""
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1,2], [3,4,5])

def test_non_digit_raises_error():
    """Test that non-digit values raise an error"""
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1,2,10], [3,4,5])
    
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1,2,3], [-1,4,5])
    
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1,2,3], ['a',4,5])

def test_large_numbers():
    """Test multiplication of larger numbers"""
    assert multiply_digit_arrays([9,9,9], [9,9,9]) == [9, 9, 8, 0, 0, 1]