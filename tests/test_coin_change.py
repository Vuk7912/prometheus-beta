import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-value coins
    assert min_coins([1], 100) == 100  # Can make any amount with 1-value coins

def test_zero_amount():
    """Test when amount is zero"""
    assert min_coins([1, 2, 5], 0) == 0

def test_edge_cases():
    """Test various edge cases"""
    assert min_coins([2, 5, 10, 1], 27) == 4  # 10 + 10 + 5 + 2
    assert min_coins([186, 419, 83, 408], 6249) == 20

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([1, -2, 5], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0], 10)

def test_single_coin_denomination():
    """Test scenarios with a single coin denomination"""
    assert min_coins([1], 5) == 5
    assert min_coins([2], 6) == 3
    assert min_coins([5], 15) == 3

def test_large_amount():
    """Test handling of larger amounts"""
    assert min_coins([1, 5, 10, 25], 100) == 4  # 4 * 25-cent coins
    
def test_impossible_change():
    """Test scenarios where exact change is impossible"""
    assert min_coins([2], 3) == -1
    assert min_coins([5, 10], 7) == -1