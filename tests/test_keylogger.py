import os
import pytest
import logging
from src.keylogger import KeystrokeLogger

def test_keystroke_logger_initialization():
    """Test that the KeystrokeLogger can be initialized."""
    logger = KeystrokeLogger()
    assert os.path.exists('logs')
    assert os.path.exists(logger.log_file)

def test_log_single_keystroke(caplog):
    """Test logging a single keystroke."""
    logger = KeystrokeLogger()
    caplog.set_level(logging.INFO)
    
    logger.log_keystroke('a')
    
    assert len(caplog.records) > 0
    assert 'Keystroke: a' in caplog.text

def test_log_special_characters(caplog):
    """Test logging keystrokes with special characters."""
    logger = KeystrokeLogger()
    caplog.set_level(logging.INFO)
    
    logger.log_keystroke('!@#$%^&*()_+')
    
    assert len(caplog.records) > 0
    assert 'Keystroke: !@#$%^&*()_+' in caplog.text

def test_invalid_keystroke_input():
    """Test that invalid input raises a ValueError."""
    logger = KeystrokeLogger()
    
    with pytest.raises(ValueError, match="Keystroke must be a string"):
        logger.log_keystroke(123)

def test_log_file_clearing(caplog):
    """Test clearing the log file."""
    logger = KeystrokeLogger()
    caplog.set_level(logging.INFO)
    
    # Log some keystrokes
    logger.log_keystroke('a')
    logger.log_keystroke('b')
    
    # Clear the log
    logger.clear_log()
    
    # Check if log was cleared
    with open(logger.log_file, 'r') as f:
        content = f.read()
        assert 'Log file cleared' in content

def test_custom_log_file():
    """Test creating a logger with a custom log file."""
    custom_log_file = 'logs/custom_keystrokes.log'
    logger = KeystrokeLogger(log_file=custom_log_file)
    
    assert logger.log_file == custom_log_file
    assert os.path.exists(custom_log_file)

def test_long_input_truncation(caplog):
    """Test that very long inputs are truncated."""
    logger = KeystrokeLogger()
    caplog.set_level(logging.INFO)
    
    long_input = 'a' * 200  # Create a very long input
    
    logger.log_keystroke(long_input)
    
    assert len(caplog.records) > 0
    assert len(caplog.text.split('Keystroke: ')[1].strip()) <= 100