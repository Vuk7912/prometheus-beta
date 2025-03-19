import pytest
from src.array_extremes_avg import calculate_extremes_average

def test_basic_functionality():
    """Test with a standard set of numbers."""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_extremes_average(numbers) == 3.5

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    numbers = [-10, -5, 0, 5, 10, 15]
    assert calculate_extremes_average(numbers) == 2.5

def test_floating_point_numbers():
    """Test with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_extremes_average(numbers) == 4.0

def test_zero_numbers():
    """Test with zero and positive numbers."""
    numbers = [0, 0, 0, 1, 2, 3]
    assert calculate_extremes_average(numbers) == 1.0

def test_invalid_input_length():
    """Test that an error is raised for incorrect number of inputs."""
    with pytest.raises(ValueError, match="Input must be a list of exactly 6 numbers"):
        calculate_extremes_average([1, 2, 3, 4, 5])
    
    with pytest.raises(ValueError, match="Input must be a list of exactly 6 numbers"):
        calculate_extremes_average([1, 2, 3, 4, 5, 6, 7])