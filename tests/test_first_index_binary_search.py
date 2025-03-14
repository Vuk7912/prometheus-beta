import pytest
from src.first_index_binary_search import find_first_occurrence

def test_find_first_occurrence_basic():
    """Test basic functionality of finding first occurrence"""
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    assert find_first_occurrence(arr, 4) == 4
    assert find_first_occurrence(arr, 2) == 1

def test_find_first_occurrence_not_found():
    """Test when target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 6) == -1
    assert find_first_occurrence(arr, 0) == -1

def test_find_first_occurrence_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_occurrence(arr, 1) == -1

def test_find_first_occurrence_single_element():
    """Test with a single-element array"""
    arr = [5]
    assert find_first_occurrence(arr, 5) == 0
    assert find_first_occurrence(arr, 6) == -1

def test_find_first_occurrence_input_validation():
    """Test input validation"""
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        find_first_occurrence(5, 5)
    
    # Test non-integer target
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_first_occurrence([1, 2, 3], "3")
    
    # Test array with non-positive integers
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, 2, -3, 4], 3)
    
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, 2, 0, 4], 3)

def test_find_first_occurrence_large_array():
    """Test with a larger array with multiple occurrences"""
    arr = [1] * 10 + [2] * 20 + [3] * 5
    assert find_first_occurrence(arr, 2) == 10
    assert find_first_occurrence(arr, 3) == 30
    assert find_first_occurrence(arr, 1) == 0