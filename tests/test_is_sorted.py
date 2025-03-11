import pytest
from src.is_sorted import is_sorted

def test_sorted_ascending_positive():
    """Test ascending sorted list of positive integers"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 1, 2, 3, 3]) == True

def test_sorted_descending_positive():
    """Test descending sorted list of positive integers"""
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True
    assert is_sorted([5, 5, 4, 3, 3], ascending=False) == True

def test_empty_and_single_element_list():
    """Test empty and single-element lists"""
    assert is_sorted([]) == True
    assert is_sorted([42]) == True
    assert is_sorted([], ascending=False) == True
    assert is_sorted([42], ascending=False) == True

def test_unsorted_list():
    """Test unsorted lists"""
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([5, 4, 6, 3, 2], ascending=False) == False

def test_different_types():
    """Test lists with different types of comparable elements"""
    assert is_sorted(['a', 'b', 'c']) == True
    assert is_sorted(['c', 'b', 'a'], ascending=False) == True

def test_mixed_types_with_comparison():
    """Test lists with mixed types that can be compared"""
    assert is_sorted([1, 1.5, 2, 2.5, 3]) == True
    assert is_sorted([3, 2.5, 2, 1.5, 1], ascending=False) == True

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        is_sorted(123)
    with pytest.raises(TypeError):
        is_sorted("not a list")
    with pytest.raises(TypeError):
        is_sorted(None)