import pytest
from src.filter_even_numbers import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test filtering even numbers from a sorted list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_all_odd():
    """Test list with no even numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_all_even():
    """Test list with all even numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == input_list

def test_filter_even_numbers_empty_list():
    """Test empty input list."""
    assert filter_even_numbers([]) == []

def test_filter_even_numbers_negative_numbers():
    """Test list with negative and positive numbers."""
    input_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [-4, -2, 0, 2, 4]
    assert filter_even_numbers(input_list) == expected

def test_filter_even_numbers_invalid_input_type():
    """Test handling of invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_even_numbers("not a list")

def test_filter_even_numbers_unsorted_list():
    """Test handling of unsorted list."""
    with pytest.raises(ValueError, match="Input list must be sorted with unique elements"):
        filter_even_numbers([3, 1, 2, 4, 5])

def test_filter_even_numbers_duplicate_elements():
    """Test handling of list with duplicate elements."""
    with pytest.raises(ValueError, match="Input list must be sorted with unique elements"):
        filter_even_numbers([1, 2, 2, 3, 4, 5])