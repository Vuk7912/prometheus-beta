import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test basic sorting of a simple list of integers"""
    input_list = [4, 2, 7, 1, 5, 3]
    expected = [1, 2, 3, 4, 5, 7]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == input_list

def test_spaghetti_sort_reverse_sorted():
    """Test list that is in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_empty_list():
    """Test empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test list with a single element"""
    input_list = [42]
    assert spaghetti_sort(input_list) == [42]

def test_spaghetti_sort_with_duplicates():
    """Test list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_floats():
    """Test sorting with floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        spaghetti_sort("not a list")

def test_spaghetti_sort_non_comparable():
    """Test that ValueError is raised for non-comparable elements"""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        spaghetti_sort([1, 2, [3], 4])

def test_spaghetti_sort_preserves_original():
    """Test that the original list is not modified"""
    input_list = [4, 2, 7, 1, 5, 3]
    original_copy = input_list.copy()
    spaghetti_sort(input_list)
    assert input_list == original_copy