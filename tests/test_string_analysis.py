import pytest
from src.string_analysis import count_vowels_consonants

def test_basic_string():
    """Test a basic string with mixed characters."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_uppercase_string():
    """Test a string with uppercase letters."""
    result = count_vowels_consonants("PYTHON")
    assert result == {'vowels': 1, 'consonants': 5}

def test_mixed_case_string():
    """Test a string with mixed case letters."""
    result = count_vowels_consonants("PrOgRaMmInG")
    assert result == {'vowels': 3, 'consonants': 8}

def test_string_with_spaces():
    """Test a string with spaces."""
    result = count_vowels_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_string_with_special_characters():
    """Test a string with special characters."""
    result = count_vowels_consonants("hello, world! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)

def test_non_alphabetic_string():
    """Test a string with only non-alphabetic characters."""
    result = count_vowels_consonants("12345 !@#$%")
    assert result == {'vowels': 0, 'consonants': 0}