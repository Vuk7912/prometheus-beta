import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of freezing point of water."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of boiling point of water."""
    assert fahrenheit_to_celsius(212) == 100

def test_zero_fahrenheit():
    """Test conversion of zero Fahrenheit."""
    assert fahrenheit_to_celsius(0) == -17.78

def test_negative_temperature():
    """Test conversion of a negative temperature."""
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_temperature():
    """Test conversion of a decimal temperature."""
    assert fahrenheit_to_celsius(98.6) == 37

def test_large_number():
    """Test conversion of a large temperature."""
    assert fahrenheit_to_celsius(1000) == 537.78

def test_invalid_input():
    """Test that TypeError is raised for non-numeric input."""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")

def test_invalid_input_list():
    """Test that TypeError is raised for list input."""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius([32])