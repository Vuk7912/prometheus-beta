import os
from typing import List, Union


def merge_files(input_files: List[str], output_file: str, separator: str = '\n\n') -> None:
    """
    Merge multiple input files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output file where merged content will be written.
        separator (str, optional): Separator to use between merged file contents. 
                                   Defaults to double newline.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        ValueError: If input_files list is empty.
        IOError: If there are issues reading or writing files.
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided. At least one file is required.")

    # Check that all input files exist
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

    try:
        # Read contents of all input files
        file_contents = []
        for file_path in input_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_contents.append(f.read().strip())

        # Write merged contents to output file
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write(separator.join(file_contents))

    except IOError as e:
        raise IOError(f"Error merging files: {e}")