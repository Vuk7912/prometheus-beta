import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitivity():
    """Test case insensitivity"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char():
    """Test empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_mixed_case_with_punctuation():
    """Test mixed case with punctuation"""
    assert is_palindrome("Race a Car") == False

def test_only_punctuation():
    """Test string with only punctuation"""
    assert is_palindrome("!@#$%^") == True