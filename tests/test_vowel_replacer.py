import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_lowercase():
    assert replace_vowels("hello") == "hulli"
    assert replace_vowels("world") == "wurld"
    assert replace_vowels("python") == "pythin"

def test_replace_vowels_uppercase():
    assert replace_vowels("HELLO") == "HULLI"
    assert replace_vowels("WORLD") == "WURLD"
    assert replace_vowels("PYTHON") == "PYTHIN"

def test_replace_vowels_mixed_case():
    assert replace_vowels("HelloWorld") == "HulluWurld"
    assert replace_vowels("PythOn") == "PythIn"

def test_replace_vowels_empty_string():
    assert replace_vowels("") == ""

def test_replace_vowels_no_vowels():
    assert replace_vowels("rhythm") == "rhythm"

def test_replace_vowels_only_vowels():
    assert replace_vowels("aeiou") == "eioua"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_repeated_vowels():
    assert replace_vowels("banana") == "benene"
    assert replace_vowels("BANANA") == "BENENE"

def test_replace_vowels_with_punctuation_and_spaces():
    assert replace_vowels("Hello, World!") == "Hulli, Wurld!"
    assert replace_vowels("Open source is awesome") == "Ipun saurcu os ewusumu"