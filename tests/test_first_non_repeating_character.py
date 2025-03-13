import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test basic scenarios
    assert first_non_repeating_character("leetcode") == "l"
    assert first_non_repeating_character("loveleetcode") == "v"
    assert first_non_repeating_character("aabb") is None
    
    # Test single character cases
    assert first_non_repeating_character("a") == "a"
    assert first_non_repeating_character("z") == "z"
    
    # Test empty string
    assert first_non_repeating_character("") is None
    
    # Test all repeated characters
    assert first_non_repeating_character("aaaaaa") is None
    
    # Test error handling
    with pytest.raises(ValueError, match="Input string must contain only lowercase letters"):
        first_non_repeating_character("ABC")
    
    with pytest.raises(ValueError, match="Input string must contain only lowercase letters"):
        first_non_repeating_character("hello123")
    
    # Test more complex scenarios
    assert first_non_repeating_character("abcdefghijklmnopqrstuvwxyz") == "a"
    assert first_non_repeating_character("abcabcabc") is None
    assert first_non_repeating_character("abcdedcba") == "c"