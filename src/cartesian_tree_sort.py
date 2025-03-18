class Node:
    """
    Node class for Cartesian Tree representation.
    
    Attributes:
        value (int or float): The value stored in the node
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
    
    # Create a stack to help build the tree
    stack = []
    
    for value in arr:
        # Remove nodes from stack that are larger than current value
        while stack and stack[-1].value > value:
            last = stack.pop()
        
        # Create current node
        node = Node(value)
        
        # If stack is not empty, connect current node
        if stack:
            stack[-1].right = node
        
        # Add current node to stack
        stack.append(node)
    
    # Return the root (first node in stack)
    return stack[0]

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