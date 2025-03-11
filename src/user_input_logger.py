import logging
import sys
import os

def log_user_input(log_file='user_input.log', log_level=logging.INFO):
    """
    Log user input from the command line to a specified log file.

    Args:
        log_file (str, optional): Path to the log file. Defaults to 'user_input.log'.
        log_level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        str: The input string that was logged.

    Raises:
        ValueError: If input is empty or None.
        IOError: If there's an issue with file logging.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)

    # Explicitly create the log file if it doesn't exist
    open(log_file, 'a').close()

    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=log_level, 
        format='%(asctime)s - %(levelname)s: %(message)s'
    )

    try:
        # Read input from command line
        user_input = input("Enter your input: ").strip()

        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")

        # Log the input
        logging.info(f"User input: {user_input}")

        return user_input

    except Exception as e:
        # Log any errors that occur
        logging.error(f"Error logging user input: {str(e)}")
        raise