import pytest
from src.unique_word_counter import count_unique_words

def test_basic_unique_word_count():
    """Test basic unique word counting"""
    assert count_unique_words("Hello, hello! How are you?") == 4

def test_empty_string():
    """Test empty string returns 0"""
    assert count_unique_words("") == 0

def test_whitespace_string():
    """Test string with only whitespace returns 0"""
    assert count_unique_words("   ") == 0

def test_case_insensitive():
    """Test case-insensitive word counting"""
    assert count_unique_words("Hello HELLO hello") == 1

def test_punctuation_handling():
    """Test removal of punctuation"""
    assert count_unique_words("Hello, hello! world.") == 2

def test_complex_text():
    """Test more complex text with multiple punctuation marks"""
    text = "The quick brown fox, jumps over the lazy dog! The quick brown fox."
    assert count_unique_words(text) == 8

def test_unicode_characters():
    """Test handling of text with Unicode characters"""
    assert count_unique_words("Café café CAFE") == 1

def test_numbers_and_words():
    """Test text with numbers and words"""
    assert count_unique_words("hello 123 Hello 123 world") == 3