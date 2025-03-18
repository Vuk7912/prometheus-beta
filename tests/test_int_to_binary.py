import pytest
from src.int_to_binary import int_to_binary

def test_zero_conversion():
    """Test conversion of zero."""
    assert int_to_binary(0) == "0"

def test_small_positive_integers():
    """Test conversion of small positive integers."""
    assert int_to_binary(1) == "1"
    assert int_to_binary(2) == "10"
    assert int_to_binary(5) == "101"
    assert int_to_binary(10) == "1010"

def test_larger_integers():
    """Test conversion of larger integers."""
    assert int_to_binary(255) == "11111111"
    assert int_to_binary(1024) == "10000000000"

def test_negative_input_raises_error():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        int_to_binary(-1)

def test_non_integer_input_raises_error():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary(None)