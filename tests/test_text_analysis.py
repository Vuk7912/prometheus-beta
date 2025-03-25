import pytest
from src.text_analysis import count_vowels_consonants

def test_basic_text():
    """Test a basic sentence with mixed characters."""
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_mixed_case():
    """Test text with mixed upper and lower case."""
    result = count_vowels_consonants("AbCdEfG")
    assert result == {'vowels': 2, 'consonants': 5}

def test_with_spaces_and_punctuation():
    """Test text with spaces and punctuation."""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
        count_vowels_consonants(None)
        count_vowels_consonants(["hello"])