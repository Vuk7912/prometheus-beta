import pytest
from src.missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_start():
    """Test when the missing number is at the start of the sequence."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_end():
    """Test when the missing number is at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_sequence():
    """Test with a larger sequence."""
    full_sequence = list(range(1, 11))
    missing_sequence = full_sequence.copy()
    missing_sequence.remove(7)
    assert find_missing_number(missing_sequence) == 7

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_find_missing_number_unsorted():
    """Test that the function works with unsorted input."""
    assert find_missing_number([5, 2, 1, 4]) == 3