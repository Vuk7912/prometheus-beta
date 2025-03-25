import pytest
from src.integer_sorter import sort_comma_separated_integers

def test_basic_sorting():
    """Test basic comma-separated integer sorting."""
    assert sort_comma_separated_integers("3,1,4,1,5,9") == [1, 1, 3, 4, 5, 9]

def test_with_whitespace():
    """Test sorting with whitespace around numbers."""
    assert sort_comma_separated_integers(" 3 , 1 , 4 ") == [1, 3, 4]

def test_with_non_integer_characters():
    """Test sorting when non-integer characters are present."""
    assert sort_comma_separated_integers("10,abc,20,def,30") == [10, 20, 30]

def test_negative_numbers():
    """Test sorting with negative numbers."""
    assert sort_comma_separated_integers("-3,-1,0,2,-2") == [-3, -2, -1, 0, 2]

def test_empty_string():
    """Test behavior with an empty string."""
    assert sort_comma_separated_integers("") == []

def test_no_valid_integers():
    """Test behavior when no valid integers are present."""
    assert sort_comma_separated_integers("hello,world") == []

def test_single_number():
    """Test sorting with a single number."""
    assert sort_comma_separated_integers("42") == [42]

def test_mixed_valid_invalid():
    """Test sorting with a mix of valid and invalid inputs."""
    assert sort_comma_separated_integers("10,abc,20,def,30") == [10, 20, 30]