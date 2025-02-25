import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test the initialization of KnightsTour class."""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.board) == 8
    assert len(kt.board[0]) == 8

def test_valid_move_detection():
    """Test the is_valid_move method."""
    kt = KnightsTour()
    
    # Test valid moves
    assert kt.is_valid_move(0, 0) == True
    assert kt.is_valid_move(7, 7) == True
    
    # Test out of board moves
    assert kt.is_valid_move(-1, 0) == False
    assert kt.is_valid_move(8, 0) == False
    assert kt.is_valid_move(0, -1) == False
    assert kt.is_valid_move(0, 8) == False

def test_invalid_start_position():
    """Test handling of invalid start positions."""
    kt = KnightsTour()
    
    with pytest.raises(ValueError):
        kt.solve_knights_tour(-1, 0)
    
    with pytest.raises(ValueError):
        kt.solve_knights_tour(8, 0)
    
    with pytest.raises(ValueError):
        kt.solve_knights_tour(0, -1)
    
    with pytest.raises(ValueError):
        kt.solve_knights_tour(0, 8)

def test_knights_tour_solution():
    """Test that a complete Knight's Tour is found."""
    kt = KnightsTour()
    
    # Test different starting positions
    for start_x, start_y in [(0, 0), (3, 3), (7, 7)]:
        tour = kt.solve_knights_tour(start_x, start_y)
        
        # Check that a tour was found
        assert tour is not None
        
        # Check the length of the tour
        assert len(tour) == 64
        
        # Check that all positions are unique
        assert len(set(tour)) == 64
        
        # Verify the tour starts at the correct position
        assert tour[0] == (start_x, start_y)

def test_knight_moves():
    """Test the knight's possible moves."""
    kt = KnightsTour()
    
    # Comprehensive list of expected moves for a typical knight
    expected_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    assert set(kt.moves) == set(expected_moves)

def test_board_reset():
    """Ensure the board is reset between tour attempts."""
    kt = KnightsTour()
    
    # First tour
    first_tour = kt.solve_knights_tour(0, 0)
    assert first_tour is not None
    
    # Second tour from a different start
    second_tour = kt.solve_knights_tour(7, 7)
    assert second_tour is not None
    
    # Ensure the tours are different or reset properly
    assert first_tour != second_tour or len(set(first_tour)) == 64

def test_move_order():
    """Verify the sequence of moves in the tour."""
    kt = KnightsTour()
    
    tour = kt.solve_knights_tour(0, 0)
    assert tour is not None
    
    # Check that each move is a valid knight's move
    for i in range(len(tour) - 1):
        x1, y1 = tour[i]
        x2, y2 = tour[i+1]
        
        # Calculate the move
        dx, dy = x2 - x1, y2 - y1
        
        # Verify it's a valid knight's move
        assert (abs(dx), abs(dy)) in [(1, 2), (2, 1)] or (abs(dx), abs(dy)) in [(2, 1), (1, 2)]