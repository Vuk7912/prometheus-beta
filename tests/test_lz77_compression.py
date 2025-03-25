import pytest
from src.lz77_compression import LZ77Compressor

class TestLZ77Compression:
    def setup_method(self):
        """Set up a fresh LZ77Compressor for each test"""
        self.compressor = LZ77Compressor()
    
    def test_compress_empty_input(self):
        """Test compression of empty input"""
        assert self.compressor.compress('') == []
        assert self.compressor.compress(b'') == []
    
    def test_compress_single_char(self):
        """Test compression of a single character"""
        compressed = self.compressor.compress('a')
        assert len(compressed) == 1
        assert compressed[0] == (0, 0, ord('a'))
    
    def test_compress_no_repeat(self):
        """Test compression of input with no repeats"""
        compressed = self.compressor.compress('abcdef')
        assert len(compressed) == 6
        assert all(item[0] == 0 and item[1] == 0 for item in compressed)
    
    def test_compress_with_repeats(self):
        """Test compression of input with repeats"""
        input_str = 'abcabcabc'
        compressed = self.compressor.compress(input_str)
        assert len(compressed) < len(input_str)
        
        # Decompress and verify
        decompressed = self.compressor.decompress(compressed)
        assert decompressed.decode('utf-8') == input_str
    
    def test_decompress_empty_input(self):
        """Test decompression of empty input"""
        assert self.compressor.decompress([]) == b''
    
    def test_roundtrip_compression(self):
        """Test full roundtrip compression and decompression"""
        test_cases = [
            'hello world',
            'abcabcabc',
            'repeated repeated repeated',
            '12345' * 10,
            bytes([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
        ]
        
        for input_data in test_cases:
            # Handle both string and bytes input
            input_bytes = input_data.encode('utf-8') if isinstance(input_data, str) else input_data
            
            # Compress
            compressed = self.compressor.compress(input_data)
            
            # Decompress
            decompressed = self.compressor.decompress(compressed)
            
            # Verify
            assert decompressed == input_bytes, f"Failed for input: {input_data}"
    
    def test_large_input(self):
        """Test compression and decompression of a larger input"""
        large_input = 'test ' * 1000
        compressed = self.compressor.compress(large_input)
        
        # Should be compressed
        assert len(compressed) < len(large_input)
        
        # Decompress and verify
        decompressed = self.compressor.decompress(compressed)
        assert decompressed.decode('utf-8') == large_input
    
    def test_binary_data(self):
        """Test compression of binary data"""
        binary_data = bytes(range(256)) * 10
        compressed = self.compressor.compress(binary_data)
        
        # Decompress and verify
        decompressed = self.compressor.decompress(compressed)
        assert decompressed == binary_data