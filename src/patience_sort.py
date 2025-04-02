from typing import List, TypeVar, Protocol
import heapq

class Comparable(Protocol):
    """Protocol for objects that can be compared"""
    def __lt__(self: 'T', other: 'T') -> bool: ...

T = TypeVar('T', bound=Comparable)

def patience_sort(arr: List[T]) -> List[T]:
    """
    Implement the Patience Sorting algorithm.
    
    Patience sorting creates sorted subsequences (piles) by 
    finding the most appropriate pile for each element,
    then merges these piles.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A new sorted list
    
    Raises:
        TypeError: If the input is not a list or contains incomparable elements
    """
    # Handle edge cases
    if arr is None:
        raise TypeError("Input cannot be None")
    
    if not arr:
        return []
    
    # Ensure all elements are comparable
    try:
        # Check if the list is homogeneous and comparable
        min(arr)
    except TypeError:
        raise TypeError("List contains incomparable elements")
    
    # Create piles (each pile is a sorted subsequence)
    piles = []
    
    for item in arr:
        # Binary search to find the right pile
        new_pile_index = len(piles)
        for i, pile in enumerate(piles):
            # If this pile's top is greater than the item, 
            # we found the right pile
            if pile and pile[-1] > item:
                new_pile_index = i
                break
        
        # Extend existing pile or create new pile
        if new_pile_index == len(piles):
            piles.append([item])
        else:
            piles[new_pile_index].append(item)
    
    # Merge piles using a min-heap
    result = []
    heap = [(pile[0], i, 0) for i, pile in enumerate(piles)]
    heapq.heapify(heap)
    
    while heap:
        val, pile_index, item_index = heapq.heappop(heap)
        result.append(val)
        
        # Move to next item in the pile
        item_index += 1
        if item_index < len(piles[pile_index]):
            next_item = piles[pile_index][item_index]
            heapq.heappush(heap, (next_item, pile_index, item_index))
    
    return result