import pytest
from src.unique_sorted_list import get_unique_sorted_integers

def test_basic_unique_sorted_list():
    """Test with a basic list of integers with duplicates."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert get_unique_sorted_integers(input_list) == expected

def test_already_sorted_list():
    """Test with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test with an empty list."""
    assert get_unique_sorted_integers([]) == []

def test_list_with_negative_numbers():
    """Test with a list containing negative numbers."""
    input_list = [-3, 0, 3, -3, 1, 0, 2]
    expected = [-3, 0, 1, 2, 3]
    assert get_unique_sorted_integers(input_list) == expected

def test_single_element_list():
    """Test with a list containing a single element."""
    assert get_unique_sorted_integers([42]) == [42]

def test_input_not_a_list():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_list_with_non_integers():
    """Test that a TypeError is raised for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])