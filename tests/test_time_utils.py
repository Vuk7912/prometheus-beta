import pytest
from datetime import datetime
from src.time_utils import get_current_time

def test_get_current_time_format():
    """
    Test that the function returns a time string in the correct HH:MM:SS format.
    """
    time_str = get_current_time()
    
    # Check string length (HH:MM:SS is 8 characters)
    assert len(time_str) == 8
    
    # Check format matches HH:MM:SS
    assert time_str[2] == ':' and time_str[5] == ':'
    
    # Validate hour, minute, second parts
    hour, minute, second = time_str.split(':')
    
    # Check hour is between 00-23
    assert 0 <= int(hour) <= 23
    
    # Check minute is between 00-59
    assert 0 <= int(minute) <= 59
    
    # Check second is between 00-59
    assert 0 <= int(second) <= 59

def test_get_current_time_close_to_actual_time():
    """
    Test that the returned time is very close to the actual current time.
    """
    func_time_str = get_current_time()
    actual_time_str = datetime.now().strftime("%H:%M:%S")
    
    # The times should be either exactly the same or differ by a second
    assert func_time_str == actual_time_str or \
           func_time_str == (datetime.now() - timedelta(seconds=1)).strftime("%H:%M:%S") or \
           func_time_str == (datetime.now() + timedelta(seconds=1)).strftime("%H:%M:%S")