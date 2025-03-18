import pytest
from src.fibonacci_utils import fibonacci, fibonacci_sum

def test_fibonacci_basic():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(1) == [1]
    assert fibonacci(2) == [1, 1, 2]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(20) == [1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_zero():
    """Test Fibonacci sequence for zero input"""
    assert fibonacci(0) == []

def test_fibonacci_negative():
    """Test Fibonacci sequence with negative input"""
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_sum_basic():
    """Test basic Fibonacci sum functionality"""
    assert fibonacci_sum([5]) == 7  # 1 + 1 + 2 + 3
    assert fibonacci_sum([10]) == 20  # 1 + 1 + 2 + 3 + 5 + 8
    assert fibonacci_sum([1, 2, 3]) == 7  # 1 + 1 + 2 + 3

def test_fibonacci_sum_empty():
    """Test Fibonacci sum with empty input"""
    assert fibonacci_sum([]) == 0

def test_fibonacci_sum_invalid_input():
    """Test Fibonacci sum with invalid input"""
    with pytest.raises(ValueError):
        fibonacci_sum([0])
    with pytest.raises(ValueError):
        fibonacci_sum([-1, 5])

def test_fibonacci_sum_multiple_numbers():
    """Test Fibonacci sum with multiple different inputs"""
    assert fibonacci_sum([20, 5]) == 20  # 1 + 1 + 2 + 3 + 5 + 8 + 13
    assert fibonacci_sum([1, 10, 20]) == 20