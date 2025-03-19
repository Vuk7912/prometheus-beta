import pytest
from src.list_utils import find_common

def test_find_common_basic():
    """Test finding common elements in two lists"""
    assert sorted(find_common([1, 2, 3], [3, 4, 5])) == [3]

def test_find_common_multiple():
    """Test finding multiple common elements"""
    assert sorted(find_common([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4]

def test_find_common_no_duplicates():
    """Test that result has no duplicates"""
    assert sorted(find_common([1, 1, 2, 2], [1, 2, 3])) == [1, 2]

def test_find_common_empty_lists():
    """Test with empty lists"""
    assert find_common([], []) == []
    assert find_common([1, 2], []) == []
    assert find_common([], [1, 2]) == []

def test_find_common_no_match():
    """Test when no common elements exist"""
    assert find_common([1, 2], [3, 4]) == []

def test_find_common_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_common(None, [1, 2])
    with pytest.raises(TypeError):
        find_common([1, 2], "not a list")
    with pytest.raises(TypeError):
        find_common("not a list", [1, 2])