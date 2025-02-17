import time
import sys
from typing import Callable, Any, Optional

class ProcessLogger:
    """
    A utility class to log real-time progress of a process.
    
    This class provides methods to track and display the progress of a long-running task,
    with customizable update intervals and formatting.
    """
    
    def __init__(self, total_steps: Optional[int] = None, prefix: str = 'Progress', 
                 suffix: str = 'Complete', decimals: int = 1, length: int = 50, 
                 fill: str = '█', print_end: str = "\r"):
        """
        Initialize the ProcessLogger.
        
        :param total_steps: Total number of steps in the process (optional)
        :param prefix: Prefix text for the progress bar
        :param suffix: Suffix text for the progress bar
        :param decimals: Number of decimal places for percentage
        :param length: Character length of the progress bar
        :param fill: Character used to fill the progress bar
        :param print_end: End character for print (default allows overwriting)
        """
        self.total_steps = total_steps
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.start_time = time.time()
    
    def print_progress_bar(self, iteration: int, total: Optional[int] = None):
        """
        Print progress bar with percentage and timing information.
        
        :param iteration: Current iteration
        :param total: Total number of iterations (optional)
        """
        total = total or self.total_steps
        
        if total is None:
            # If no total is provided, just print iteration count
            print(f"{self.prefix}: {iteration} {self.suffix}", end=self.print_end)
            return
        
        # Calculate percentage and progress bar
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(self.length * iteration // total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # Calculate estimated time
        elapsed_time = time.time() - self.start_time
        est_total_time = elapsed_time * (total / iteration) if iteration > 0 else 0
        est_remaining_time = est_total_time - elapsed_time
        
        # Construct and print the progress output
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix}'
        output += f' (Elapsed: {elapsed_time:.2f}s, Remaining: {est_remaining_time:.2f}s)'
        
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Print newline if process is complete
        if iteration == total:
            print()
    
    def log(self, current_step: int, total_steps: Optional[int] = None):
        """
        Log the current progress.
        
        :param current_step: Current step in the process
        :param total_steps: Total steps (overrides initialization value if provided)
        """
        self.print_progress_bar(current_step, total_steps)
    
    def track(self, func: Callable) -> Callable:
        """
        Decorator to automatically track progress of a function.
        
        :param func: Function to track
        :return: Wrapped function with progress tracking
        """
        def wrapper(*args, **kwargs):
            if self.total_steps is None:
                raise ValueError("Total steps must be set to use the track decorator")
            
            result = func(*args, **kwargs)
            
            # If the function returns an iterable, track its progress
            if hasattr(result, '__iter__'):
                for i, item in enumerate(result, 1):
                    self.log(i)
                    yield item
            else:
                self.log(self.total_steps)
                return result
        
        return wrapper

# Example usage
def example_process():
    """
    Example function demonstrating ProcessLogger usage.
    """
    # Without known total steps
    simple_logger = ProcessLogger(prefix='Simple Process')
    for i in range(100):
        time.sleep(0.05)  # Simulate work
        simple_logger.log(i+1)
    
    # With decorator and known total steps
    @ProcessLogger(total_steps=50, prefix='Decorator Process').track
    def sample_task():
        for _ in range(50):
            time.sleep(0.1)  # Simulate work
            yield _
    
    list(sample_task())  # Execute the task