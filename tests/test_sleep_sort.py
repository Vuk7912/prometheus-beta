import pytest
import time
import threading
from src.sleep_sort import sleep_sort

def test_basic_sorting():
    """Test basic sorting of a small list of positive integers."""
    input_list = [5, 2, 8, 1, 9]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sorting_with_floats():
    """Test sorting with floating point numbers."""
    input_list = [5.5, 2.2, 8.8, 1.1, 9.9]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_empty_list():
    """Test handling of an empty list."""
    assert sleep_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    input_list = [42]
    result = sleep_sort(input_list)
    assert result == input_list

def test_negative_numbers_raise_error():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Sleep sort does not support negative numbers"):
        sleep_sort([-1, 2, 3])

def test_non_numeric_input_raises_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must contain only numeric values"):
        sleep_sort([1, 2, 'a'])

def test_performance_with_large_list():
    """Test sorting performance and correctness with a larger list."""
    input_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    start_time = time.time()
    result = sleep_sort(input_list)
    end_time = time.time()
    
    # Verify sorting
    assert result == sorted(input_list)
    
    # Performance check - sorting should take less than 1 second
    assert end_time - start_time < 1.0