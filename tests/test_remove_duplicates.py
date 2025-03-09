import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicates([1, 2, 3, 2, 1, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_empty_list():
    """Test with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicate elements."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_preserve_order():
    """Test that the order of first occurrence is preserved."""
    assert remove_duplicates([3, 1, 2, 3, 1, 4, 2]) == [3, 1, 2, 4]

def test_remove_duplicates_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_non_integer_elements():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, "3", 4])

def test_remove_duplicates_mixed_types_fail():
    """Test that a ValueError is raised for mixed-type list."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, 3.5, 4])