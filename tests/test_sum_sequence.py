import pytest
from src.sum_sequence import sum_to_n

def test_sum_to_n_basic():
    """Test basic functionality of sum_to_n function."""
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(0) == 0

def test_sum_to_n_large_number():
    """Test sum_to_n with larger numbers."""
    assert sum_to_n(100) == 5050
    assert sum_to_n(1000) == 500500

def test_sum_to_n_edge_cases():
    """Test edge cases and error handling."""
    with pytest.raises(ValueError):
        sum_to_n(-1)
    
    with pytest.raises(TypeError):
        sum_to_n(3.14)
    
    with pytest.raises(TypeError):
        sum_to_n("10")