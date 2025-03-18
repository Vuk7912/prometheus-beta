import os
import pytest
import bz2
import tempfile
import shutil

from src.file_compressor import compress_file

def test_compress_file_default_output():
    """Test compression with default output path"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test compression content')

        # Compress the file
        compressed_path = compress_file(test_file_path)

        # Verify compressed file exists with .bz2 extension
        assert os.path.exists(compressed_path)
        assert compressed_path == test_file_path + '.bz2'

        # Verify content can be decompressed
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test compression content'

def test_compress_file_custom_output():
    """Test compression with custom output path"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        custom_output = os.path.join(tmpdir, 'custom_compressed.bz2')
        with open(test_file_path, 'w') as f:
            f.write('Test compression content')

        # Compress the file
        compressed_path = compress_file(test_file_path, custom_output)

        # Verify compressed file exists at custom path
        assert os.path.exists(compressed_path)
        assert compressed_path == custom_output

        # Verify content can be decompressed
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test compression content'

def test_compress_nonexistent_file():
    """Test compression of a nonexistent file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file(nonexistent_path)

def test_compress_directory():
    """Test compression of a directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(IsADirectoryError):
            compress_file(tmpdir)

def test_large_file_compression():
    """Test compression of a larger file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a larger test file
        test_file_path = os.path.join(tmpdir, 'large_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test ' * 10000)  # Create a file with repeated content

        # Compress the file
        compressed_path = compress_file(test_file_path)

        # Verify compressed file exists
        assert os.path.exists(compressed_path)

        # Verify content can be decompressed
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test ' * 10000

def test_binary_file_compression():
    """Test compression of a binary file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a binary test file
        test_file_path = os.path.join(tmpdir, 'binary_file.bin')
        with open(test_file_path, 'wb') as f:
            f.write(b'\x00\x01\x02\x03' * 1000)

        # Compress the file
        compressed_path = compress_file(test_file_path)

        # Verify compressed file exists
        assert os.path.exists(compressed_path)

        # Verify content can be decompressed
        with bz2.open(compressed_path, 'rb') as f:
            assert f.read() == b'\x00\x01\x02\x03' * 1000