import pytest
from src.consecutive_sequence import find_longest_consecutive_sequence

def test_standard_case():
    """Test a standard case with multiple sequences"""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_longer_sequence():
    """Test a longer consecutive sequence"""
    assert find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_list():
    """Test an empty list input"""
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    """Test a list with a single element"""
    assert find_longest_consecutive_sequence([5]) == [5]

def test_no_consecutive_sequence():
    """Test a list with no consecutive numbers"""
    assert find_longest_consecutive_sequence([5, 10, 15, 20]) == [5]

def test_duplicate_numbers():
    """Test a list with duplicate numbers"""
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_unsorted_input():
    """Test an unsorted input list"""
    result = find_longest_consecutive_sequence([9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6, 2])
    assert result == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_negative_numbers():
    """Test a list with negative numbers"""
    assert find_longest_consecutive_sequence([-5, -4, -3, -2, 0, 1, 3]) == [-5, -4, -3, -2]