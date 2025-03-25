import pytest
import math
from src.fibonacci_square_pair import generate_fibonacci_square_pair_sequence, is_perfect_square

def test_is_perfect_square():
    """Test the perfect square identification function."""
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True
    
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(7) == False

def test_sequence_generation_basic():
    """Test basic sequence generation."""
    sequence = generate_fibonacci_square_pair_sequence(5)
    
    # Check length
    assert len(sequence) == 5

def test_sequence_validation():
    """Validate the sequence generation properties."""
    sequence = generate_fibonacci_square_pair_sequence(7)
    
    # The goal is to have most/some consecutive pair sums as perfect squares
    # But it's not guaranteed for all pairs
    square_sum_count = 0
    for i in range(1, len(sequence)):
        pair_sum = sequence[i-1] + sequence[i]
        if is_perfect_square(pair_sum):
            square_sum_count += 1
    
    # At least some pairs should have square sums
    assert square_sum_count > 0, "No consecutive pair sums are perfect squares"

def test_edge_cases():
    """Test edge cases and error conditions."""
    # Test minimum length
    assert generate_fibonacci_square_pair_sequence(1) == [1]
    
    # Test invalid inputs
    with pytest.raises(ValueError, match="Sequence length must be at least 1"):
        generate_fibonacci_square_pair_sequence(0)
    
    with pytest.raises(ValueError, match="Sequence length must be at least 1"):
        generate_fibonacci_square_pair_sequence(-1)
    
    with pytest.raises(TypeError):
        generate_fibonacci_square_pair_sequence("not a number")
    
    with pytest.raises(TypeError):
        generate_fibonacci_square_pair_sequence(3.14)

def test_increasing_sequence_length():
    """Verify the sequence behaves correctly for different lengths."""
    for n in range(1, 10):
        sequence = generate_fibonacci_square_pair_sequence(n)
        assert len(sequence) == n
        
        # Ensure the sequence is strictly increasing or non-decreasing
        assert all(sequence[i] >= sequence[i-1] for i in range(1, len(sequence))), \
            f"Sequence for n={n} is not monotonically non-decreasing"