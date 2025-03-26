import pytest
from src.unique_even_sum import sum_unique_even_numbers

def test_basic_unique_even_sum():
    """Test basic functionality with unique even numbers"""
    assert sum_unique_even_numbers([2, 4, 6, 8]) == 0
    assert sum_unique_even_numbers([2, 3, 4, 5, 6]) == 2
    assert sum_unique_even_numbers([1, 3, 5, 7]) == 0

def test_repeated_even_numbers():
    """Test cases with repeated even numbers"""
    assert sum_unique_even_numbers([2, 2, 4, 4, 6]) == 0
    assert sum_unique_even_numbers([2, 2, 3, 4, 5]) == 0
    assert sum_unique_even_numbers([2, 3, 4, 5, 2]) == 0

def test_mixed_numbers():
    """Test with a mix of unique and repeated even and odd numbers"""
    assert sum_unique_even_numbers([2, 3, 4, 5, 6, 7, 8, 2, 4]) == 8
    assert sum_unique_even_numbers([10, 11, 12, 10, 12, 13]) == 0

def test_empty_list():
    """Test with an empty list"""
    assert sum_unique_even_numbers([]) == 0

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        sum_unique_even_numbers(None)
    
    with pytest.raises(TypeError):
        sum_unique_even_numbers([1, 2, '3'])
    
    with pytest.raises(TypeError):
        sum_unique_even_numbers(123)

def test_negative_numbers():
    """Test with negative even numbers"""
    assert sum_unique_even_numbers([-2, -4, -2]) == 0
    assert sum_unique_even_numbers([-2, 3, -4, 5, -2]) == -4