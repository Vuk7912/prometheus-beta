import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_basic_near_palindrome_pairs():
    """Test finding basic near-palindrome pairs"""
    result = find_near_palindrome_pairs(["abcda", "edcba", "hello", "olleh"])
    assert len(result) == 2
    assert ["abcda", "edcba"] in result or ["edcba", "abcda"] in result

def test_no_near_palindrome_pairs():
    """Test case with no near-palindrome pairs"""
    result = find_near_palindrome_pairs(["abc", "def", "ghi"])
    assert len(result) == 0

def test_single_near_palindrome():
    """Test case with some strings near-palindromes"""
    result = find_near_palindrome_pairs(["abcda", "hello", "world"])
    assert len(result) == 0

def test_multiple_near_palindrome_pairs():
    """Test finding multiple pairs of near-palindromes"""
    result = find_near_palindrome_pairs(["abcda", "edcba", "abxde", "exdba"])
    assert len(result) == 2

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