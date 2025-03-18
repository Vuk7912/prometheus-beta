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
    
    # Use explicit creation approach
    nodes = [Node(x) for x in arr]
    
    # First node is always the root
    root = nodes[0]
    
    # Track the last node processed
    last = root
    
    # Build tree level by level
    for node in nodes[1:]:
        # If current node is less than previous, make it the right child
        while last.value > node.value:
            # If no left child exists, make node the left child
            if not last.left:
                last.left = node
                break
            # Otherwise, go up the tree
            last = last.parent if hasattr(last, 'parent') else last
        
        # Connect node to its parent
        node.parent = last
        
        # Update last processed node
        last = node
    
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