import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_list = [1, 2, 3, 2, 1, 4]
    assert remove_duplicates(input_list) == [1, 2, 3, 4]

def test_remove_duplicates_strings():
    """Test removing duplicates from a list of strings"""
    input_list = ['a', 'b', 'a', 'c', 'b']
    assert remove_duplicates(input_list) == ['a', 'b', 'c']

def test_remove_duplicates_empty_list():
    """Test handling of an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    input_list = [1, 'a', 1, 'b', 'a']
    assert remove_duplicates(input_list) == [1, 'a', 'b']

def test_remove_duplicates_preserve_order():
    """Test that original order of first occurrence is preserved"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert remove_duplicates(input_list) == [3, 1, 4, 5, 9, 2, 6]