import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    # Sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_fibonacci_input_validation():
    """Test input validation for Fibonacci function."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers."""
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610