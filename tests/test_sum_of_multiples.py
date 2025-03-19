import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic_range():
    """Test sum of multiples in a basic range."""
    assert sum_of_multiples(1, 10) == 33  # 2+3+4+6+8+9+10 = 33

def test_sum_of_multiples_single_number():
    """Test when min and max are the same number."""
    assert sum_of_multiples(3, 3) == 3
    assert sum_of_multiples(2, 2) == 2
    assert sum_of_multiples(5, 5) == 0

def test_sum_of_multiples_empty_range():
    """Test when min is greater than max."""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        sum_of_multiples(10, 5)

def test_sum_of_multiples_large_range():
    """Test with a larger range of numbers."""
    assert sum_of_multiples(1, 20) == 78  # Sum of multiples of 2 or 3 up to 20

def test_sum_of_multiples_negative_numbers():
    """Test with range including zero."""
    assert sum_of_multiples(0, 10) == 33  # Includes multiples in range with zero

def test_sum_of_multiples_zero_range():
    """Test with zero included in the range."""
    assert sum_of_multiples(0, 5) == 15  # 2+3+4+6 = 15