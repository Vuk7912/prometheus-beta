import pytest
from src.anagram import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("Astronomer", "Moon starer") == True

def test_whitespace_handling():
    """Test handling of whitespace in anagram check"""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("conversation", "voices rant on") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("a", "aa") == False

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_anagram(123, "abc")
    with pytest.raises(TypeError):
        is_anagram("abc", None)
    with pytest.raises(TypeError):
        is_anagram([], "abc")