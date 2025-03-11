import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic_integers():
    """Test sorting of basic integer list"""
    arr = [5, 2, 9, 1, 7]
    assert tree_sort(arr) == [1, 2, 5, 7, 9]

def test_tree_sort_already_sorted():
    """Test list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test list sorted in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert tree_sort(arr) == [1, 2, 3, 4, 5]

def test_tree_sort_with_duplicates():
    """Test list with duplicate values"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert tree_sort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_tree_sort_empty_list():
    """Test sorting of an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    assert tree_sort(arr) == [42]

def test_tree_sort_floating_point():
    """Test sorting of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert tree_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_tree_sort_negative_numbers():
    """Test sorting of list with negative numbers"""
    arr = [-5, 2, -10, 0, 7]
    assert tree_sort(arr) == [-10, -5, 0, 2, 7]

def test_tree_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")

def test_tree_sort_uncomparable_elements():
    """Test handling of uncomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, 2, {}, 4])