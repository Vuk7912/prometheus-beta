import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_multiple_words():
    """Test multiple word conversion to sponge case."""
    assert to_sponge_case("hello world") == "HeLlO wOrLd"
    assert to_sponge_case("python programming") == "PyThOn PrOgRaMmInG"

def test_empty_string():
    """Test conversion of empty string."""
    assert to_sponge_case("") == ""

def test_string_with_numbers():
    """Test conversion of string with numbers."""
    assert to_sponge_case("hello123") == "HeLlO123"

def test_string_with_special_characters():
    """Test conversion of string with special characters."""
    # The key point is that alphanumeric characters alternate case
    # while preserving the original spacing and special characters
    result = to_sponge_case("hello, world!")
    # Verify that alphabetic characters alternate, special characters remain
    assert result == "HeLlO, WoRlD!"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    
    with pytest.raises(TypeError):
        to_sponge_case(None)

def test_already_mixed_case():
    """Test conversion of string with mixed case."""
    assert to_sponge_case("HeLLo") == "HeLlO"