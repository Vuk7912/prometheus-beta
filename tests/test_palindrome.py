import pytest
from src.palindrome import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome strings."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_edge_cases():
    """Test edge cases like empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("!!") == True

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Madam") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("MaDaM") == True

def test_with_numbers():
    """Test palindromes with numbers."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("Python") == False

def test_complex_punctuation():
    """Test palindromes with complex punctuation."""
    assert is_palindrome("Do geese see God?") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True