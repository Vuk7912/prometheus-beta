import pytest
from src.string_utils import rotate_and_reverse

def test_basic_rotation_and_reverse():
    """Test basic string rotation and reversal."""
    assert rotate_and_reverse("hello", 2) == "olleh"
    assert rotate_and_reverse("python", 3) == "nohtyp"

def test_full_rotation():
    """Test rotations equal to string length."""
    assert rotate_and_reverse("world", 5) == "dlrow"
    assert rotate_and_reverse("world", 10) == "dlrow"

def test_zero_rotations():
    """Test when no rotations are performed."""
    assert rotate_and_reverse("test", 0) == "tset"

def test_empty_string():
    """Test empty string handling."""
    assert rotate_and_reverse("", 5) == ""

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        rotate_and_reverse(123, 2)
    
    with pytest.raises(TypeError, match="Rotations must be an integer"):
        rotate_and_reverse("hello", "2")

def test_negative_rotations():
    """Test error handling for negative rotations."""
    with pytest.raises(ValueError, match="Rotations cannot be negative"):
        rotate_and_reverse("hello", -1)

def test_large_rotations():
    """Test handling of rotations larger than string length."""
    assert rotate_and_reverse("abcde", 7) == "decba"
    assert rotate_and_reverse("abcde", 12) == "decba"