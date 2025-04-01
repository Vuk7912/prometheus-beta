"""
Test module for file_reader functionality.

This module contains comprehensive tests for the read_text_file function,
covering various scenarios and edge cases.
"""

import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_valid_text_file():
    """Test reading a valid text file with simple content."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, World!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, World!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_file_with_unicode():
    """Test reading a file with Unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)

def test_read_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent_file.txt")

def test_read_directory():
    """Test that IsADirectoryError is raised when path is a directory."""
    with pytest.raises(IsADirectoryError):
        read_text_file(".")

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        read_text_file(123)  # Passing an integer instead of a string