import pytest
from src.string_utils import find_longest_common_suffix

def test_common_suffix_basic():
    """Test finding a common suffix in multiple strings."""
    strings = ["flower", "power", "tower"]
    assert find_longest_common_suffix(strings) == "ower"

def test_common_suffix_single_string():
    """Test with a single string."""
    strings = ["hello"]
    assert find_longest_common_suffix(strings) == "hello"

def test_common_suffix_empty_list():
    """Test with an empty list."""
    strings = []
    assert find_longest_common_suffix(strings) == ""

def test_common_suffix_no_common_suffix():
    """Test with strings that have no common suffix."""
    strings = ["abc", "def", "ghi"]
    assert find_longest_common_suffix(strings) == ""

def test_common_suffix_different_lengths():
    """Test with strings of different lengths."""
    strings = ["longer", "short", "mega"]
    assert find_longest_common_suffix(strings) == ""

def test_common_suffix_case_sensitive():
    """Test case sensitivity of suffix matching."""
    strings = ["hellO", "wellO", "fallO"]
    assert find_longest_common_suffix(strings) == "llO"

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_list_element_type():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["string", 123, "another"])

def test_minimal_common_suffix():
    """Test finding a minimal single-character common suffix."""
    strings = ["a", "ba", "ca"]
    assert find_longest_common_suffix(strings) == "a"