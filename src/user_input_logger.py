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
    # Get the parent directory
    log_dir = os.path.dirname(os.path.abspath(log_file))
    os.makedirs(log_dir, exist_ok=True)

    # Create a logger
    logger = logging.getLogger('user_input_logger')
    logger.setLevel(log_level)

    # Create file handler
    try:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(file_handler)

        # Read input from command line
        user_input = input("Enter your input: ").strip()

        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")

        # Log the input
        logger.info(f"User input: {user_input}")

        # Remove handler to prevent duplicate logs
        logger.removeHandler(file_handler)
        file_handler.close()

        return user_input

    except Exception as e:
        # Log any errors that occur
        logging.error(f"Error logging user input: {str(e)}")
        raise