import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios"""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert sorted(result) == sorted([[0, 1], [1, 0]])

def test_empty_list():
    """Test with an empty list"""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    """Test with a single word"""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_palindrome_with_empty_string():
    """Test palindrome pairs involving an empty string"""
    words = ["", "a", "ab"]
    result = find_palindrome_pairs(words)
    expected_pairs = sorted([[0, 1], [1, 0], [0, 2], [2, 0]])
    assert sorted(result) == expected_pairs

def test_multiple_palindrome_pairs():
    """Test multiple palindrome pairs in a single list"""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected_pairs = sorted([[0, 1], [1, 0], [2, 4], [3, 2]])
    assert sorted(result) == expected_pairs

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        find_palindrome_pairs("not a list")

def test_invalid_list_element_type():
    """Test that ValueError is raised for non-string list elements"""
    with pytest.raises(ValueError):
        find_palindrome_pairs(["valid", 123, "string"])

def test_case_sensitivity():
    """Test that palindrome pairs are case-sensitive"""
    words = ["Abc", "cba"]
    result = find_palindrome_pairs(words)
    assert result == []