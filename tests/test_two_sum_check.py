import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_found():
    """Test when a pair summing to target exists."""
    assert two_sum_check([1, 4, 7, 11], 15) == True

def test_two_sum_check_not_found():
    """Test when no pair summing to target exists."""
    assert two_sum_check([1, 2, 3, 4], 10) == False

def test_two_sum_check_edge_cases():
    """Test various edge cases."""
    # Single element list
    assert two_sum_check([5], 10) == False
    
    # Large numbers
    assert two_sum_check([1000000, -1000000, 500000], 0) == True

def test_two_sum_check_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Non-list input
    with pytest.raises(TypeError):
        two_sum_check(42, 10)
    
    # Non-integer elements
    with pytest.raises(TypeError):
        two_sum_check([1, 2, '3'], 5)
    
    # Empty list
    with pytest.raises(ValueError):
        two_sum_check([], 10)
    
    # Non-unique elements
    with pytest.raises(ValueError):
        two_sum_check([1, 2, 2], 4)

def test_two_sum_check_zero_cases():
    """Test cases involving zero."""
    assert two_sum_check([0, 5, -5], 0) == True
    assert two_sum_check([1, 2, 3], 0) == False

def test_two_sum_check_negative_numbers():
    """Test cases with negative numbers."""
    assert two_sum_check([-1, -2, 3, 4], 2) == True
    assert two_sum_check([-5, -3, -1], -8) == True