import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic_cases():
    # First Fibonacci number (index 1)
    assert fibonacci_sum(1) == 0
    
    # First two Fibonacci numbers (index 2)
    assert fibonacci_sum(2) == 1
    
    # First three Fibonacci numbers (0, 1, 1)
    assert fibonacci_sum(3) == 2
    
    # First four Fibonacci numbers (0, 1, 1, 2)
    assert fibonacci_sum(4) == 4
    
    # First five Fibonacci numbers (0, 1, 1, 2, 3)
    assert fibonacci_sum(5) == 7

def test_fibonacci_sum_larger_n():
    # Verify sum for larger n
    assert fibonacci_sum(10) == 88

def test_fibonacci_sum_invalid_input():
    # Test error handling for invalid inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")