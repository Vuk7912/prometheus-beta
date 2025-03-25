import pytest
from src.longest_unique_substring import longest_unique_substring_length

def test_longest_unique_substring_length():
    # Test cases from the docstring
    assert longest_unique_substring_length("abcabcbb") == 3
    assert longest_unique_substring_length("bbbbb") == 1
    assert longest_unique_substring_length("") == 0
    
    # Additional test cases
    assert longest_unique_substring_length("pwwkew") == 3
    assert longest_unique_substring_length("dvdf") == 3
    
    # Edge cases
    assert longest_unique_substring_length(" ") == 1
    assert longest_unique_substring_length("au") == 2
    
    # Long string with unique characters
    assert longest_unique_substring_length("abcdefghijklmnopqrstuvwxyz") == 26
    
    # String with partial repeats
    assert longest_unique_substring_length("aab") == 2
    assert longest_unique_substring_length("abba") == 2
    
    # Unicode characters
    assert longest_unique_substring_length("こんにちは") == 5
    
    # Mixed character types
    assert longest_unique_substring_length("a1B2c3D4") == 8