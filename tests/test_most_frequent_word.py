import pytest
from src.most_frequent_word import most_frequent_word

def test_basic_functionality():
    """Test basic word frequency detection."""
    text = "the quick brown fox jumps over the lazy dog"
    assert most_frequent_word(text) == "the"

def test_single_word():
    """Test a text with only one word."""
    text = "hello"
    assert most_frequent_word(text) == "hello"

def test_multiple_same_frequency():
    """Test when multiple words have the same frequency."""
    text = "a b c a b c"
    result = most_frequent_word(text)
    assert result in ["a", "b", "c"]

def test_empty_text_raises_error():
    """Test that empty text raises a ValueError."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        most_frequent_word("")

def test_only_spaces_raises_error():
    """Test that text with only spaces raises a ValueError."""
    with pytest.raises(ValueError, match="No words found in the input text"):
        most_frequent_word("   ")

def test_invalid_characters_raises_error():
    """Test that input with invalid characters raises a ValueError."""
    with pytest.raises(ValueError, match="Input text must contain only lowercase letters and spaces"):
        most_frequent_word("hello 123 world")

def test_case_sensitivity():
    """Verify that the function works with lowercase letters."""
    text = "apple banana apple cherry banana"
    assert most_frequent_word(text) == "apple"