import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Madam, I'm Adam") == True

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a.b,c:d") == False
    assert is_palindrome("a") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False

def test_edge_cases():
    """Test edge cases like empty string, single character, etc."""
    assert is_palindrome(" ") == True
    assert is_palindrome("  ") == True
    assert is_palindrome("!@#") == True