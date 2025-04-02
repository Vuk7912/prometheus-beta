import os
import pytest
import lzma
import tempfile

from src.xz_compression import compress_xz, decompress_xz

class TestXZCompression:
    def test_compress_string(self):
        """Test compressing a string"""
        input_text = "Hello, world! This is a test of XZ compression."
        compressed = compress_xz(input_text)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0
        
    def test_compress_bytes(self):
        """Test compressing bytes"""
        input_bytes = b"Binary data compression test"
        compressed = compress_xz(input_bytes)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0
    
    def test_compress_to_file(self):
        """Test compressing to a file"""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            input_text = "Compress to file test"
            compress_xz(input_text, temp_file.name)
            
            # Verify file exists and is not empty
            assert os.path.exists(temp_file.name)
            assert os.path.getsize(temp_file.name) > 0
        
        # Clean up
        os.unlink(temp_file.name)
    
    def test_decompress_bytes(self):
        """Test decompressing bytes"""
        input_text = "Hello, world! Decompression test"
        compressed = compress_xz(input_text)
        decompressed = decompress_xz(compressed)
        assert decompressed == input_text
    
    def test_decompress_from_file(self):
        """Test decompressing from a file"""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            input_text = "Decompress from file test"
            compress_xz(input_text, temp_file.name)
            
            # Decompress from the file
            decompressed = decompress_xz(temp_file.name)
            assert decompressed == input_text
        
        # Clean up
        os.unlink(temp_file.name)
    
    def test_decompress_to_file(self):
        """Test decompressing to a file"""
        input_text = "Decompress to file test"
        
        with tempfile.NamedTemporaryFile(delete=False) as compressed_file, \
             tempfile.NamedTemporaryFile(delete=False) as decompressed_file:
            
            # Compress to first temp file
            compress_xz(input_text, compressed_file.name)
            
            # Decompress to second temp file
            decompress_xz(compressed_file.name, decompressed_file.name)
            
            # Read and verify decompressed file content
            with open(decompressed_file.name, 'r') as f:
                assert f.read() == input_text
        
        # Clean up
        os.unlink(compressed_file.name)
        os.unlink(decompressed_file.name)
    
    def test_error_empty_input(self):
        """Test handling of empty input"""
        with pytest.raises(ValueError, match="Input data cannot be empty"):
            compress_xz(b"")
        
        with pytest.raises(ValueError, match="Input data cannot be empty"):
            decompress_xz(b"")
    
    def test_error_invalid_input_type(self):
        """Test handling of invalid input types"""
        with pytest.raises(TypeError, match="Input must be str or bytes"):
            compress_xz(123)
        
        with pytest.raises(TypeError, match="Input must be bytes or a valid file path"):
            decompress_xz(123)
    
    def test_invalid_compressed_data(self):
        """Test decompression of invalid compressed data"""
        with pytest.raises(lzma.LZMAError):
            decompress_xz(b"Invalid compressed data")

    def test_large_data_compression(self):
        """Test compression of large data"""
        large_input = "X" * 1_000_000  # 1 million characters
        compressed = compress_xz(large_input)
        decompressed = decompress_xz(compressed)
        assert decompressed == large_input