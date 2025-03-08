import pytest
from src.word_char_reverser import reverse_words_and_chars

def test_reverse_words_and_chars():
    # Test basic functionality
    assert reverse_words_and_chars("Hello World") == "dlroW olleH"
    assert reverse_words_and_chars("Python is awesome") == "emosewa si nohtyP"
    
    # Test empty string
    assert reverse_words_and_chars("") == ""
    
    # Test single word
    assert reverse_words_and_chars("Python") == "nohtyP"
    
    # Test multiple words with different lengths
    assert reverse_words_and_chars("a b c") == "c b a"
    
    # Test with punctuation
    assert reverse_words_and_chars("Hello, World!") == "!dlroW ,olleH"
    
    # Test with mixed case
    assert reverse_words_and_chars("OpenAI ChatGPT") == "TPGtahC IAnepO"
    
    # Test with extra whitespace
    assert reverse_words_and_chars("  Python  is  great  ") == "taerg si nohtyP"