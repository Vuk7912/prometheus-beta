import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test with a typical array and valid k"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test with an array of a single element"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_all_same_elements():
    """Test with an array of identical elements"""
    arr = [2, 2, 2, 2, 2]
    assert max_subarray_sum(arr, 3) == 6  # sum of any 3 elements is 6

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, -2, 3, 4, -5, 6, 7]
    assert max_subarray_sum(arr, 3) == 17  # 4 + 6 + 7 = 17

def test_invalid_k_zero():
    """Test with k = 0"""
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum([1, 2, 3], 0)

def test_invalid_k_negative():
    """Test with negative k"""
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        max_subarray_sum([1, 2, 3], -1)

def test_k_larger_than_array():
    """Test with k larger than array length"""
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than array length"):
        max_subarray_sum([1, 2, 3], 4)

def test_empty_array():
    """Test with an empty array"""
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than array length"):
        max_subarray_sum([], 1)