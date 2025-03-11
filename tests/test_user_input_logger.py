import os
import logging
import pytest
import sys
from unittest.mock import patch
import src.user_input_logger as user_input_logger

def test_log_user_input_normal_case(tmp_path):
    """Test logging of normal user input."""
    log_file = str(tmp_path / "test_input.log")
    
    # Simulate user input
    with patch('builtins.input', return_value="Hello, World!"):
        result = user_input_logger.log_user_input(log_file)
    
    # Check return value
    assert result == "Hello, World!"
    
    # Verify log file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "User input: Hello, World!" in log_content

def test_log_user_input_empty_input(tmp_path):
    """Test handling of empty input."""
    log_file = str(tmp_path / "empty_input.log")
    
    # Simulate empty input
    with patch('builtins.input', return_value=""):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            user_input_logger.log_user_input(log_file)

def test_log_user_input_whitespace_input(tmp_path):
    """Test handling of whitespace-only input."""
    log_file = str(tmp_path / "whitespace_input.log")
    
    # Simulate whitespace input
    with patch('builtins.input', return_value="   "):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            user_input_logger.log_user_input(log_file)

def test_log_user_input_logging_level(tmp_path):
    """Test different logging levels."""
    log_file = str(tmp_path / "log_level_test.log")
    
    # Simulate user input with DEBUG level
    with patch('builtins.input', return_value="Debug message"):
        result = user_input_logger.log_user_input(log_file, logging.DEBUG)
    
    # Verify log file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "User input: Debug message" in log_content