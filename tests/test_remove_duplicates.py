import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a simple string."""
    assert remove_duplicates("hello") == "helo"

def test_remove_duplicates_preserve_order():
    """Ensure the first occurrence of each character is preserved."""
    assert remove_duplicates("banana") == "ban"

def test_remove_duplicates_mixed_case():
    """Test string with mixed case characters."""
    assert remove_duplicates("HeLLo") == "HeLo"

def test_remove_duplicates_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicates("") == ""

def test_remove_duplicates_no_duplicates():
    """Test string with no duplicate characters."""
    assert remove_duplicates("abcdef") == "abcdef"

def test_remove_duplicates_all_duplicates():
    """Test string with all duplicate characters."""
    assert remove_duplicates("aaaaaa") == "a"

def test_remove_duplicates_special_characters():
    """Test string with special characters and duplicates."""
    assert remove_duplicates("a!b!c") == "a!bc"

def test_remove_duplicates_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicates(None)