import pytest
from src.unique_pairs import get_unique_pairs

def test_normal_list():
    """Test unique pairs for a normal list of integers."""
    result = get_unique_pairs([1, 2, 3])
    assert set(result) == {(1, 2), (1, 3), (2, 3)}
    assert len(result) == 3

def test_empty_list():
    """Test behavior with an empty list."""
    assert get_unique_pairs([]) == []

def test_single_element_list():
    """Test behavior with a single-element list."""
    assert get_unique_pairs([1]) == []

def test_duplicate_elements():
    """Test behavior with duplicate elements."""
    result = get_unique_pairs([1, 1, 2])
    assert set(result) == {(1, 1), (1, 2), (1, 2)}
    assert len(result) == 3

def test_invalid_input_type():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_pairs("not a list")

def test_non_integer_elements():
    """Test error handling for non-integer list elements."""
    with pytest.raises(ValueError, match="All list elements must be integers"):
        get_unique_pairs([1, "2", 3])

def test_large_list():
    """Test with a larger list of integers."""
    large_list = list(range(5))
    result = get_unique_pairs(large_list)
    assert len(result) == 10  # All possible unique pairs
    
    # Verify all combinations
    expected_pairs = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4),
        (3, 4)
    ]
    assert set(result) == set(expected_pairs)