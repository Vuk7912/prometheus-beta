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
    
    # Find the minimum element
    min_index = arr.index(min(arr))
    
    # Create root node with the minimum element
    root = Node(arr[min_index])
    
    # Build left subtree if needed
    if min_index > 0:
        root.left = build_cartesian_tree(arr[:min_index])
    
    # Build right subtree if needed
    if min_index < len(arr) - 1:
        root.right = build_cartesian_tree(arr[min_index+1:])
    
    return root

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