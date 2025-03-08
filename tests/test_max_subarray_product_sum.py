import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_case():
    """Test a basic scenario with a clear subarray match."""
    arr = [1, 2, 3, 4]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 5  # 2 + 3

def test_multiple_subarrays():
    """Test when multiple subarrays match the target product."""
    arr = [1, 2, 3, 2, 4]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 9  # 3 + 2 + 4

def test_no_matching_subarray():
    """Test when no subarray matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 100
    assert find_max_subarray_product_sum(arr, target_product) == -1

def test_single_element_exact_match():
    """Test when a single element matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 3
    assert find_max_subarray_product_sum(arr, target_product) == 3

def test_entire_array_match():
    """Test when the entire array matches the target product."""
    arr = [1, 2, 3]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 6

def test_invalid_input_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)

def test_invalid_input_non_positive():
    """Test that an array with non-positive integers raises a ValueError."""
    with pytest.raises(ValueError, match="Input array must contain only positive integers"):
        find_max_subarray_product_sum([1, 2, -3, 4], 10)

def test_large_input():
    """Test with a larger input to check performance and correctness."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_product = 120
    assert find_max_subarray_product_sum(arr, target_product) == 54  # 6 + 7 + 8 + 9 + 10