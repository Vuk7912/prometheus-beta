import pytest
from src.string_permutations import generate_unique_permutations

def test_basic_permutations():
    """Test generating permutations for a basic string."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_string_with_duplicates():
    """Test generating permutations for a string with duplicate characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_single_character_string():
    """Test generating permutations for a single character string."""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_input_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)

def test_empty_string_error():
    """Test that ValueError is raised for empty string."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        generate_unique_permutations('')

def test_string_order_consistency():
    """Ensure multiple calls produce consistent results."""
    first_call = generate_unique_permutations('abc')
    second_call = generate_unique_permutations('abc')
    assert first_call == second_call