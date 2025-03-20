import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram("Debit Card", "Bad Credit") == True
    assert is_anagram("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram(" listen", "silent ") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True
    assert is_anagram("", "non-empty") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("short", "shorter") == False
    assert is_anagram("a", "aa") == False

def test_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    with pytest.raises(TypeError):
        is_anagram("test", None)
    with pytest.raises(TypeError):
        is_anagram(None, None)