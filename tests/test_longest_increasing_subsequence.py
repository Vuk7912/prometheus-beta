import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    assert subsequence == [10, 22, 33, 50, 60, 80]

def test_complex_sequence():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 6
    assert subsequence == [0, 4, 6, 9, 13, 15]

def test_already_sorted_sequence():
    arr = [1, 2, 3, 4, 5]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_reverse_sorted_sequence():
    arr = [5, 4, 3, 2, 1]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [1]

def test_single_element_sequence():
    arr = [42]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 1
    assert subsequence == [42]

def test_duplicate_element_sequence():
    arr = [1, 2, 2, 3, 3, 4]
    length, subsequence = find_longest_increasing_subsequence(arr)
    assert length == 4
    assert subsequence == [1, 2, 3, 4]

def test_invalid_input_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_increasing_subsequence([])

def test_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_longest_increasing_subsequence("not a list")
        find_longest_increasing_subsequence(123)
        find_longest_increasing_subsequence(None)