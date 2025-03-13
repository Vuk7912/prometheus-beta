import pytest
from src.fizzy_numbers import find_fizzy_numbers

def test_fizzy_numbers_basic():
    """Test basic functionality of fizzy numbers."""
    assert find_fizzy_numbers(10) == [3, 6, 7, 9]

def test_fizzy_numbers_larger_range():
    """Test fizzy numbers in a larger range."""
    result = find_fizzy_numbers(20)
    expected = [3, 6, 7, 9, 12, 14, 15, 18]
    assert result == expected

def test_fizzy_numbers_edge_cases():
    """Test edge cases like 1 and small ranges."""
    assert find_fizzy_numbers(1) == []
    assert find_fizzy_numbers(2) == []
    assert find_fizzy_numbers(3) == [3]

def test_invalid_input():
    """Test that invalid inputs raise ValueError."""
    with pytest.raises(ValueError):
        find_fizzy_numbers(0)
    
    with pytest.raises(ValueError):
        find_fizzy_numbers(-5)
    
    with pytest.raises(ValueError):
        find_fizzy_numbers(3.5)
    
    with pytest.raises(ValueError):
        find_fizzy_numbers("10")