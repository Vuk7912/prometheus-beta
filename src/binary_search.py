def binary_search(arr, target):
    """
    Perform an efficient binary search to find the index of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements in ascending order.
        target: The element to search for in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Handle empty array case
    if not arr:
        return -1
    
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1
    
    # Continue search while left pointer is less than or equal to right pointer
    while left <= right:
        # Calculate mid point to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if mid element is the target
        if arr[mid] == target:
            return mid
        
        # If target is less than mid element, search left half
        elif target < arr[mid]:
            right = mid - 1
        
        # If target is greater than mid element, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1