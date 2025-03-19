import os
import pytest
from src.pair_sum_diff_nine import sum_pairs_with_diff_nine

def test_basic_functionality(tmp_path):
    # Create a temporary file with numbers
    test_file = tmp_path / "numbers.txt"
    test_file.write_text("1\n10\n5\n14\n20\n29\n")
    
    # Expected: 1+10, 5+14, 20+29 have differences of 9
    result = sum_pairs_with_diff_nine(str(test_file))
    assert result == (1+10) + (5+14) + (20+29), "Failed to sum pairs with difference of 9"

def test_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    result = sum_pairs_with_diff_nine(str(test_file))
    assert result == 0, "Should return 0 for empty file"

def test_no_pairs(tmp_path):
    # Create a file with no pairs having difference of 9
    test_file = tmp_path / "no_pairs.txt"
    test_file.write_text("1\n2\n3\n4\n5\n")
    
    result = sum_pairs_with_diff_nine(str(test_file))
    assert result == 0, "Should return 0 when no pairs have difference of 9"

def test_duplicate_numbers(tmp_path):
    # Test with duplicate numbers that can form pairs
    test_file = tmp_path / "duplicates.txt"
    test_file.write_text("1\n10\n1\n10\n5\n14\n")
    
    result = sum_pairs_with_diff_nine(str(test_file))
    assert result == 2 * ((1+10) + (5+14)), "Failed to handle duplicate numbers"

def test_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_diff_nine("non_existent_file.txt")

def test_invalid_content(tmp_path):
    # Test non-numeric content
    test_file = tmp_path / "invalid.txt"
    test_file.write_text("1\n2\nabc\n4\n")
    
    with pytest.raises(ValueError):
        sum_pairs_with_diff_nine(str(test_file))