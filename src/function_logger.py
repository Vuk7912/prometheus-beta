import logging
import functools
import time
from typing import Callable, Any

# Configure basic logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_execution(logger: logging.Logger = None) -> Callable:
    """
    A decorator to log function execution start and end.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
                Defaults to the root logger if not provided.
    
    Returns:
        Callable: Decorated function with logging
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log function start
            logger.info(f"Starting execution of {func.__name__}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log successful completion
                logger.info(f"Finished execution of {func.__name__}. "
                            f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator