import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_equal_length_arrays():
    """Test median for two arrays of equal length."""
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_different_length_arrays():
    """Test median for arrays of different lengths."""
    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_one_empty_array():
    """Test median when one array is empty."""
    nums1 = []
    nums2 = [1, 2, 3, 4, 5]
    assert find_median_sorted_arrays(nums1, nums2) == 3

def test_odd_total_length():
    """Test median for odd total number of elements."""
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    assert find_median_sorted_arrays(nums1, nums2) == 3.5

def test_even_total_length():
    """Test median for even total number of elements."""
    nums1 = [1, 3]
    nums2 = [2, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

def test_single_element_arrays():
    """Test median for single-element arrays."""
    nums1 = [1]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 1.5

def test_large_arrays():
    """Test median for larger input arrays."""
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10]
    assert find_median_sorted_arrays(nums1, nums2) == 5.5

def test_negative_numbers():
    """Test median with negative numbers."""
    nums1 = [-5, -3, -1]
    nums2 = [-4, -2, 0]
    assert find_median_sorted_arrays(nums1, nums2) == -2.5

def test_both_empty_arrays_raises_error():
    """Test that an error is raised when both arrays are empty."""
    with pytest.raises(ValueError, match="Both input arrays cannot be empty"):
        find_median_sorted_arrays([], [])

def test_unsorted_input_raises_error():
    """Ensure function works with properly sorted inputs."""
    nums1 = [3, 1, 4]  # unsorted
    nums2 = [2, 6, 5]  # unsorted
    with pytest.raises(ValueError, match="Input arrays are not sorted or contain invalid data"):
        find_median_sorted_arrays(nums1, nums2)