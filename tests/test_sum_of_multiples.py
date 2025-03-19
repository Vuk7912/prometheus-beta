import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic_range():
    """Test sum of multiples in a basic range."""
    # Manually calculating the expected values
    sum_1_to_10 = sum(x for x in range(1, 11) if x % 2 == 0 or x % 3 == 0)
    print(f"Sum for range 1 to 10: {sum_1_to_10}")
    assert sum_of_multiples(1, 10) == sum_1_to_10

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
    # Manually calculating the expected values
    sum_1_to_20 = sum(x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0)
    print(f"Sum for range 1 to 20: {sum_1_to_20}")
    assert sum_of_multiples(1, 20) == sum_1_to_20

def test_sum_of_multiples_zero_positive_range():
    """Test with range including zero."""
    # Manually calculating the expected values
    sum_0_to_10 = sum(x for x in range(0, 11) if x % 2 == 0 or x % 3 == 0)
    print(f"Sum for range 0 to 10: {sum_0_to_10}")
    assert sum_of_multiples(0, 10) == sum_0_to_10

def test_sum_of_multiples_zero_range():
    """Test with zero included in the range."""
    # Manually calculating the expected values
    sum_0_to_5 = sum(x for x in range(0, 6) if x % 2 == 0 or x % 3 == 0)
    print(f"Sum for range 0 to 5: {sum_0_to_5}")
    assert sum_of_multiples(0, 5) == sum_0_to_5