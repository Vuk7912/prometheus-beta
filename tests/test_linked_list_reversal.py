import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create linked list from.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a regular list for easy assertion.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Values of the linked list in order.
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    single_node = ListNode(5)
    reversed_list = reverse_linked_list(single_node)
    assert linked_list_to_list(reversed_list) == [5]

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    # Original list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = create_linked_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(original_list)
    
    # Expected reversed list: 5 -> 4 -> 3 -> 2 -> 1
    assert linked_list_to_list(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    original_list = create_linked_list([1, 2])
    reversed_list = reverse_linked_list(original_list)
    assert linked_list_to_list(reversed_list) == [2, 1]

def test_invalid_input_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a ListNode or None"):
        reverse_linked_list([1, 2, 3])  # List instead of ListNode
    
    with pytest.raises(TypeError, match="Input must be a ListNode or None"):
        reverse_linked_list("not a list")  # String input
    
    with pytest.raises(TypeError, match="Input must be a ListNode or None"):
        reverse_linked_list(42)  # Integer input