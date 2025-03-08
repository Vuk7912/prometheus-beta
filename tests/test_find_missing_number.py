import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard case."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_at_start():
    """Test when the missing number is at the start of the range."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_at_end():
    """Test when the missing number is at the end of the range."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_single_element():
    """Test with a single element list."""
    assert find_missing_number([2]) == 1

def test_find_missing_number_invalid_input():
    """Test handling of invalid inputs."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])
    
    with pytest.raises(ValueError, match="Array must contain only integers"):
        find_missing_number([1, 2, '3', 4])

def test_find_missing_number_unsorted():
    """Test that the function works with unsorted input."""
    assert find_missing_number([3, 1, 5, 4]) == 2