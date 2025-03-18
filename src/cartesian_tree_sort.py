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
    
    A Cartesian Tree is a binary tree where:
    1. The tree satisfies heap property (parent has the smallest value)
    2. In-order traversal gives the original array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the constructed Cartesian Tree
    """
    if not arr:
        return None
    
    # Handle simple cases
    if len(arr) == 1:
        return Node(arr[0])
    
    # Find the minimum element and its index
    min_value = min(arr)
    min_index = arr.index(min_value)
    
    # Create root with the minimum element
    root = Node(min_value)
    
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
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    input_arr = arr.copy()
    
    # Perform sorting
    sorted_arr = []
    
    def recursive_sort(sublist):
        """
        Recursively sort sublists using Cartesian Tree
        
        Args:
            sublist (list): Sublist to be sorted
        """
        if len(sublist) <= 1:
            return sublist
        
        # Build Cartesian Tree and traverse
        root = build_cartesian_tree(sublist)
        
        def in_order_traversal(node):
            if node is None:
                return
            
            in_order_traversal(node.left)
            sorted_arr.append(node.value)
            in_order_traversal(node.right)
        
        in_order_traversal(root)
    
    # Sort the entire input array
    recursive_sort(input_arr)
    
    return sorted_arr