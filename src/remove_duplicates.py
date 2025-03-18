from typing import List, TypeVar, Union

T = TypeVar('T')

def remove_duplicates(arr: List[T]) -> List[T]:
    """
    Remove duplicate elements from an array while maintaining O(n) time complexity.
    
    This function uses a set to track unique elements, preserving the original 
    order of first occurrence for each unique element.
    
    Args:
        arr (List[T]): Input list that may contain duplicate elements
    
    Returns:
        List[T]: A new list with duplicates removed, maintaining original order
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 1, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b', 'c']
        >>> remove_duplicates([])
        []
    """
    # Handle empty input
    if not arr:
        return []
    
    # Use a set to track seen elements 
    seen = set()
    result = []
    
    # Iterate through the input array
    for item in arr:
        # Only add to result if not seen before
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result