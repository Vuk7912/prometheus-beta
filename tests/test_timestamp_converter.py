import pytest
from datetime import datetime, timezone
import sys
import os
import re

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a standard timestamp"""
    # January 1, 2000, 00:00:00 UTC
    timestamp = 946684800
    assert timestamp_to_human_readable(timestamp) == '2000-01-01 00:00:00 UTC'

def test_float_timestamp():
    """Test conversion of a float timestamp"""
    # January 1, 2000, 00:00:00 UTC
    timestamp = 946684800.123
    assert timestamp_to_human_readable(timestamp) == '2000-01-01 00:00:00 UTC'

def test_recent_timestamp():
    """Test conversion of a recent timestamp"""
    # Use current time as a reference point
    current_time = datetime.now(timezone.utc).timestamp()
    result = timestamp_to_human_readable(current_time)
    
    # Use regex to validate the format instead of exact length
    assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$', result)

def test_invalid_type_raises_error():
    """Test that non-numeric input raises TypeError"""
    with pytest.raises(TypeError, match="Timestamp must be a number"):
        timestamp_to_human_readable("not a number")
    
    with pytest.raises(TypeError, match="Timestamp must be a number"):
        timestamp_to_human_readable([12345])

def test_negative_timestamp_raises_error():
    """Test that negative timestamp raises ValueError"""
    with pytest.raises(ValueError, match="Timestamp cannot be negative"):
        timestamp_to_human_readable(-1)

def test_extreme_large_timestamp():
    """Test extremely large timestamp handling"""
    # Use a timestamp far in the future
    with pytest.raises(ValueError, match="Timestamp is out of valid range"):
        timestamp_to_human_readable(2**63)  # Extremely large number