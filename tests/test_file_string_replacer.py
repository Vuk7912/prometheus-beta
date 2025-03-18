"""
Tests for file string replacement functionality.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("hello world hello universe")
    return str(file_path)

def test_replace_string_basic(sample_file):
    """Test basic string replacement."""
    replacements = replace_string_in_file(sample_file, "hello", "hi")
    
    assert replacements == 2
    with open(sample_file, 'r') as file:
        content = file.read()
    assert content == "hi world hi universe"

def test_replace_string_no_replacements(sample_file):
    """Test when no replacements are made."""
    replacements = replace_string_in_file(sample_file, "goodbye", "hi")
    
    assert replacements == 0
    with open(sample_file, 'r') as file:
        content = file.read()
    assert content == "hello world hello universe"

def test_replace_with_empty_new_string(sample_file):
    """Test replacing with an empty string."""
    replacements = replace_string_in_file(sample_file, "hello ", "")
    
    assert replacements == 2
    with open(sample_file, 'r') as file:
        content = file.read()
    assert content == "worldhiuniverse"

def test_error_non_existent_file():
    """Test error handling for non-existent file."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_error_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_error_empty_old_string(sample_file):
    """Test error handling for empty old string."""
    with pytest.raises(ValueError):
        replace_string_in_file(sample_file, "", "new")