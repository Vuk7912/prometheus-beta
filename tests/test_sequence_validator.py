import pytest
from src.sequence_validator import is_valid_increasing_sequence

def test_valid_increasing_sequences():
    """Test various valid increasing sequences."""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True
    assert is_valid_increasing_sequence([-5, -3, 0, 2, 4]) == True

def test_invalid_increasing_sequences():
    """Test various invalid increasing sequences."""
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_increasing_sequence([1, 1, 2, 3]) == False
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False

def test_edge_cases():
    """Test edge cases like empty list and single-element list."""
    assert is_valid_increasing_sequence([]) == True
    assert is_valid_increasing_sequence([42]) == True

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        is_valid_increasing_sequence("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        is_valid_increasing_sequence(123)
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        is_valid_increasing_sequence([1, 2, "3", 4])
    
    with pytest.raises(ValueError, match="All elements must be integers"):
        is_valid_increasing_sequence([1, 2, 3.5, 4])