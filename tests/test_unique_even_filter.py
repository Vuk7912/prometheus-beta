import pytest
from src.unique_even_filter import filter_unique_even_numbers

def test_filter_unique_even_numbers():
    # Test with mixed numbers including repeats
    assert filter_unique_even_numbers([1, 2, 3, 4, 2, 5, 6, 4, 7, 8]) == [2, 4, 6, 8]

def test_filter_no_even_numbers():
    # Test with only odd numbers
    assert filter_unique_even_numbers([1, 3, 5, 7]) == []

def test_filter_empty_list():
    # Test with empty list
    assert filter_unique_even_numbers([]) == []

def test_filter_all_unique_even():
    # Test with all unique even numbers
    assert filter_unique_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_filter_preserves_order():
    # Test that original order is preserved
    assert filter_unique_even_numbers([8, 2, 6, 2, 4, 8, 6]) == [8, 2, 6, 4]

def test_filter_with_negative_numbers():
    # Test with negative numbers
    assert filter_unique_even_numbers([-2, 1, -2, 3, 4, -4, 5]) == [-2, 4, -4]