import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 5)
    assert result == datetime(2023, 5, 10)

def test_subtract_days_from_date_string():
    """Test subtracting days from a date string."""
    base_date = "2023-05-15"
    result = subtract_days_from_date(base_date, 5)
    assert result == datetime(2023, 5, 10)

def test_subtract_zero_days():
    """Test subtracting zero days."""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 0)
    assert result == base_date

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError, match="Input date must be a datetime object or ISO format string"):
        subtract_days_from_date(123, 5)

def test_invalid_date_string():
    """Test handling of invalid date string."""
    with pytest.raises(ValueError, match="Input date must be a valid datetime or ISO format string"):
        subtract_days_from_date("invalid-date", 5)

def test_negative_days_to_subtract():
    """Test handling of negative days to subtract."""
    with pytest.raises(ValueError, match="Days to subtract must be a non-negative integer"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_non_integer_days():
    """Test handling of non-integer days."""
    with pytest.raises(ValueError, match="Days to subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), 5.5)