import pytest
from src.dijkstra import dijkstra_shortest_path

def test_basic_shortest_path():
    """Test a simple graph with a clear shortest path"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 6

def test_single_node_path():
    """Test path from a node to itself"""
    graph = {
        'A': {},
        'B': {}
    }
    graph['A']['A'] = 0
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_multiple_possible_paths():
    """Test a graph with multiple possible paths"""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 3},
        'C': {'D': 2},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'B', 'D']
    assert distance == 4

def test_non_existent_start_node():
    """Test raising an error for non-existent start node"""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start node 'X' not found in graph"):
        dijkstra_shortest_path(graph, 'X', 'B')

def test_non_existent_end_node():
    """Test raising an error for non-existent end node"""
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    with pytest.raises(ValueError, match="End node 'X' not found in graph"):
        dijkstra_shortest_path(graph, 'A', 'X')

def test_no_path_exists():
    """Test raising an error when no path exists"""
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists between A and C"):
        dijkstra_shortest_path(graph, 'A', 'C')

def test_complex_graph():
    """Test a more complex graph with multiple nodes and paths"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5, 'E': 6},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4