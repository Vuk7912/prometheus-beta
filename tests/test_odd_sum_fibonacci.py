import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic functionality of the sequence generator."""
    result = generate_odd_sum_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_odd_sum_property():
    """Verify that the sum of any two consecutive numbers is odd."""
    sequence = generate_odd_sum_fibonacci(10)
    for i in range(1, len(sequence)):
        assert (sequence[i-1] + sequence[i]) % 2 == 1, \
            f"Sum of {sequence[i-1]} and {sequence[i]} is not odd"

def test_edge_cases():
    """Test edge cases like 0, 1, and 2 terms."""
    assert generate_odd_sum_fibonacci(0) == [], "Zero terms should return empty list"
    assert generate_odd_sum_fibonacci(1) == [0], "One term should return [0]"
    assert generate_odd_sum_fibonacci(2) == [0, 1], "Two terms should return [0, 1]"

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_odd_sum_fibonacci(-1)

def test_type_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci("5")

def test_longer_sequence():
    """Test a longer sequence to ensure the odd sum property holds."""
    sequence = generate_odd_sum_fibonacci(15)
    assert len(sequence) == 15, f"Expected 15 terms, got {len(sequence)}"
    for i in range(1, len(sequence)):
        assert (sequence[i-1] + sequence[i]) % 2 == 1, \
            f"Sum of {sequence[i-1]} and {sequence[i]} is not odd"