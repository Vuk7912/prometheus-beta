import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test behavior with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("hello", "") == ""
    assert longest_common_subsequence("", "world") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_identical_strings():
    """Test when both strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_partial_matches():
    """Test strings with partial matches"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BDAB"
    assert longest_common_subsequence("XMJYAUZ", "MZJAWXU") == "MJAU"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == "ello"

def test_type_error():
    """Test type checking"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "test")

def test_special_characters():
    """Test with special characters"""
    assert longest_common_subsequence("a!b@c#", "x!y@z#") == "!@#"
    assert longest_common_subsequence("hello, world!", "hello world") == "hello world"