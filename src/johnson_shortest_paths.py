import heapq
from typing import Dict, List, Tuple, Optional

def johnson_shortest_paths(graph: Dict[int, Dict[int, int]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm to find shortest paths between all pairs of vertices.
    
    Johnson's algorithm combines Bellman-Ford and Dijkstra's algorithms to find 
    shortest paths in a graph that may contain negative edge weights (but no negative cycles).
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are source vertices, values are dicts of 
                                           {destination: weight} for each edge.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: A dictionary of shortest paths between all pairs of vertices.
        None if a negative cycle is detected.
    
    Raises:
        ValueError: If the graph is empty.
    """
    # Check for empty graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Get all vertices
    vertices = set(graph.keys()).union(
        set(v for edges in graph.values() for v in edges.keys())
    )
    
    # Add a new source vertex
    vertices_list = list(vertices)
    new_source = max(vertices) + 1 if vertices else 0
    
    # Create modified graph with new source vertex
    modified_graph = graph.copy()
    modified_graph[new_source] = {v: 0 for v in vertices_list}
    
    # Step 1: Bellman-Ford to compute vertex potentials
    potentials = bellman_ford(modified_graph, new_source)
    
    # Check if Bellman-Ford detected a negative cycle
    if potentials is None:
        return None
    
    # Step 2: Reweight the graph
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v, weight in graph[u].items():
            reweighted_graph[u][v] = weight + potentials[u] - potentials[v]
    
    # Step 3: Run Dijkstra's for each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = dijkstra(reweighted_graph, source, potentials)
    
    return shortest_paths

def bellman_ford(graph: Dict[int, Dict[int, int]], source: int) -> Optional[Dict[int, int]]:
    """
    Bellman-Ford algorithm to detect negative cycles and compute vertex potentials.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Graph representation
        source (int): Source vertex
    
    Returns:
        Optional[Dict[int, int]]: Dictionary of vertex potentials, or None if negative cycle exists
    """
    # Initialize distances
    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    
    # Relax edges |V| - 1 times
    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # Check for negative cycle
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return None
    
    return dist

def dijkstra(graph: Dict[int, Dict[int, int]], source: int, potentials: Dict[int, int]) -> Dict[int, int]:
    """
    Dijkstra's algorithm with vertex potentials for reweighted graph.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Reweighted graph
        source (int): Source vertex
        potentials (Dict[int, int]): Vertex potentials from Bellman-Ford
    
    Returns:
        Dict[int, int]: Shortest distances from source to all other vertices
    """
    # Priority queue to store vertices to visit
    pq = [(0, source)]
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_dist > distances[u]:
            continue
        
        # Check all neighbors
        for v, weight in graph[u].items():
            # Compute distance with potential correction
            dist = current_dist + weight
            
            # Update if shorter path found
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    
    # Adjust distances back to original weights
    return {
        v: (dist + potentials[v] - potentials[source]) 
        if dist != float('inf') else float('inf')
        for v, dist in distances.items()
    }