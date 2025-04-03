import pytest
from src.find_first_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an index"""
    assert find_first_index([1, 2, 3, 2, 1], 2) == 1
    assert find_first_index([1, 2, 3], 3) == 2

def test_find_first_index_not_found():
    """Test when target is not in the array"""
    assert find_first_index([1, 2, 3], 4) == -1

def test_find_first_index_empty_array():
    """Test with an empty array"""
    assert find_first_index([], 1) == -1

def test_find_first_index_multiple_occurrences():
    """Test that only the first occurrence is returned"""
    assert find_first_index([1, 2, 2, 3], 2) == 1

def test_find_first_index_different_types():
    """Test with different types of elements"""
    assert find_first_index([1, 'a', True, 'a', 2], 'a') == 1
    assert find_first_index([1, 'a', True, 'a', 2], True) == 2

def test_find_first_index_edge_cases():
    """Test various edge cases"""
    # None as target
    assert find_first_index([1, None, 2], None) == 1
    
    # Strings
    assert find_first_index(['hello', 'world', 'hello'], 'world') == 1
    
    # Mixed types
    assert find_first_index([1, '1', True], '1') == 1