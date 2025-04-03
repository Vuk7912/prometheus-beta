import pytest
from src.anagram import isAnagram

def test_basic_anagrams():
    """Test basic anagram cases"""
    assert isAnagram("listen", "silent") == True
    assert isAnagram("triangle", "integral") == True
    assert isAnagram("hello", "world") == False

def test_case_insensitive():
    """Test case-insensitive anagram detection"""
    assert isAnagram("Astronomer", "Moon starer") == True
    assert isAnagram("Debit Card", "Bad Credit") == True

def test_whitespace_and_punctuation():
    """Test anagram detection with whitespace and punctuation"""
    assert isAnagram("a decimal point", "im a dot in place") == True
    assert isAnagram("The Morse Code", "Here come dots") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert isAnagram("", "") == True
    assert isAnagram("", "a") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram("abc", "abcd") == False
    assert isAnagram("short", "shorter") == False

def test_single_character():
    """Test single character strings"""
    assert isAnagram("a", "a") == True
    assert isAnagram("a", "b") == False

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert isAnagram("aab", "aba") == True
    assert isAnagram("aab", "abc") == False

def test_non_alphanumeric():
    """Test handling of non-alphanumeric characters"""
    assert isAnagram("a!b@c", "c@b!a") == True
    assert isAnagram("a,b.c", "c.b,a") == True
    assert isAnagram("a!b", "a@c") == False