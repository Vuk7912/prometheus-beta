import pytest
from src.string_converter import to_constant_case

def test_basic_string_conversion():
    """Test basic string conversion to constant case."""
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("helloWorld") == "HELLO_WORLD"
    assert to_constant_case("hello-world") == "HELLO_WORLD"
    assert to_constant_case("hello_world") == "HELLO_WORLD"

def test_special_characters():
    """Test handling of special characters and mixed inputs."""
    assert to_constant_case("hello@world") == "HELLO_WORLD"
    assert to_constant_case("hello world!") == "HELLO_WORLD"
    assert to_constant_case("Hello123World") == "HELLO_123_WORLD"

def test_empty_and_whitespace_inputs():
    """Test edge cases with empty and whitespace strings."""
    assert to_constant_case("") == ""
    assert to_constant_case("   ") == ""
    assert to_constant_case(" hello ") == "HELLO"

def test_invalid_input_type():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_constant_case(123)
    
    with pytest.raises(TypeError):
        to_constant_case(None)

def test_complex_string_conversions():
    """Test more complex string conversion scenarios."""
    assert to_constant_case("snake_case_string") == "SNAKE_CASE_STRING"
    assert to_constant_case("camelCaseString") == "CAMEL_CASE_STRING"
    assert to_constant_case("mixed-Case_String") == "MIXED_CASE_STRING"
    assert to_constant_case("   mixed Case   String   ") == "MIXED_CASE_STRING"