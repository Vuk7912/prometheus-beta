import pytest
from src.graph_shortest_path import find_shortest_path


def test_basic_path():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    # Direct path
    assert find_shortest_path(graph, 'A', 'B') == ['A', 'B']
    
    # Path with multiple steps 
    path = find_shortest_path(graph, 'A', 'D')
    assert path in [['A', 'B', 'D'], ['A', 'C', 'D']]


def test_same_node():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    # Path to same node
    assert find_shortest_path(graph, 'A', 'A') == ['A']


def test_no_path():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    # Disconnected graph
    assert find_shortest_path(graph, 'A', 'C') is None


def test_complex_path():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Complex multi-step path
    path = find_shortest_path(graph, 'A', 'F')
    assert path in [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


def test_numeric_nodes():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    
    # Path with numeric node labels
    assert find_shortest_path(graph, 1, 2) == [1, 2]


def test_invalid_node_raises_error():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    # Non-existent start node
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        find_shortest_path(graph, 'X', 'A')
    
    # Non-existent end node
    with pytest.raises(ValueError, match="End node Y not found in graph"):
        find_shortest_path(graph, 'A', 'Y')


def test_empty_graph():
    graph = {}
    
    # Empty graph
    with pytest.raises(ValueError, match="Start node A not found in graph"):
        find_shortest_path(graph, 'A', 'B')