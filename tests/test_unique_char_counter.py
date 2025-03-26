import pytest
from src.unique_char_counter import count_unique_characters

def test_unique_characters_basic():
    """Test basic unique character counting."""
    assert count_unique_characters('hello') == 4
    assert count_unique_characters('world') == 5

def test_case_sensitivity():
    """Verify that the function is case-sensitive."""
    assert count_unique_characters('aAaA') == 2
    assert count_unique_characters('AbCa') == 4

def test_edge_cases():
    """Test edge cases like empty string and whitespace."""
    assert count_unique_characters('') == 0
    assert count_unique_characters('   ') == 0
    assert count_unique_characters('\t\n') == 0

def test_special_characters():
    """Test strings with special characters and repetitions."""
    assert count_unique_characters('!!@@##') == 3
    assert count_unique_characters('a1b2c3') == 6

def test_unicode_characters():
    """Test with unicode and non-ASCII characters."""
    assert count_unique_characters('éèêë') == 4
    assert count_unique_characters('こんにちは') == 5