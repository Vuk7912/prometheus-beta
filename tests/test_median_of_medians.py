import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import select_kth_smallest

def test_basic_selection():
    """Test basic functionality of kth smallest selection."""
    arr = [7, 10, 4, 3, 20, 15]
    assert select_kth_smallest(arr, 3) == 7
    assert select_kth_smallest(arr, 1) == 3
    assert select_kth_smallest(arr, 6) == 20

def test_sorted_array():
    """Test selection in a sorted array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 5) == 5
    assert select_kth_smallest(arr, 9) == 9

def test_reverse_sorted_array():
    """Test selection in a reverse sorted array."""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 5) == 5
    assert select_kth_smallest(arr, 9) == 9

def test_duplicate_elements():
    """Test selection with duplicate elements."""
    arr = [3, 3, 3, 3, 3, 3, 3]
    assert select_kth_smallest(arr, 1) == 3
    assert select_kth_smallest(arr, 4) == 3
    assert select_kth_smallest(arr, 7) == 3

def test_mixed_elements():
    """Test selection with mixed positive and negative elements."""
    arr = [-5, 10, 0, -3, 8, 5, -1, 6]
    assert select_kth_smallest(arr, 1) == -5
    assert select_kth_smallest(arr, 4) == -1
    assert select_kth_smallest(arr, 8) == 10

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        select_kth_smallest([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        select_kth_smallest([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        select_kth_smallest([1, 2, 3], 4)

def test_large_array():
    """Test selection in a large array."""
    arr = list(range(1000, 0, -1))  # Reverse sorted large array
    assert select_kth_smallest(arr, 1) == 1
    assert select_kth_smallest(arr, 500) == 500
    assert select_kth_smallest(arr, 1000) == 1000

def test_single_element_array():
    """Test selection in a single-element array."""
    arr = [42]
    assert select_kth_smallest(arr, 1) == 42