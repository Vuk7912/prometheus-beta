class Node:
    """
    Binary tree node class for tree sort implementation.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, value):
        """
        Initialize a new Node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement tree sort algorithm.
    
    Tree sort works by:
    1. Creating a binary search tree from the input array
    2. Performing an in-order traversal to get sorted elements
    
    Args:
        arr (list): Input list to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Create root of the binary search tree
    try:
        root = None
        for item in arr:
            root = insert_node(root, item)
        
        # Collect sorted elements
        sorted_list = []
        in_order_traversal(root, sorted_list)
        return sorted_list
    
    except TypeError:
        raise ValueError("List contains elements that cannot be compared")

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    Args:
        root (Node): Root of the current subtree
        value: Value to be inserted
    
    Returns:
        Node: Updated root of the subtree
    """
    # If tree is empty, create new root
    if root is None:
        return Node(value)
    
    # Recursively insert based on BST property
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    
    return root

def in_order_traversal(node, result):
    """
    Perform in-order traversal to collect sorted elements.
    
    Args:
        node (Node): Current node in traversal
        result (list): List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Collect current node's value
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)