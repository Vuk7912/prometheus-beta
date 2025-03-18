class Node:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value (int): The value stored in the node
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
    
    A Cartesian Tree is a binary tree where:
    1. The tree is heap-ordered (parent is smaller than children)
    2. An in-order traversal yields the original array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the constructed Cartesian Tree
    """
    if not arr:
        return None
    
    # Handle empty or single-element arrays
    if len(arr) == 1:
        return Node(arr[0])
    
    # Find the index of the minimum element
    min_index = arr.index(min(arr))
    
    # Create root node with the minimum element
    root = Node(arr[min_index])
    
    # Recursively build left and right subtrees
    if min_index > 0:
        root.left = build_cartesian_tree(arr[:min_index])
    
    if min_index < len(arr) - 1:
        root.right = build_cartesian_tree(arr[min_index+1:])
    
    return root

def cartesian_tree_sort(arr):
    """
    Implement Cartesian Tree Sort algorithm.
    
    This sorting algorithm works by:
    1. Building a Cartesian Tree from the input array
    2. Performing an in-order traversal to get the sorted array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains elements that cannot be compared
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    input_arr = arr.copy()
    
    # Build Cartesian Tree
    root = build_cartesian_tree(input_arr)
    
    # Sorted output list
    sorted_arr = []
    
    def in_order_traversal(node):
        """
        Perform in-order traversal to extract sorted elements.
        
        Args:
            node (Node): Current node in the Cartesian Tree
        """
        if node is None:
            return
        
        in_order_traversal(node.left)
        sorted_arr.append(node.value)
        in_order_traversal(node.right)
    
    # Traverse and sort
    in_order_traversal(root)
    
    return sorted_arr