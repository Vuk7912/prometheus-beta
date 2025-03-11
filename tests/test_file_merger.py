import os
import pytest
import tempfile
import shutil


def test_merge_files_basic():
    from src.file_merger import merge_files

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Create test input files
        input_files = [
            os.path.join(temp_dir, 'file1.txt'),
            os.path.join(temp_dir, 'file2.txt')
        ]
        output_file = os.path.join(temp_dir, 'merged.txt')

        # Write content to input files
        with open(input_files[0], 'w') as f1:
            f1.write("Hello")
        with open(input_files[1], 'w') as f2:
            f2.write("World")

        # Merge files
        merge_files(input_files, output_file)

        # Verify merged content
        with open(output_file, 'r') as merged:
            content = merged.read()
            assert content == "Hello\n\nWorld"

    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)


def test_merge_files_empty_list():
    from src.file_merger import merge_files

    # Test empty input files list
    with pytest.raises(ValueError, match="No input files provided"):
        merge_files([], 'output.txt')


def test_merge_files_nonexistent_input():
    from src.file_merger import merge_files

    # Test nonexistent input file
    with pytest.raises(FileNotFoundError, match="Input file not found"):
        merge_files(['nonexistent_file.txt'], 'output.txt')


def test_merge_files_custom_separator():
    from src.file_merger import merge_files

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Create test input files
        input_files = [
            os.path.join(temp_dir, 'file1.txt'),
            os.path.join(temp_dir, 'file2.txt')
        ]
        output_file = os.path.join(temp_dir, 'merged.txt')

        # Write content to input files
        with open(input_files[0], 'w') as f1:
            f1.write("Hello")
        with open(input_files[1], 'w') as f2:
            f2.write("World")

        # Merge files with custom separator
        merge_files(input_files, output_file, separator=' --- ')

        # Verify merged content
        with open(output_file, 'r') as merged:
            content = merged.read()
            assert content == "Hello --- World"

    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)