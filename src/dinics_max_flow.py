from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, num_vertices: int):
        """
        Initialize the Dinic's algorithm max flow graph.
        
        :param num_vertices: Number of vertices in the graph
        """
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.flow_edges = {}
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph.
        
        :param u: Source vertex
        :param v: Destination vertex
        :param capacity: Edge capacity
        """
        # Validate input
        if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
            raise ValueError("Vertex index out of range")
        
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        
        # Forward edge
        forward_edge = {'to': v, 'capacity': capacity, 'flow': 0}
        # Reverse edge for residual graph
        reverse_edge = {'to': u, 'capacity': 0, 'flow': 0}
        
        forward_edge['reverse'] = len(self.graph[v])
        reverse_edge['reverse'] = len(self.graph[u])
        
        self.graph[u].append(forward_edge)
        self.graph[v].append(reverse_edge)
    
    def _bfs(self, source: int, sink: int) -> List[int]:
        """
        Breadth-first search to build level graph.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Level of each vertex or -1 if not reachable
        """
        level = [-1] * self.num_vertices
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for edge in self.graph[u]:
                residual_capacity = edge['capacity'] - edge['flow']
                if residual_capacity > 0 and level[edge['to']] == -1:
                    level[edge['to']] = level[u] + 1
                    queue.append(edge['to'])
        
        return level
    
    def _dfs(self, u: int, sink: int, flow: int, level: List[int], 
             blocked_flow: List[int]) -> int:
        """
        Depth-first search for augmenting path.
        
        :param u: Current vertex
        :param sink: Sink vertex
        :param flow: Current flow
        :param level: Level of each vertex
        :param blocked_flow: Tracking flow at each vertex
        :return: Augmented flow
        """
        if u == sink:
            return flow
        
        for i, edge in enumerate(self.graph[u]):
            residual_capacity = edge['capacity'] - edge['flow']
            
            if (level[edge['to']] == level[u] + 1 and 
                residual_capacity > 0 and 
                blocked_flow[u] > 0):
                
                curr_flow = min(flow, residual_capacity)
                curr_flow = min(curr_flow, blocked_flow[u])
                
                temp_flow = self._dfs(edge['to'], sink, curr_flow, 
                                      level, blocked_flow)
                
                if temp_flow > 0:
                    edge['flow'] += temp_flow
                    
                    # Update reverse edge
                    reverse_idx = edge['reverse']
                    self.graph[edge['to']][reverse_idx]['flow'] -= temp_flow
                    
                    blocked_flow[u] -= temp_flow
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using Dinic's algorithm.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices:
            raise ValueError("Invalid source or sink vertex")
        
        if source == sink:
            raise ValueError("Source and sink cannot be the same vertex")
        
        total_flow = 0
        
        while True:
            # Build level graph
            level = self._bfs(source, sink)
            
            # If sink is not reachable, max flow is found
            if level[sink] == -1:
                break
            
            # Track blocked flow for each vertex
            blocked_flow = [float('inf')] * self.num_vertices
            
            # Find blocking flow
            while True:
                flow = self._dfs(source, sink, float('inf'), level, blocked_flow)
                
                if flow == 0:
                    break
                
                total_flow += flow
        
        return total_flow