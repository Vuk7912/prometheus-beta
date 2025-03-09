import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_normal_string():
    """Test reversing a normal string"""
    s = list('hello')
    reverse_string_in_place(s)
    assert s == list('olleh')

def test_reverse_single_character():
    """Test reversing a single character list"""
    s = list('a')
    reverse_string_in_place(s)
    assert s == list('a')

def test_reverse_empty_list():
    """Test reversing an empty list"""
    s = []
    reverse_string_in_place(s)
    assert s == []

def test_reverse_even_length_string():
    """Test reversing a string with even number of characters"""
    s = list('python')
    reverse_string_in_place(s)
    assert s == list('nohtyp')

def test_reverse_odd_length_string():
    """Test reversing a string with odd number of characters"""
    s = list('code')
    reverse_string_in_place(s)
    assert s == list('edoc')

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_in_place("not a list")
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_in_place(123)
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_in_place(None)