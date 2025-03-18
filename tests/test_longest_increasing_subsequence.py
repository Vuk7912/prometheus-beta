import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence_length

def test_empty_array():
    """Test that an empty array returns 0."""
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element():
    """Test that a single-element array returns 1."""
    assert longest_increasing_subsequence_length([5]) == 1

def test_no_increasing_subsequence():
    """Test an array with no increasing subsequence."""
    assert longest_increasing_subsequence_length([5,4,3,2,1]) == 1

def test_simple_increasing_subsequence():
    """Test a simple increasing subsequence."""
    assert longest_increasing_subsequence_length([1,2,3,4,5]) == 5

def test_mixed_subsequences():
    """Test an array with multiple subsequences."""
    assert longest_increasing_subsequence_length([1,3,5,4,7]) == 3

def test_repeated_elements():
    """Test an array with repeated elements."""
    assert longest_increasing_subsequence_length([2,2,2,2]) == 1

def test_multiple_increasing_subsequences():
    """Test an array with multiple increasing subsequences."""
    assert longest_increasing_subsequence_length([1,2,3,1,2,3,4]) == 4

def test_negative_numbers():
    """Test an array with negative numbers."""
    assert longest_increasing_subsequence_length([-3,-2,-1,0,1,2]) == 6

def test_mixed_positive_negative():
    """Test an array with mixed positive and negative numbers."""
    assert longest_increasing_subsequence_length([-1,2,3,4,-5,6,7]) == 4