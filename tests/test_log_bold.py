import pytest
from io import StringIO
import sys

from src.log_bold import log_bold

def test_log_bold_normal_message(capsys):
    """Test logging a normal message in bold."""
    result = log_bold("Hello, World!")
    captured = capsys.readouterr()
    
    assert result == "\033[1mHello, World!\033[0m"
    assert captured.out.strip() == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("")

def test_log_bold_non_string_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(42)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(None)

def test_log_bold_special_characters(capsys):
    """Test logging messages with special characters."""
    result = log_bold("!@#$%^&*()_+")
    captured = capsys.readouterr()
    
    assert result == "\033[1m!@#$%^&*()_+\033[0m"
    assert captured.out.strip() == "\033[1m!@#$%^&*()_+\033[0m"