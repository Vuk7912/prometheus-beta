import pytest
from src.count_a_occurrences import count_a_occurrences

def test_count_a_occurrences():
    # Test various scenarios
    assert count_a_occurrences("Apple") == 1
    assert count_a_occurrences("banana") == 3
    assert count_a_occurrences("JAVA") == 2  # Corrected expectation
    assert count_a_occurrences("a") == 1
    assert count_a_occurrences("A") == 1
    assert count_a_occurrences("") == 0
    assert count_a_occurrences("Hello World") == 0
    assert count_a_occurrences("AaAaA") == 5

def test_input_types():
    # Test different input types
    with pytest.raises(AttributeError):
        count_a_occurrences(123)
    with pytest.raises(AttributeError):
        count_a_occurrences(None)