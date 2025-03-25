import pytest
from src.longest_palindrome import find_longest_palindromic_substring

def test_palindrome_basic_cases():
    assert find_longest_palindromic_substring("babad") in ["bab", "aba"]
    assert find_longest_palindromic_substring("cbbd") == "bb"

def test_palindrome_edge_cases():
    assert find_longest_palindromic_substring("") == ""
    assert find_longest_palindromic_substring("a") == "a"
    assert find_longest_palindromic_substring("aa") == "aa"

def test_palindrome_multiple_options():
    assert find_longest_palindromic_substring("abcda") == "a"
    assert find_longest_palindromic_substring("racecar") == "racecar"

def test_palindrome_complex_cases():
    assert find_longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
    assert find_longest_palindromic_substring("abba") == "abba"

def test_palindrome_no_palindrome():
    assert find_longest_palindromic_substring("abcdef") in ["a", "b", "c", "d", "e", "f"]

def test_palindrome_case_sensitivity():
    assert find_longest_palindromic_substring("AbBa") == "A"  # Currently only matches single case-sensitive character

def test_palindrome_unicode_support():
    assert find_longest_palindromic_substring("ñañ") == "ñañ"