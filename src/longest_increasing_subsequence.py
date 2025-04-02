def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        tuple: A tuple containing:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence itself (list)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        (6, [10, 22, 33, 50, 60, 80])
        >>> find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
        (6, [0, 2, 6, 9, 13, 15])
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming approach
    # lengths[i] stores the length of the LIS ending at index i
    lengths = [1] * n
    
    # predecessors tracks the previous index in the LIS
    predecessors = [-1] * n
    
    # Track the maximum length and its ending index
    max_length = 1
    max_index = 0
    
    # Compute LIS
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
        
        # Update max length
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = predecessors[current]
    
    return max_length, subsequence