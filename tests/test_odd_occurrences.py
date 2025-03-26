import pytest
from src.odd_occurrences import find_number_with_odd_occurrences

def test_basic_odd_occurrence():
    """Test basic scenario with a single odd occurrence number."""
    assert find_number_with_odd_occurrences([1, 1, 2, 2, 3]) == 3

def test_multiple_odd_occurrences():
    """Test scenario with multiple numbers having odd occurrences."""
    assert find_number_with_odd_occurrences([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 3

def test_all_same_numbers():
    """Test scenario where all numbers are the same."""
    assert find_number_with_odd_occurrences([5, 5, 5]) == 5

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_number_with_odd_occurrences([])

def test_no_odd_occurrence_raises_error():
    """Test that a list with no number appearing odd times raises a ValueError."""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_number_with_odd_occurrences([1, 1, 2, 2, 3, 3])

def test_large_numbers():
    """Test with large numbers."""
    assert find_number_with_odd_occurrences([10000, 10000, 20000, 20000, 30000, 30000, 40000]) == 40000

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_number_with_odd_occurrences([-1, -1, 2, 2, -3]) == -3