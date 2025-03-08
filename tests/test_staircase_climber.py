import pytest
from src.staircase_climber import count_staircase_ways

def test_basic_staircase():
    """Test a simple staircase with known climbing ways."""
    assert count_staircase_ways([1, 1, 1]) == 3  # Short staircase
    assert count_staircase_ways([1, 2, 1]) == 2  # Mixed step sizes

def test_single_step_staircase():
    """Test staircases with single-step lengths."""
    assert count_staircase_ways([1]) == 1
    assert count_staircase_ways([1, 1]) == 2
    assert count_staircase_ways([1, 1, 1]) == 3

def test_two_step_staircase():
    """Test staircases with two-step lengths."""
    assert count_staircase_ways([2]) == 1
    assert count_staircase_ways([2, 1]) == 1
    assert count_staircase_ways([1, 2]) == 1

def test_long_staircase():
    """Test a longer staircase with mixed step sizes."""
    assert count_staircase_ways([1, 2, 3, 1]) == 5

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="must be a non-empty list"):
        count_staircase_ways([])
    
    with pytest.raises(ValueError, match="must be a non-empty list"):
        count_staircase_ways(None)
    
    with pytest.raises(ValueError, match="must be positive integers"):
        count_staircase_ways([0, 1, 2])
    
    with pytest.raises(ValueError, match="must be positive integers"):
        count_staircase_ways([-1, 2, 3])

def test_complex_staircase():
    """Comprehensive test of various staircase configurations."""
    test_cases = [
        ([1, 1, 1, 1], 5),    # 4-step uniform
        ([2, 2], 1),           # Two 2-step lengths
        ([1, 2, 1, 1], 3),     # Mixed length
    ]
    
    for stair_lengths, expected_ways in test_cases:
        assert count_staircase_ways(stair_lengths) == expected_ways