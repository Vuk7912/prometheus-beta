import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_comma_words("hello,world") == "Hello,World"

def test_already_capitalized():
    """Test when words are already capitalized."""
    assert capitalize_comma_words("Hello,World") == "Hello,World"

def test_mixed_case():
    """Test mixed case input."""
    assert capitalize_comma_words("hElLo,wOrLd") == "Hello,World"

def test_single_word():
    """Test single word input."""
    assert capitalize_comma_words("hello") == "Hello"

def test_multiple_words():
    """Test multiple words."""
    assert capitalize_comma_words("python,is,awesome") == "Python,Is,Awesome"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_comma_words("") == ""

def test_invalid_input_with_whitespace():
    """Test that whitespace raises a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello, world")

def test_invalid_input_with_punctuation():
    """Test that non-alphabetical characters raise a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello!world")

def test_invalid_input_with_numbers():
    """Test that numbers raise a ValueError."""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello42,world")