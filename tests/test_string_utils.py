import pytest
from src.string_utils import remove_char_length

def test_remove_char_length_basic():
    """Test basic functionality of removing a character and getting length."""
    assert remove_char_length("hello", "l") == 3

def test_remove_char_length_no_char():
    """Test when the character to remove is not in the string."""
    assert remove_char_length("hello", "x") == 5

def test_remove_char_length_empty_string():
    """Test with an empty string."""
    assert remove_char_length("", "a") == 0

def test_remove_char_length_multiple_chars():
    """Test removing multiple instances of a character."""
    assert remove_char_length("banana", "a") == 3

def test_remove_char_length_entire_string():
    """Test when the character removes the entire string."""
    assert remove_char_length("xxxx", "x") == 0

def test_remove_char_length_type_error():
    """Test type error handling."""
    with pytest.raises(TypeError):
        remove_char_length(123, "a")
    with pytest.raises(TypeError):
        remove_char_length("hello", 123)

def test_remove_char_length_value_error():
    """Test value error for multi-character input."""
    with pytest.raises(ValueError):
        remove_char_length("hello", "ab")