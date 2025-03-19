import pytest
from src.substring_reversal import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal in the middle of a string."""
    assert reverse_substring("hello world", 1, 4) == "hlleo world"

def test_full_string_reversal():
    """Test reversing the entire string."""
    assert reverse_substring("hello", 0, 5) == "olleh"

def test_no_reversal():
    """Test when start and end indices are the same (no change)."""
    assert reverse_substring("hello", 2, 2) == "hello"

def test_single_character_reversal():
    """Test reversing a single character."""
    assert reverse_substring("hello", 1, 2) == "hello"

def test_negative_index_error():
    """Test that negative indices raise a ValueError."""
    with pytest.raises(ValueError, match="Indices must be non-negative"):
        reverse_substring("hello", -1, 3)

def test_out_of_bounds_error():
    """Test that out of bounds indices raise a ValueError."""
    with pytest.raises(ValueError, match="Indices out of string bounds"):
        reverse_substring("hello", 0, 6)

def test_invalid_index_order_error():
    """Test that start index greater than end index raises a ValueError."""
    with pytest.raises(ValueError, match="Start index must be less than or equal to end index"):
        reverse_substring("hello", 3, 2)

def test_empty_string():
    """Test reversal on an empty string."""
    assert reverse_substring("", 0, 0) == ""

def test_edge_cases():
    """Test various edge cases of substring reversal."""
    test_cases = [
        ("abcdef", 0, 0, "abcdef"),  # No change
        ("abcdef", 3, 3, "abcdef"),  # No change
        ("abcdef", 1, 5, "adcbef"),  # Partial reversal
        ("abcdef", 0, 6, "fedcba"),  # Full reversal
    ]
    
    for input_str, start, end, expected in test_cases:
        assert reverse_substring(input_str, start, end) == expected