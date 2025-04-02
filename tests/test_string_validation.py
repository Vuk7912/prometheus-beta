import pytest
from src.string_validation import is_numeric_string

def test_valid_numeric_string():
    """Test that purely numeric strings return True."""
    assert is_numeric_string("12345") == True
    assert is_numeric_string("0") == True
    assert is_numeric_string("9876543210") == True

def test_invalid_numeric_string():
    """Test that strings with non-digit characters return False."""
    assert is_numeric_string("123a45") == False
    assert is_numeric_string("12 345") == False
    assert is_numeric_string("-123") == False
    assert is_numeric_string("3.14") == False

def test_empty_string():
    """Test that an empty string returns False."""
    assert is_numeric_string("") == False

def test_whitespace_string():
    """Test that strings with only whitespace return False."""
    assert is_numeric_string(" ") == False
    assert is_numeric_string("\t") == False
    assert is_numeric_string("\n") == False

def test_error_handling():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        is_numeric_string(12345)
    
    with pytest.raises(TypeError):
        is_numeric_string(None)
    
    with pytest.raises(TypeError):
        is_numeric_string(["123"])