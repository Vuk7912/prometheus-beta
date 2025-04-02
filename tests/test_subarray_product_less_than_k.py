import pytest
from src.subarray_product_less_than_k import count_subarrays_with_product_less_than_k

def test_basic_case():
    """Test a basic scenario with a simple array."""
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 8

def test_empty_array():
    """Test an empty input array."""
    nums = []
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_all_elements_less_than_k():
    """Test when all elements are less than k."""
    nums = [1, 2, 3, 4]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 10

def test_no_valid_subarrays():
    """Test when no subarrays have product less than k."""
    nums = [10, 20, 30]
    k = 5
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array():
    """Test an array with a single element."""
    nums = [5]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 1

def test_invalid_k_raises_error():
    """Test that an invalid k raises a ValueError."""
    nums = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_with_product_less_than_k(nums, 0)
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_with_product_less_than_k(nums, -1)

def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_subarrays_with_product_less_than_k(123, 10)
    
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        count_subarrays_with_product_less_than_k([1, 2, -3], 10)
    
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        count_subarrays_with_product_less_than_k([1, 2, 3.5], 10)