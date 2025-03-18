import pytest
import random
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, Node

def test_cartesian_tree_sort_basic():
    """Test sorting of basic integer list"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_empty_list():
    """Test sorting of an empty list"""
    arr = []
    result = cartesian_tree_sort(arr)
    assert result == []

def test_cartesian_tree_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    result = cartesian_tree_sort(arr)
    assert result == [42]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting of an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    result = cartesian_tree_sort(arr)
    assert result == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting of a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_duplicates():
    """Test sorting of a list with duplicate elements"""
    arr = [3, 3, 3, 2, 2, 1, 1]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_negative_numbers():
    """Test sorting of a list with negative numbers"""
    arr = [-3, 0, -5, 2, -1, 4]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_random():
    """Test sorting of a random list"""
    arr = random.sample(range(-100, 100), 50)
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_float_numbers():
    """Test sorting of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr)

def test_cartesian_tree_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        cartesian_tree_sort("not a list")
        cartesian_tree_sort(123)
        cartesian_tree_sort(None)

def test_build_cartesian_tree_basic():
    """Test basic Cartesian Tree construction"""
    arr = [3, 1, 4]
    root = build_cartesian_tree(arr)
    
    assert root is not None
    assert root.value == 1  # Minimum element becomes root
    assert root.left is None
    
    # Check right subtree
    assert root.right is not None
    assert root.right.value == 3
    assert root.right.right is not None
    assert root.right.right.value == 4