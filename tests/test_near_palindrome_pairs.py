import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding basic near-palindrome pairs"""
    result = find_near_palindrome_pairs(["abcda", "edcxb", "hello", "olleh"])
    assert len(result) > 0

def test_no_near_palindrome_pairs():
    """Test case with no near-palindrome pairs"""
    result = find_near_palindrome_pairs(["abc", "def", "ghi"])
    assert len(result) == 0

def test_single_near_palindrome():
    """Test case with some strings near-palindromes but no pairs"""
    result = find_near_palindrome_pairs(["abcda", "hello", "world"])
    assert len(result) == 0

def test_multiple_near_palindrome_pairs():
    """Test finding multiple pairs of near-palindromes"""
    result = find_near_palindrome_pairs(["abcda", "edcxb", "abxde", "exdba"])
    # Ensure multiple pairs of near-palindromes can be found
    assert len(result) >= 1

def test_input_type_error():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError):
        find_near_palindrome_pairs("not a list")

def test_input_element_type_error():
    """Test error handling for non-string list elements"""
    with pytest.raises(ValueError):
        find_near_palindrome_pairs(["abc", 123, "def"])

def test_empty_list():
    """Test with an empty list"""
    result = find_near_palindrome_pairs([])
    assert len(result) == 0