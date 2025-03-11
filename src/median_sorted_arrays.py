def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays.
    
    This function efficiently finds the median when two input arrays are already sorted.
    It works with arrays of different lengths and handles various edge cases.
    
    Time Complexity: O(log(min(m,n)))
    Space Complexity: O(1)
    
    Args:
        nums1 (list[int]): First sorted input array
        nums2 (list[int]): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        ValueError: If both input arrays are empty
    """
    # Ensure nums1 is the smaller array for optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Handle empty array cases
    if len(nums1) == 0:
        if len(nums2) == 0:
            raise ValueError("Both input arrays cannot be empty")
        
        mid = len(nums2) // 2
        return (nums2[mid] + nums2[~mid]) / 2
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max/min values around the partition
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if partition is correct
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # Determine median based on total number of elements
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        
        # Adjust partition
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
    
    # If no valid partition is found (this should not happen with valid inputs)
    raise ValueError("Input arrays are not sorted or contain invalid data")