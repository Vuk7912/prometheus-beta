import pytest
from src.dinics_max_flow import DinicMaxFlow

def test_basic_max_flow():
    """Test basic max flow scenario with a simple graph."""
    dinic = DinicMaxFlow(4)
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 2, 2)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(2, 3, 8)
    
    max_flow = dinic.max_flow(0, 3)
    assert max_flow == 14

def test_single_edge_max_flow():
    """Test max flow with a single direct edge."""
    dinic = DinicMaxFlow(2)
    dinic.add_edge(0, 1, 5)
    
    max_flow = dinic.max_flow(0, 1)
    assert max_flow == 5

def test_no_path_max_flow():
    """Test max flow when no path exists."""
    dinic = DinicMaxFlow(3)
    dinic.add_edge(0, 1, 5)
    
    max_flow = dinic.max_flow(0, 2)
    assert max_flow == 0

def test_complex_max_flow():
    """Test a more complex graph with multiple paths."""
    dinic = DinicMaxFlow(6)
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(1, 4, 8)
    dinic.add_edge(2, 3, 6)
    dinic.add_edge(2, 4, 2)
    dinic.add_edge(3, 5, 7)
    dinic.add_edge(4, 5, 12)
    
    max_flow = dinic.max_flow(0, 5)
    assert max_flow == 17

def test_invalid_vertex_input():
    """Test error handling for invalid vertex indices."""
    dinic = DinicMaxFlow(3)
    
    with pytest.raises(ValueError, match="Vertex index out of range"):
        dinic.add_edge(0, 5, 10)
    
    with pytest.raises(ValueError, match="Invalid source or sink vertex"):
        dinic.max_flow(0, 5)

def test_negative_capacity():
    """Test error handling for negative capacity."""
    dinic = DinicMaxFlow(2)
    
    with pytest.raises(ValueError, match="Capacity cannot be negative"):
        dinic.add_edge(0, 1, -5)

def test_source_sink_same():
    """Test error handling when source and sink are the same."""
    dinic = DinicMaxFlow(2)
    
    with pytest.raises(ValueError, match="Source and sink cannot be the same vertex"):
        dinic.max_flow(0, 0)