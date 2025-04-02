import pytest
from src.sum_unique_elements import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality with unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 6  # 1 + 2 + 3
    assert sum_unique_elements([1, 1, 1, 1]) == 1
    assert sum_unique_elements([5, 4, 3, 5, 4, 2]) == 14  # 5 + 4 + 3 + 2

def test_sum_unique_elements_empty():
    """Test with an empty list"""
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_negative_numbers():
    """Test with negative numbers"""
    assert sum_unique_elements([-1, -2, -1, 3, -2]) == 0  # -1 + -2 + 3

def test_sum_unique_elements_single_element():
    """Test with a single element"""
    assert sum_unique_elements([42]) == 42

def test_sum_unique_elements_invalid_input():
    """Test that TypeError is raised for invalid inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_elements(123)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, '3'])
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, 3.14])