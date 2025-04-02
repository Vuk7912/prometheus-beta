def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays in nums where the product of elements is less than k.
    
    Args:
        nums (List[int]): Input array of positive integers
        k (int): Maximum product threshold
    
    Returns:
        int: Number of subarrays with product less than k
    
    Raises:
        ValueError: If k is less than 1
        TypeError: If nums is not a list or contains non-integer elements
    """
    # Input validation
    if k < 1:
        raise ValueError("k must be a positive integer")
    
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(num, int) and num > 0 for num in nums):
        raise TypeError("All elements must be positive integers")
    
    # Edge case: empty array
    if not nums:
        return 0
    
    # Sliding window approach
    count = 0
    left = 0
    curr_product = 1
    
    for right in range(len(nums)):
        # Expand window by multiplying current element
        curr_product *= nums[right]
        
        # Shrink window from left if product exceeds k
        while curr_product >= k and left <= right:
            curr_product //= nums[left]
            left += 1
        
        # Count subarrays
        count += right - left + 1
    
    return count