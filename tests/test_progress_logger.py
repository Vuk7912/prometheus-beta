import io
import sys
import pytest
from contextlib import redirect_stdout
from src.progress_logger import log_progress


def test_log_progress_basic_list():
    """Test basic functionality with a list."""
    items = list(range(10))
    captured_output = []
    
    with redirect_stdout(io.StringIO()) as f:
        result = list(log_progress(items))
        output = f.getvalue()
    
    # Verify the output contains progress information
    assert '|' in output
    assert '%' in output
    # Verify the function returns the original items
    assert result == items


def test_log_progress_custom_parameters():
    """Test log_progress with custom parameters."""
    items = list(range(5))
    
    with redirect_stdout(io.StringIO()) as f:
        result = list(log_progress(
            items, 
            prefix='Test:', 
            suffix='Done', 
            decimals=2, 
            length=30, 
            fill='#'
        ))
        output = f.getvalue()
    
    # Verify custom parameters are reflected in output
    assert 'Test:' in output
    assert 'Done' in output
    assert '#' in output
    assert len(output.split('|')[1].strip()) <= 30
    assert result == items


def test_log_progress_no_total():
    """Test log_progress with generator input."""
    def gen_items():
        for i in range(7):
            yield i
    
    with redirect_stdout(io.StringIO()) as f:
        result = list(log_progress(gen_items()))
        output = f.getvalue()
    
    # Verify progress is logged and all items are returned
    assert len(result) == 7
    assert '|' in output
    assert '%' in output


def test_log_progress_invalid_total():
    """Test log_progress with invalid total."""
    with pytest.raises(ValueError):
        list(log_progress(range(10), total=0))
    
    with pytest.raises(ValueError):
        list(log_progress(range(10), total=-5))


def test_log_progress_empty_iterable():
    """Test log_progress with empty iterable."""
    empty_list = []
    
    with redirect_stdout(io.StringIO()) as f:
        result = list(log_progress(empty_list))
        output = f.getvalue()
    
    # Verify no error and no output for empty iterable
    assert len(result) == 0
    assert len(output.strip()) == 0