import pytest
from src.find_smallest_multiple import find_smallest_multiple_of_five

def test_basic_functionality():
    """Test basic scenarios with different array inputs."""
    assert find_smallest_multiple_of_five([1, 2, 3]) == 4
    assert find_smallest_multiple_of_five([3, 1, 2]) == 4
    assert find_smallest_multiple_of_five([10, 20]) == 1

def test_negative_numbers():
    """Test arrays with negative numbers."""
    assert find_smallest_multiple_of_five([-1, -2, -3]) == 1
    assert find_smallest_multiple_of_five([1, -1, 2]) == 3

def test_floating_point_numbers():
    """Test arrays with floating point numbers."""
    assert find_smallest_multiple_of_five([1.5, 2.5]) == 1

def test_zero_input():
    """Test array with zero."""
    assert find_smallest_multiple_of_five([0]) == 5

def test_input_validation():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five("not a list")
    
    with pytest.raises(TypeError):
        find_smallest_multiple_of_five([1, 2, "three"])
    
    with pytest.raises(ValueError):
        find_smallest_multiple_of_five([])

def test_large_numbers():
    """Test with large numbers."""
    assert find_smallest_multiple_of_five([10000, 20000]) == 1
    assert find_smallest_multiple_of_five([-10000, 10000]) == 5