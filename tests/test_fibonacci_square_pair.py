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
    
    # Check first two elements are 1
    assert sequence[:2] == [1, 1]

def test_sequence_square_pair_property():
    """Test that consecutive pair sums are perfect squares."""
    for n in range(1, 10):
        sequence = generate_fibonacci_square_pair_sequence(n)
        
        # Starting from the second pair
        for i in range(1, len(sequence)):
            pair_sum = sequence[i-1] + sequence[i]
            assert is_perfect_square(pair_sum), \
                f"Pair sum {pair_sum} at index {i} is not a perfect square"

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

def test_sequence_growth():
    """Verify the sequence grows correctly."""
    for n in range(1, 10):
        sequence = generate_fibonacci_square_pair_sequence(n)
        
        # Verify every pair generates a square sum
        for i in range(1, len(sequence)):
            assert is_perfect_square(sequence[i-1] + sequence[i]), \
                f"Failed at sequence length {n}, index {i}"