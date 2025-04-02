import pytest
from src.gnome_sort import gnome_sort

def test_basic_sorting():
    """Test basic list sorting"""
    assert gnome_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_already_sorted():
    """Test list that is already sorted"""
    assert gnome_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test list in reverse order"""
    assert gnome_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test empty list"""
    assert gnome_sort([]) == []

def test_single_element():
    """Test list with single element"""
    assert gnome_sort([42]) == [42]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    assert gnome_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_negative_numbers():
    """Test list with negative numbers"""
    assert gnome_sort([-1, -5, 10, 0, -3]) == [-5, -3, -1, 0, 10]

def test_mixed_types_same_type():
    """Test sorting of strings"""
    assert gnome_sort(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']

def test_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        gnome_sort("not a list")

def test_large_list():
    """Test sorting of a larger list"""
    large_list = list(range(100, 0, -1))
    assert gnome_sort(large_list) == list(range(1, 101))