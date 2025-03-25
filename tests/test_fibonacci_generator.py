import pytest
from src.fibonacci_generator import generate_fibonacci

def test_fibonacci_base_cases():
    """Test the base cases for Fibonacci generation."""
    assert generate_fibonacci(1) == 1
    assert generate_fibonacci(2) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    # Check first few known Fibonacci numbers
    assert generate_fibonacci(3) == 2
    assert generate_fibonacci(4) == 3
    assert generate_fibonacci(5) == 5
    assert generate_fibonacci(6) == 8
    assert generate_fibonacci(7) == 13

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fibonacci(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fibonacci(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be a positive integer"):
        generate_fibonacci(1.5)
    with pytest.raises(TypeError, match="Input must be a positive integer"):
        generate_fibonacci("3")
    with pytest.raises(TypeError, match="Input must be a positive integer"):
        generate_fibonacci(None)