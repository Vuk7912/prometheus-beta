import pytest
from src.bubble_sort import bubble_sort

def test_basic_sorting():
    """Test basic list sorting"""
    assert bubble_sort([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]

def test_already_sorted_list():
    """Test list that is already sorted"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test list in reverse order"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test list with duplicate elements"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_empty_list():
    """Test empty list"""
    assert bubble_sort([]) == []

def test_single_element_list():
    """Test list with a single element"""
    assert bubble_sort([42]) == [42]

def test_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bubble_sort("not a list")

def test_mixed_type_list():
    """Test list with comparable mixed types"""
    assert bubble_sort([3, 1.5, 2, 4]) == [1.5, 2, 3, 4]

def test_negative_numbers():
    """Test sorting with negative numbers"""
    assert bubble_sort([-5, 0, -3, 2, 1]) == [-5, -3, 0, 1, 2]