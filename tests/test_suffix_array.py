import pytest
from src.suffix_array import create_suffix_array, search_in_suffix_array

def test_create_suffix_array_basic():
    """Test basic suffix array creation"""
    text = "banana"
    suffix_arr = create_suffix_array(text)
    assert suffix_arr == [5, 3, 1, 0, 4, 2]
    
    # Validate that indices correspond to sorted suffixes
    sorted_suffixes = sorted(text[i:] for i in range(len(text)))
    assert [text[idx:] for idx in suffix_arr] == sorted_suffixes

def test_create_suffix_array_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        create_suffix_array(123)
    
    with pytest.raises(ValueError):
        create_suffix_array("")

def test_search_in_suffix_array_basic():
    """Test basic pattern searching in suffix array"""
    text = "banana"
    
    # Search for existing patterns
    assert search_in_suffix_array(text, "ana") == [1, 3]
    assert search_in_suffix_array(text, "an") == [1, 3]
    assert search_in_suffix_array(text, "banana") == [0]

def test_search_in_suffix_array_edge_cases():
    """Test edge cases and boundary conditions"""
    text = "banana"
    
    # Search for non-existent patterns
    assert search_in_suffix_array(text, "xyz") == []
    
    # Search with single character patterns
    assert search_in_suffix_array(text, "a") == [1, 3, 5]

def test_search_in_suffix_array_precomputed_array():
    """Test searching with a precomputed suffix array"""
    text = "banana"
    suffix_arr = create_suffix_array(text)
    
    assert search_in_suffix_array(text, "ana", suffix_arr) == [1, 3]

def test_search_in_suffix_array_error_handling():
    """Test error handling for search function"""
    with pytest.raises(TypeError):
        search_in_suffix_array(123, "pattern")
    
    with pytest.raises(TypeError):
        search_in_suffix_array("text", 123)
    
    with pytest.raises(ValueError):
        search_in_suffix_array("", "pattern")
    
    with pytest.raises(ValueError):
        search_in_suffix_array("text", "")

def test_long_text_pattern_matching():
    """Test pattern matching in a longer text"""
    text = "abracadabra"
    
    assert search_in_suffix_array(text, "abra") == [0, 7]
    assert search_in_suffix_array(text, "cad") == [4]

def test_case_sensitivity():
    """Verify case-sensitive pattern matching"""
    text = "Hello World"
    
    assert search_in_suffix_array(text, "o") == [4, 7]
    assert search_in_suffix_array(text, "O") == []