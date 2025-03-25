import pytest
from src.johnson_shortest_paths import johnson_shortest_paths

def test_basic_positive_graph():
    """Test a simple graph with positive edge weights."""
    graph = {
        0: {1: 5, 2: 2},
        1: {2: 1, 3: 3},
        2: {3: 6},
        3: {}
    }
    result = johnson_shortest_paths(graph)
    
    # Expected shortest paths (manual calculation)
    assert result[0][1] == 5  # Direct path 0->1
    assert result[0][2] == 2  # Direct path 0->2
    assert result[0][3] == 8  # Path 0->2->1->3
    assert result[1][3] == 3  # Direct path 1->3

def test_graph_with_negative_weights():
    """Test a graph with some negative edge weights."""
    graph = {
        0: {1: -1, 2: 4},
        1: {2: 3, 3: 2},
        2: {3: 5},
        3: {}
    }
    result = johnson_shortest_paths(graph)
    
    # Verify key properties of shortest paths
    assert result[0][1] == -1  # Direct path 0->1
    assert result[0][2] == 2   # Path 0->1->2
    assert result[0][3] == 1   # Path 0->1->3

def test_single_vertex_graph():
    """Test a graph with only one vertex."""
    graph = {0: {}}
    result = johnson_shortest_paths(graph)
    
    # Verify single vertex results
    assert list(result.keys()) == [0]
    assert result[0] == {0: 0}

def test_disconnected_graph():
    """Test a graph with disconnected vertices."""
    graph = {
        0: {1: 5},
        1: {0: 5},
        2: {3: 3},
        3: {2: 3}
    }
    result = johnson_shortest_paths(graph)
    
    # Verify distances between connected components
    assert result[0][1] == 5
    assert result[2][3] == 3
    assert result[0][2] == float('inf')
    assert result[0][3] == float('inf')

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError):
        johnson_shortest_paths({})

def test_negative_cycle_detection():
    """Test a graph with a negative cycle."""
    graph = {
        0: {1: -1},
        1: {2: -1},
        2: {0: -1}
    }
    result = johnson_shortest_paths(graph)
    
    # Verify negative cycle detection
    assert result is None