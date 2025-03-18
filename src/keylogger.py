import logging
import os
from typing import Optional

class KeystrokeLogger:
    """
    A class to log keystrokes with configurable logging options.
    
    This logger provides a mechanism to record keystrokes with built-in 
    security and error handling features.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. 
                                      If None, uses a default log file.
        """
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Set default log file if not provided
        self.log_file = log_file or 'logs/keystrokes.log'
        
        # Configure logging
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
    def log_keystroke(self, key: str) -> None:
        """
        Log a single keystroke.
        
        Args:
            key (str): The keystroke to log
        
        Raises:
            ValueError: If the input is not a valid string
        """
        # Validate input
        if not isinstance(key, str):
            raise ValueError("Keystroke must be a string")
        
        # Sanitize input to prevent log injection
        sanitized_key = self._sanitize_input(key)
        
        # Log the keystroke
        logging.info(f"Keystroke: {sanitized_key}")
    
    def _sanitize_input(self, input_str: str) -> str:
        """
        Sanitize input to prevent log injection and ensure safe logging.
        
        Args:
            input_str (str): Input string to sanitize
        
        Returns:
            str: Sanitized input string
        """
        # Remove newlines and limit length
        return input_str.replace('\n', ' ')[:100]
    
    def clear_log(self) -> None:
        """
        Clear the current log file.
        """
        try:
            open(self.log_file, 'w').close()
            logging.info("Log file cleared")
        except IOError as e:
            logging.error(f"Failed to clear log file: {e}")