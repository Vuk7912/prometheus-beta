import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello world") == "HeLlO wOrLd"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_sponge_case("a") == "A"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_sponge_case("PyThOn") == "PyThOn"

def test_special_characters():
    """Test conversion with special characters and spaces."""
    assert to_sponge_case("hello, world!") == "HeLlO, wOrLd!"

def test_non_string_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_sponge_case(None)

def test_whitespace_handling():
    """Test handling of multiple whitespace characters."""
    assert to_sponge_case("  spaces  ") == "  SpAcEs  "