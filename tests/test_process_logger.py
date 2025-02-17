import pytest
import time
import sys
from io import StringIO
from src.process_logger import ProcessLogger

def test_process_logger_initialization():
    """Test ProcessLogger initialization with default parameters."""
    logger = ProcessLogger(total_steps=100)
    assert logger.total_steps == 100
    assert logger.prefix == 'Progress'
    assert logger.suffix == 'Complete'

def test_process_logger_log_without_total():
    """Test logging without specifying total steps."""
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    logger = ProcessLogger()
    logger.log(10)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert 'Progress: 10 Complete' in output

def test_process_logger_log_with_total():
    """Test logging with total steps."""
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    logger = ProcessLogger(total_steps=50)
    logger.log(25)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert '50%' in output

def test_process_logger_decorator():
    """Test the tracking decorator."""
    @ProcessLogger(total_steps=5).track
    def sample_task():
        for i in range(5):
            time.sleep(0.01)
            yield i
    
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Execute the task
    list(sample_task())
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert '100%' in output

def test_process_logger_decorator_error():
    """Test decorator raises error when total steps not set."""
    @ProcessLogger().track
    def sample_task():
        for i in range(5):
            yield i
    
    with pytest.raises(ValueError, match="Total steps must be set"):
        list(sample_task())

def test_process_logger_custom_params():
    """Test ProcessLogger with custom parameters."""
    logger = ProcessLogger(
        total_steps=100, 
        prefix='Custom', 
        suffix='Done', 
        decimals=2, 
        length=25, 
        fill='#'
    )
    
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output

    logger.log(50)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert 'Custom' in output
    assert 'Done' in output
    assert '50.00%' in output