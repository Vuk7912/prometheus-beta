import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello"
    result = convert_to_random_case(input_str)
    
    # Assert that the result is the same length
    assert len(result) == len(input_str)
    
    # Assert that the result contains the same characters as the input
    assert sorted(result.lower()) == sorted(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """
    Test that the function produces different results across multiple calls.
    Note: This is a probabilistic test and might occasionally fail.
    """
    input_str = "hello"
    results = set()
    
    # Generate multiple results to check for randomness
    for _ in range(10):
        results.add(convert_to_random_case(input_str))
    
    # If randomness is working, we should have more than one unique result
    assert len(results) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and mixed case input."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Assert the result maintains the same length and characters
    assert len(result) == len(input_str)
    assert sorted(result.lower()) == sorted(input_str.lower())