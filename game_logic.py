'''Contains the GameLogic class for the Peg Solitaire game.'''

class GameLogic():
    '''Class to handle the logic of the Peg Solitaire game.'''
    def __init__(self, controller):
        self.controller = controller
        self.board = {}
        self.board_type = None
        self.size = None
        self.valid_moves = []
        self.valid_sizes = {
            "english": [5, 7, 9],
            "diamond": [5, 7, 9],
            "hexagon": [5, 7, 9, 11]
        }

    def new_game(self, board_type, size):
        '''Starts a new game with the given board type and size.'''
        self.board_type = str(board_type)
        self.size = size
        self.board = self.generate_board(board_type, size)
        self.valid_moves = self.get_valid_moves()

    def validate_board_parameters(self, board_type, size):
        '''Validates the board type and size.'''
        no_moves_made = self.board == self.generate_board(self.board_type, self.size)
        if size in self.valid_sizes[board_type]:
            return {"board_type": board_type, "size": size, "new_game": no_moves_made}
        elif board_type != self.board_type and size == self.size:
            # If the current size is not valid for the new board type,
            # change to nearest valid size
            new_size = -999
            for test_size in sorted(self.valid_sizes[board_type]):
                if test_size <= self.size:
                    new_size = test_size
                else:
                    if abs(test_size - self.size) < abs(new_size - self.size):
                        new_size = test_size
            return {"board_type": board_type, "size": new_size, "new_game": no_moves_made}
        else:
            return {"board_type": self.board_type, "size": self.size, "new_game": False}

    def change_size(self, size):
        '''If no moves have been made, 
        changes the size of the board and generates a new board.'''            
        if size in self.valid_sizes[self.board_type]:
            if self.board == self.generate_board(self.board_type, self.size):
                self.size = size
                self.board = self.generate_board(self.board_type, size)
                self.valid_moves = self.get_valid_moves()
                return {"board": self.board, "size": self.size}
            else:
                return {"board": self.board, "size": size}
        else:
            return {"board": self.board, "size": self.size}

    def change_board_type(self, board_type):
        '''If no moves have been made,
        changes the board type and generates a new board.'''
        if self.size in self.valid_sizes[board_type]:
            new_size = self.size
        else:
            # If the current size is not valid for the new board type,
            # change to nearest valid size
            new_size = -999
            for test_size in sorted(self.valid_sizes[board_type]):
                if test_size <= self.size:
                    new_size = test_size
                else:
                    if abs(test_size - self.size) < abs(new_size - self.size):
                        new_size = test_size
        
        if self.board == self.generate_board(self.board_type, self.size):
            self.board_type = board_type
            self.size = new_size
            self.board = self.generate_board(board_type, self.size)
            self.valid_moves = self.get_valid_moves()
        return {"board": self.board, "size": new_size}

    def generate_board(self, board_type, size):
        '''Generates a board of the given type and size.'''
        if board_type == "english":
            return self.generate_english_board(size)
        elif board_type == "diamond":
            return self.generate_diamond_board(size)
        elif board_type == "hexagon":
            return self.generate_hexagon_board(size)

    def generate_english_board(self, size):
        '''Generates an English board of the given size.'''
        board = {}
        for i in range(size):
            for j in range(size):
                if ((i < (size // 3) and j < (size // 3))
                    or (i < (size // 3) and j >= size - (size // 3))
                    or (i >= size - (size // 3) and j < (size // 3))
                    or (i >= size - (size // 3) and j >= size - (size // 3))):
                    pass  # Skip corners for English board``
                else:
                    board[(i, j)] = 1 if (i, j) != (size // 2, size // 2) else 0
        return board

    def generate_diamond_board(self, size):
        '''Generates a Diamond board of the given size.'''
        board = {}
        for i in range(size):
            for j in range(size):
                if abs(i - size // 2) + abs(j - size // 2) <= size // 2:
                    board[(i, j)] = 1 if (i, j) != (size // 2, size // 2) else 0
        return board

    def generate_hexagon_board(self, size):
        '''Generates a Hexagon board of the given size.'''
        board = {}
        width = round(size/2) + (round(size/2) + 1) % 2
        for i in range(width):
            for j in range(size):
                dist = abs(i - (width // 2)) + abs(j - (size // 2))
                if dist < size / 2:
                    board[(i, j)] = 1 if (i, j) != (width // 2, size // 2) else 0
        return board

    def make_move(self, from_pos, to_pos):
        '''Moves a peg from from_pos to to_pos.
         Returns True if the move is valid.'''
        if (from_pos, to_pos) in self.get_valid_moves():
            self.board[from_pos] = 0
            self.board[to_pos] = 1
            skip_pos = (from_pos[0] + (to_pos[0] - from_pos[0]) // 2,
                        from_pos[1] + (to_pos[1] - from_pos[1]) // 2)
            self.board[skip_pos] = 0
            return True
        return False

    def get_valid_moves(self):
        '''Returns a list of all valid moves on the current board.
        Each move is represented as a tuple (from_pos, to_pos).'''
        valid_moves = []
        for from_pos in self.board.keys():
            if self.board[from_pos] == 1:  # There's a peg at from_pos
                directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
                for dx, dy in directions:
                    to_pos = (from_pos[0] + dx, from_pos[1] + dy)
                    skip_pos = (from_pos[0] + dx // 2, from_pos[1] + dy // 2)
                    if (to_pos in self.board and self.board[to_pos] == 0
                        and skip_pos in self.board
                        and self.board[skip_pos] == 1):
                        valid_moves.append((from_pos, to_pos))
        return valid_moves

    def game_over(self):
        '''If game is over, return number of remaining pegs, else return 0.'''
        if not self.get_valid_moves():
            return sum(self.board.values())
        return 0
