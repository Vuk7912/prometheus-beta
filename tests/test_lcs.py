import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"
    assert longest_common_subsequence("Hello", "Hello") == "Hello"
    assert longest_common_subsequence("HELLO", "hello") == ""

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_repeated_characters():
    """Test with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BDAB"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)

def test_long_strings():
    """Test with longer strings"""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    # Either first or last character will be a valid LCS
    result = longest_common_subsequence(str1, str2)
    assert result in ["A", "Z"]