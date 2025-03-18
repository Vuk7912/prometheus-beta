import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort is a quirky sorting algorithm that uses threading and sleep times 
    to sort numbers. Each number creates a separate thread that sleeps proportionally 
    to its value before adding it to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of input numbers
    
    Raises:
        ValueError: If input contains negative numbers
        TypeError: If input contains non-numeric types
    """
    # Validate input
    if not arr:
        return []
    
    # Explicitly check for non-numeric types before other checks
    if not all(isinstance(num, (int, float)) for num in arr):
        raise TypeError("Input must contain only numeric values")
    
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort does not support negative numbers")
    
    # Thread-safe list to store sorted results
    result = []
    lock = threading.Lock()
    
    def sort_worker(num):
        """Worker function for each number in the input list."""
        # Sleep proportional to the number's value
        time.sleep(num * 0.001)  # Scaled sleep time to make sorting more predictable
        
        # Thread-safe append to result list
        with lock:
            result.append(num)
    
    # Create and start threads for each number
    threads = [threading.Thread(target=sort_worker, args=(num,)) for num in arr]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result