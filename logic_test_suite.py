import unittest
from copy import deepcopy

from game_logic import GameLogic
from game_controller import PegSolitaireController

class TestLogicBoardSize(unittest.TestCase):

    def setUp(self):
        """Create a new game with the English board type and size 5 before each test."""
        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=5)
        self.game = self.game_controller.logic

    def test_1_1_board_size_regenerates(self):
        """AC 1.1: Selecting a supported board size in a newly generated game 
        changes the board to the new size."""
        self.game_controller.change_board_parameters(board_type="english", size=7)
        expected_board = {
            (0,2): 1, (0,3): 1, (0,4): 1,
            (1,2): 1, (1,3): 1, (1,4): 1,
            (2,0): 1, (2,1): 1, (2,2): 1, (2,3): 1, (2,4): 1, (2,5): 1, (2,6): 1,
            (3,0): 1, (3,1): 1, (3,2): 1, (3,3): 0, (3,4): 1, (3,5): 1, (3,6): 1,
            (4,0): 1, (4,1): 1, (4,2): 1, (4,3): 1, (4,4): 1, (4,5): 1, (4,6): 1,
            (5,2): 1, (5,3): 1, (5,4): 1,
            (6,2): 1, (6,3): 1, (6,4): 1,
        }

        self.assertEqual(self.game.board.keys(), expected_board.keys())

    def test_1_3_new_board_size_is_correct(self):
        """AC 1.3: Starting a new game with a supported board size selected 
        generates a board of the selected size."""
        self.game_controller.new_game(board_type="english", size=7)
        expected_board = {
            (0,2): 1, (0,3): 1, (0,4): 1,
            (1,2): 1, (1,3): 1, (1,4): 1,
            (2,0): 1, (2,1): 1, (2,2): 1, (2,3): 1, (2,4): 1, (2,5): 1, (2,6): 1,
            (3,0): 1, (3,1): 1, (3,2): 1, (3,3): 0, (3,4): 1, (3,5): 1, (3,6): 1,
            (4,0): 1, (4,1): 1, (4,2): 1, (4,3): 1, (4,4): 1, (4,5): 1, (4,6): 1,
            (5,2): 1, (5,3): 1, (5,4): 1,
            (6,2): 1, (6,3): 1, (6,4): 1,
        }
        self.assertEqual(self.game.board.keys(), expected_board.keys())

    def test_1_4_invalid_board_size_rejected(self):
        """AC 1.4: An invalid board size is rejected."""
        expected_board = deepcopy(self.game.board)
        self.game_controller.change_board_parameters(board_type="english", size=4)  # Invalid size for English board
        self.assertEqual(self.game.size, 5)
        self.assertEqual(self.game.board, expected_board)

class TestLogicBoardType(unittest.TestCase):
    
    def setUp(self):
        """Create a new game with the English board type and size 5 before each test."""
        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=5)
        self.game = self.game_controller.logic

    def test_2_1_board_type_regenerates(self):
        """AC 2.1: Selecting a supported board type in a newly generated game 
        changes the board to the new type."""
        self.game_controller.change_board_parameters(board_type="diamond", size=5)
        expected_board = {
            (0,2): 1,
            (1,1): 1, (1,2): 1, (1,3): 1,
            (2,0): 1, (2,1): 1, (2,2): 0, (2,3): 1, (2,4): 1,
            (3,1): 1, (3,2): 1, (3,3): 1,
            (4,2): 1
        }
        self.assertEqual(self.game.board.keys(), expected_board.keys())

    def test_2_3_new_board_type_is_correct(self):
        """AC 2.3: Starting a new game with a supported board size selected 
        generates a board of the selected size."""
        self.game_controller.new_game(board_type="diamond", size=5)
        expected_board = {
            (0,2): 1,
            (1,1): 1, (1,2): 1, (1,3): 1,
            (2,0): 1, (2,1): 1, (2,2): 0, (2,3): 1, (2,4): 1,
            (3,1): 1, (3,2): 1, (3,3): 1,
            (4,2): 1
        }
        self.assertEqual(self.game.board.keys(), expected_board.keys())

