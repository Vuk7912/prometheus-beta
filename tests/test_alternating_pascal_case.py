import pytest
from src.alternating_pascal_case import convert_to_alternating_pascal_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating Pascal case."""
    assert convert_to_alternating_pascal_case("hello world") == 'HelloWorldHello'

def test_string_with_special_characters():
    """Test conversion of string with special characters."""
    assert convert_to_alternating_pascal_case("python-is_awesome") == 'PythonIsAwesomePython'

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_pascal_case("") == ''

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_alternating_pascal_case("hello") == 'Hello'

def test_multiple_consecutive_special_characters():
    """Test conversion with multiple consecutive special characters."""
    assert convert_to_alternating_pascal_case("hello---world__test") == 'HelloWorldTestHello'

def test_numbers_in_string():
    """Test conversion of string with numbers."""
    assert convert_to_alternating_pascal_case("hello2world3test") == 'Hello2World3TestHello'

def test_error_non_string_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_pascal_case(123)

def test_string_with_mixed_case():
    """Test conversion of string with mixed case."""
    assert convert_to_alternating_pascal_case("HelloWORLD") == 'HelloWorldHello'

def test_only_special_characters():
    """Test conversion of string with only special characters."""
    assert convert_to_alternating_pascal_case("---___") == ''