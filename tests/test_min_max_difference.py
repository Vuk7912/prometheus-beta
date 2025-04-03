import pytest
from src.min_max_difference import find_min_max_difference

def test_basic_positive_numbers():
    """Test with a simple string of positive numbers."""
    assert find_min_max_difference("1,5,3,9") == 8

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert find_min_max_difference("-5,10,3,0") == 15

def test_single_number():
    """Test with a single number."""
    assert find_min_max_difference("7") == 0

def test_repeated_numbers():
    """Test with repeated numbers."""
    assert find_min_max_difference("4,4,4,4") == 0

def test_whitespace_handling():
    """Test handling of whitespace around numbers."""
    assert find_min_max_difference(" 1 , 5 , 3 , 9 ") == 8

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_min_max_difference("")

def test_invalid_input_raises_error():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a comma-separated string of integers"):
        find_min_max_difference("1,2,three,4")

def test_only_commas_raises_error():
    """Test that a string with only commas raises a ValueError."""
    with pytest.raises(ValueError, match="No valid integers found in the input string"):
        find_min_max_difference(",,")