class TestLogicFilledSpaces(unittest.TestCase):

    def setUp(self):
        """Create a new game."""
        self.game_controller = PegSolitaireController(False)
        self.game = self.game_controller.logic

    def test_3_1_board_filled_spaces_are_correct(self):
        """AC 3.1: The board is filled with pegs in the correct starting positions."""
        self.game_controller.new_game(board_type="english", size=7)
        expected_board = {
            (0,2): 1, (0,3): 1, (0,4): 1,
            (1,2): 1, (1,3): 1, (1,4): 1,
            (2,0): 1, (2,1): 1, (2,2): 1, (2,3): 1, (2,4): 1, (2,5): 1, (2,6): 1,
            (3,0): 1, (3,1): 1, (3,2): 1, (3,3): 0, (3,4): 1, (3,5): 1, (3,6): 1,
            (4,0): 1, (4,1): 1, (4,2): 1, (4,3): 1, (4,4): 1, (4,5): 1, (4,6): 1,
            (5,2): 1, (5,3): 1, (5,4): 1,
            (6,2): 1, (6,3): 1, (6,4): 1,
        }
        self.game_controller.new_game(board_type="diamond", size=5)
        expected_board = {
            (0,2): 1,
            (1,1): 1, (1,2): 1, (1,3): 1,
            (2,0): 1, (2,1): 1, (2,2): 0, (2,3): 1, (2,4): 1,
            (3,1): 1, (3,2): 1, (3,3): 1,
            (4,2): 1
        }
        self.assertEqual(self.game.board.keys(), expected_board.keys())
        self.game.new_game(board_type="hexagon", size=7)
        expected_board = {
            (0,2): 1, (0,3): 1, (0,4): 1,
            (1,1): 1, (1,2): 1, (1,3): 1, (1,4): 1, (1,5): 1,
            (2,0): 1, (2,1): 1, (2,2): 1, (2,3): 1, (2,4): 1, (2,5): 1, (2,6): 1,
            (3,1): 1, (3,2): 1, (3,3): 0, (3,4): 1, (3,5): 1,
            (4,2): 1, (4,3): 1, (4,4): 1
        }
        self.assertEqual(self.game.board.keys(), expected_board.keys())

class TestLogicMoves(unittest.TestCase):

    def setUp(self):
        """Create a board with a known valid move."""
        self.board = {                          (0,2): 1, (0,3): 1, (0,4): 1,
                                                (1,2): 1, (1,3): 1, (1,4): 1,
                      (2,0): 1,    (2,1): 1,    (2,2): 1, (2,3): 1, (2,4): 1, (2,5): 1,    (2,6): 1,
                      (3,0): 1,    (3,1): 1,    (3,2): 1, (3,3): 0, (3,4): 1, (3,5): 1,    (3,6): 1,
                      (4,0): 1,    (4,1): 1,    (4,2): 1, (4,3): 1, (4,4): 1, (4,5): 1,    (4,6): 1,
                                                (5,2): 1, (5,3): 1, (5,4): 1,
                                                (6,2): 1, (6,3): 1, (6,4): 1,}

        # Set up a valid horizontal jump:
        # source (3, 1), jumped peg (3, 2), destination (3, 3).
        self.board[(3,1)] = 1
        self.board[(3,2)] = 1
        self.board[(3,3)] = 0

        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=7)
        self.game = self.game_controller.logic

        self.game.board = deepcopy(self.board)

    def test_4_1_valid_moves_and_removes_jumped(self):
        """AC 4.1: A valid move moves the peg and removes the jumped peg."""
        move_success = self.game_controller.send_move((3, 1), (3, 3))

        self.assertTrue(move_success)
        self.assertEqual(self.game.board[(3,1)], 0)
        self.assertEqual(self.game.board[(3,2)], 0)
        self.assertEqual(self.game.board[(3,3)], 1)

    def test_4_2_invalid_move_leaves_board_unchanged(self):
        """AC 4.2: An invalid move does not change the board."""
        board_before = deepcopy(self.game.board)

        # Destination is not two spaces away in a straight line.
        move_success = self.game_controller.send_move((3, 1), (4, 2))

        self.assertFalse(move_success)
        self.assertEqual(self.game.board, board_before)

    def test_4_3_move_must_follow_board_type_rules(self):
        """AC 4.3: A move must be legal for the selected board type."""
        # The corner is not a playable space on an English board.
        board_before = deepcopy(self.game.board)

        move_success = self.game_controller.send_move((3, 1), (0, 0))

        self.assertFalse(move_success)
        self.assertEqual(self.game.board, board_before)

class TestLogicGameOver(unittest.TestCase):
    '''Game over testing.'''
    def setUp(self):
        """Create a board with no valid moves."""
        self.board = {
            (0,4): 0,
            (1,4): 0,
            (2,0): 1, (2,1): 0, (2,2): 1, (2,3): 0, (2,4): 0,
            (3,2): 0,
            (4,2): 0
        }

        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=5)
        self.game = self.game_controller.logic

        self.game.board = deepcopy(self.board)

    def test_5_1_game_over_detected(self):
        """AC 5.1: The game detects when there are no valid moves left."""
        self.assertTrue(self.game.game_over() > 0)

if __name__ == "__main__":
    unittest.main()
