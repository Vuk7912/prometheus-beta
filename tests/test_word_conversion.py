import pytest
from src.word_conversion import can_convert_by_deleting_one_char

def test_successful_conversions():
    assert can_convert_by_deleting_one_char('abc', 'ac') == True
    assert can_convert_by_deleting_one_char('abcd', 'abc') == True
    assert can_convert_by_deleting_one_char('abcd', 'abd') == True

def test_failed_conversions():
    assert can_convert_by_deleting_one_char('abc', 'abc') == False
    assert can_convert_by_deleting_one_char('abc', 'abcd') == False
    assert can_convert_by_deleting_one_char('abc', 'def') == False

def test_edge_cases():
    # Empty strings
    assert can_convert_by_deleting_one_char('a', '') == True
    assert can_convert_by_deleting_one_char('', 'a') == False

def test_invalid_inputs():
    with pytest.raises(TypeError):
        can_convert_by_deleting_one_char(123, 'abc')
    with pytest.raises(TypeError):
        can_convert_by_deleting_one_char('abc', 456)