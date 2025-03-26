from typing import List, Union, Any

def multiply_array_elements(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    """
    Multiply corresponding elements from two input arrays.
    
    Args:
        arr1 (List[Any]): First input array
        arr2 (List[Any]): Second input array
    
    Returns:
        List[Any]: Array with elements multiplied pairwise
    
    Raises:
        ValueError: If input arrays have different lengths
        TypeError: If multiplication is not supported for given element types
    """
    # Check if arrays have the same length
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length")
    
    # Validate that elements can be multiplied
    def can_multiply(a, b):
        try:
            a * b
            return True
        except TypeError:
            return False
    
    # Check if all elements can be multiplied
    if not all(can_multiply(a, b) for a, b in zip(arr1, arr2)):
        raise TypeError("Cannot multiply all elements in the arrays")
    
    # Multiply corresponding elements
    return [a * b for a, b in zip(arr1, arr2)]