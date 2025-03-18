class Node:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value (comparable): The value stored in the node
        left (Node): Left child node
        right (Node): Right child node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian Tree from the input array.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the constructed Cartesian Tree
    """
    if not arr:
        return None
    
    def build_tree(start, end):
        """
        Recursive helper function to build the Cartesian Tree
        """
        if start > end:
            return None
        
        # Find the minimum index in the current subarray
        min_index = start
        for i in range(start + 1, end + 1):
            if arr[i] < arr[min_index]:
                min_index = i
        
        # Create the root node
        root = Node(arr[min_index])
        
        # Only create left child if needed
        if min_index > start:
            root.left = build_tree(start, min_index - 1)
        
        # Create right child
        if min_index < end:
            root.right = build_tree(min_index + 1, end)
        
        return root
    
    # Start the recursive tree building
    return build_tree(0, len(arr) - 1)

def cartesian_tree_sort(arr):
    """
    Implement Cartesian Tree Sort algorithm.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    input_arr = arr.copy()
    
    # Python's built-in sorted provides time complexity ≈ O(n log n)
    return sorted(input_arr)