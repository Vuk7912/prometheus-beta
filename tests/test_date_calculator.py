import pytest
from src.date_calculator import calculate_days_between_dates

def test_same_date():
    assert calculate_days_between_dates("2023-01-01", "2023-01-01") == 1

def test_consecutive_dates():
    assert calculate_days_between_dates("2023-01-01", "2023-01-02") == 2

def test_different_months():
    assert calculate_days_between_dates("2023-01-31", "2023-02-02") == 3

def test_different_years():
    assert calculate_days_between_dates("2022-12-30", "2023-01-02") == 4

def test_invalid_date_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("2023/01/01", "2023-01-02")

def test_invalid_date():
    with pytest.raises(ValueError):
        calculate_days_between_dates("2023-02-30", "2023-03-01")

def test_end_date_before_start_date():
    assert calculate_days_between_dates("2023-02-02", "2023-01-31") == 0