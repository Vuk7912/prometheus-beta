from typing import List, Optional
from collections import deque

class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (int): The value stored in the node
        left (Optional[TreeNode]): Left child node
        right (Optional[TreeNode]): Right child node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a zigzag level order traversal of a binary tree.
    
    In a zigzag level order traversal, nodes are traversed 
    level by level, alternating between left-to-right and 
    right-to-left directions.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree
    
    Returns:
        List[List[int]]: A list of levels, where each level 
        contains node values in zigzag order
    
    Examples:
        # Tree:    3
        #        /   \
        #       9    20
        #           /  \
        #          15   7
        # Result: [[3], [20,9], [15,7]]
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Use a queue for level-order traversal
    queue = deque([root])
    
    # Result list to store levels
    result = []
    
    # Flag to track traversal direction
    left_to_right = True
    
    while queue:
        # Number of nodes at current level
        level_size = len(queue)
        
        # List to store current level's nodes
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            # Pop the front node from queue
            node = queue.popleft()
            
            # Add node's value to current level
            current_level.append(node.val)
            
            # Add child nodes to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse level if needed for zigzag pattern
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        
        # Flip direction for next level
        left_to_right = not left_to_right
    
    return result