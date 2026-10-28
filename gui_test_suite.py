import unittest
import sys
from copy import deepcopy

from game_controller import PegSolitaireController
from game_gui import GameGUI
from PySide6.QtWidgets import QApplication

class TestGUIBoardSize(unittest.TestCase):

    def setUp(self):
        """Create a new game with the English board type and size 5 before each test."""
        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=5)
        self.gui = self.game_controller.gui

    def tearDown(self):
            if QApplication.instance() is not None:
                QApplication.shutdown(self.game_controller.gui_app)
            return super().tearDown()

    def test_1_2_display_size_options(self):
        """AC 1.2: Selecting a board size displays the available size options."""
        available_sizes = [self.gui.size_select.itemText(i) for i in range(self.gui.size_select.count())]
        expected_sizes = ['5', '7', '9'] 

        self.assertEqual(available_sizes, expected_sizes)

class TestGUIBoardTypes(unittest.TestCase):

    def setUp(self):
        """Create a new game with the English board type and size 7 before each test."""
        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=7)
        self.gui = self.game_controller.gui

    def tearDown(self):
        self.gui.close()
        if QApplication.instance() is not None:
            QApplication.shutdown(self.game_controller.gui_app)
        return super().tearDown()

    def test_2_2_valid_move_updates_board_state(self):
        expected_types = ['english', 'diamond', 'hexagon']
        board_types = []
        for button in self.gui.board_type_select.buttons():
            board_types.append(button.text())
        self.assertEqual(board_types, expected_types)

class TestGUIMove(unittest.TestCase):

    def setUp(self):
        """Create a new game with the English board type and size 7 before each test."""
        self.game_controller = PegSolitaireController(False)
        self.game_controller.new_game(board_type="english", size=7)
        self.gui = self.game_controller.gui

    def tearDown(self):
        self.gui.close()
        if QApplication.instance() is not None:
            QApplication.shutdown(self.game_controller.gui_app)
        return super().tearDown()
        
    def test_4_4_valid_move_updates_board_state(self):
        """AC 4.4: The board reflects the new peg positions."""
        expected_board = deepcopy(self.gui.get_board())
        expected_board[(3, 1)] = '0'  # Peg moved from (3, 1)
        expected_board[(3, 2)] = '0'  # Peg jumped over (3, 2)
        expected_board[(3, 3)] = '1'  # Peg moved to (3, 3)

        self.gui.click_position((3,1))
        self.gui.click_position((3,3))
        after_board = self.gui.get_board()
        self.assertEqual(after_board.keys(), expected_board.keys())
        for pos in after_board.keys():
            self.assertEqual(after_board[pos], expected_board[pos])

if __name__ == "__main__":
    unittest.main()
    