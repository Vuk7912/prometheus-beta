import pytest
from src.quick_sort import quick_sort

def test_quick_sort_basic():
    """Test basic sorting of a random list of integers"""
    input_list = [3, 6, 8, 10, 1, 2, 1]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_empty_list():
    """Test sorting an empty list"""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element"""
    assert quick_sort([42]) == [42]

def test_quick_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert quick_sort(input_list) == input_list

def test_quick_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 2, 2]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-1, -5, 10, 0, 3, -3]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_floating_point():
    """Test sorting a list with floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert quick_sort(input_list) == expected

def test_quick_sort_original_list_unchanged():
    """Ensure the original list is not modified"""
    input_list = [3, 1, 4, 1, 5, 9]
    original_copy = input_list.copy()
    quick_sort(input_list)
    assert input_list == original_copy

def test_quick_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        quick_sort("not a list")
    
    with pytest.raises(TypeError):
        quick_sort(123)
    
    with pytest.raises(TypeError):
        quick_sort(None)