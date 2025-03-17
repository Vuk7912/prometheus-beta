import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start: str, end: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between start and end nodes in a weighted graph using Dijkstra's algorithm.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Each key is a node, and its value is a dict of neighboring nodes 
                                           with their corresponding edge weights.
        start (str): Starting node
        end (str): Destination node
    
    Returns:
        Tuple[List[str], int]: A tuple containing:
            - The shortest path as a list of nodes
            - The total distance of the path
    
    Raises:
        ValueError: If start or end node is not in the graph
        ValueError: If no path exists between start and end nodes
    """
    # Validate input nodes exist in the graph
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    if end not in graph:
        raise ValueError(f"End node '{end}' not found in graph")
    
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the end node, reconstruct and return the path
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors[current_node]
            return list(reversed(path)), current_distance
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # If no path is found
    raise ValueError(f"No path exists between {start} and {end}")