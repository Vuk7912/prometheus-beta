import pytest
from src.patience_sort import patience_sort

def test_basic_sorting():
    """Test basic sorting of integers"""
    input_list = [5, 2, 8, 12, 1, 6]
    assert patience_sort(input_list) == sorted(input_list)

def test_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert patience_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(input_list) == sorted(input_list)

def test_float_sorting():
    """Test sorting a list of floats"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert patience_sort(input_list) == sorted(input_list)

def test_string_sorting():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    assert patience_sort(input_list) == sorted(input_list)

def test_none_input():
    """Test that None input raises a TypeError"""
    with pytest.raises(TypeError):
        patience_sort(None)

def test_incomparable_elements():
    """Test that incomparable elements raise a TypeError"""
    with pytest.raises(TypeError):
        patience_sort([1, "a", 2, "b"])

def test_large_list():
    """Test sorting a large list"""
    import random
    large_list = [random.randint(0, 10000) for _ in range(1000)]
    assert patience_sort(large_list) == sorted(large_list)