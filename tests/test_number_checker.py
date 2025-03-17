import pytest
from src.number_checker import is_even_or_odd

def test_positive_even_numbers():
    """Test even positive numbers."""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(100) == 'even'
    assert is_even_or_odd(3000) == 'even'

def test_positive_odd_numbers():
    """Test odd positive numbers."""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(101) == 'odd'
    assert is_even_or_odd(3001) == 'odd'

def test_negative_numbers():
    """Test even and odd negative numbers."""
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'

def test_invalid_inputs():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    with pytest.raises(TypeError):
        is_even_or_odd('not a number')
    with pytest.raises(TypeError):
        is_even_or_odd([2])
    with pytest.raises(TypeError):
        is_even_or_odd(None)