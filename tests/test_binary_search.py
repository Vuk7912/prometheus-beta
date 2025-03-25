import pytest
from src.binary_search import binary_search

def test_binary_search_normal_cases():
    """Test binary search in typical scenarios."""
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_binary_search_not_found():
    """Test cases where target is not in the array."""
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1

def test_binary_search_edge_cases():
    """Test edge cases like empty array and single-element array."""
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 4) == -1

def test_binary_search_duplicate_elements():
    """Test binary search with duplicate elements."""
    assert binary_search([1, 2, 2, 3, 3, 3, 4], 3) in [3, 4, 5]

def test_binary_search_large_sorted_array():
    """Test binary search on a large sorted array."""
    large_arr = list(range(0, 1000, 2))
    assert binary_search(large_arr, 500) == large_arr.index(500)
    assert binary_search(large_arr, 501) == -1