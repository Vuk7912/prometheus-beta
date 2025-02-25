class KnightsTour:
    """
    A class to solve the Knight's Tour problem on an 8x8 chessboard.
    
    The Knight's Tour is a sequence of moves by a knight on a chessboard 
    such that the knight visits every square exactly once.
    """
    
    def __init__(self, board_size=8):
        """
        Initialize the Knight's Tour solver.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.board = [[-1] * board_size for _ in range(board_size)]
        
        # Possible moves for a knight
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def is_valid_move(self, x, y):
        """
        Check if the move is within the board and the square is unvisited.
        
        :param x: x-coordinate on the board
        :param y: y-coordinate on the board
        :return: True if move is valid, False otherwise
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                self.board[x][y] == -1)
    
    def solve_knights_tour(self, start_x, start_y):
        """
        Find a Knight's Tour starting from the given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: List of moves if a tour is found, None otherwise
        """
        # Validate start position
        if not (0 <= start_x < self.board_size and 0 <= start_y < self.board_size):
            raise ValueError("Invalid starting position")
        
        # Reset the board
        self.board = [[-1] * self.board_size for _ in range(self.board_size)]
        
        # Mark the first move
        self.board[start_x][start_y] = 0
        
        # Try to solve the tour
        if self._solve_tour(start_x, start_y, 1):
            return self._get_tour_moves()
        
        return None
    
    def _solve_tour(self, x, y, move_count):
        """
        Backtracking algorithm to solve the Knight's Tour.
        
        :param x: Current x-coordinate
        :param y: Current y-coordinate
        :param move_count: Number of moves made so far
        :return: True if a complete tour is found, False otherwise
        """
        # If all squares are visited, we've found a solution
        if move_count == self.board_size * self.board_size:
            return True
        
        # Try all possible moves
        for dx, dy in self.moves:
            next_x, next_y = x + dx, y + dy
            
            # Check if the move is valid
            if self.is_valid_move(next_x, next_y):
                # Mark the move
                self.board[next_x][next_y] = move_count
                
                # Recursively try to complete the tour
                if self._solve_tour(next_x, next_y, move_count + 1):
                    return True
                
                # Backtrack if the move doesn't lead to a solution
                self.board[next_x][next_y] = -1
        
        return False
    
    def _get_tour_moves(self):
        """
        Convert the board representation to a list of moves.
        
        :return: List of tuples representing the sequence of moves
        """
        tour = [(0, 0)] * (self.board_size * self.board_size)
        for x in range(self.board_size):
            for y in range(self.board_size):
                tour[self.board[x][y]] = (x, y)
        
        return tour