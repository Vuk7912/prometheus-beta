import pytest
from src.char_frequency import get_char_frequency

def test_basic_frequency():
    """Test basic character frequency counting."""
    result = get_char_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def test_empty_string():
    """Test frequency of an empty string."""
    result = get_char_frequency("")
    assert result == {}

def test_string_with_spaces():
    """Test frequency of a string with spaces."""
    result = get_char_frequency("hello world")
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_special_characters():
    """Test frequency of string with special characters."""
    result = get_char_frequency("a!b@c#")
    assert result == {'a': 1, '!': 1, 'b': 1, '@': 1, 'c': 1, '#': 1}

def test_invalid_input():
    """Test that function raises TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_char_frequency(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        get_char_frequency(None)

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    result = get_char_frequency("Hello")
    assert result == {'H': 1, 'e': 1, 'l': 2, 'o': 1}