from collections import deque
from typing import Dict, List, Optional, Set, Union


def find_shortest_path(graph: Dict[Union[str, int], List[Union[str, int]]], 
                       start: Union[str, int], 
                       end: Union[str, int]) -> Optional[List[Union[str, int]]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using BFS.
    
    Args:
        graph (Dict): Adjacency list representation of the graph
        start (str/int): Starting node 
        end (str/int): Target node
    
    Returns:
        Optional[List]: Shortest path from start to end, or None if no path exists
    
    Raises:
        ValueError: If start or end nodes are not in the graph
    """
    # Validate input nodes exist in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    if end not in graph:
        raise ValueError(f"End node {end} not found in graph")
    
    # Handle case where start and end are the same
    if start == end:
        return [start]
    
    # Queue for BFS traversal
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent cycles
    visited: Set[Union[str, int]] = set()
    
    # BFS traversal
    while queue:
        current_node, path = queue.popleft()
        
        # Mark current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            # If neighbor is the target, return the path
            if neighbor == end:
                return path + [neighbor]
            
            # Add unvisited neighbors to queue
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None