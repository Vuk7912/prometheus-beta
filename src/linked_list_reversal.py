class ListNode:
    """
    Represents a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode): Reference to the next node in the list.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.
        
        Args:
            val (Any, optional): Value to be stored in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list by changing the direction of node pointers.
    
    Args:
        head (ListNode): The head of the original linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    
    Raises:
        TypeError: If the input is not a ListNode or None
    """
    # Handle edge cases
    if head is None:
        return None
    
    # Validate input type
    if not isinstance(head, ListNode):
        raise TypeError("Input must be a ListNode or None")
    
    # If list has only one node, return it as is
    if head.next is None:
        return head
    
    # Initialize pointers for reversal
    prev = None
    current = head
    
    # Traverse and reverse links
    while current is not None:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return new head (last node of original list)
    return prev