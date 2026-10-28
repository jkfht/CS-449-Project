'''Contains the PegSolitaireController class for the Peg Solitaire game.'''

import sys
from PySide6.QtWidgets import QApplication
from game_gui import GameGUI
from game_logic import GameLogic

class PegSolitaireController:
    '''Handles communication between game logic and GUI'''
    def __init__(self, keep_open = True):
        self.gui_app= QApplication.instance() or QApplication(sys.argv)
        self.logic = GameLogic(self)
        self.gui = GameGUI(self)
        self.selected_piece = None
        self.gameover_lock = False
        self.gui.show()
        self.new_game("english", 7)
        # Block to prevent unnecessary exception
        try:
            if keep_open:
                sys.exit(self.gui_app.exec())
        except:
            pass

    def __exit__(self, exc_type, exc, tb):
        '''Shuts down app instance upon close'''
        if QApplication.instance() is not None:
            QApplication.shutdown(self.gui_app)

    def new_game(self, board_type, size):
        self.logic.new_game(board_type, size)
        self.gui.update_board(self.logic.board)
        self.gui.update_parameters(board_type, size)
        self.gameover_lock = False  # Reset the game over lock for a new game

    def click_position(self, position):
        if self.gameover_lock:
            return  # Ignore clicks if the game is over
        # If peg at the clicked position
        if self.logic.board.get(position) == 1:
            self.selected_piece = position
            self.gui.select(position)  # Highlight the selected piece in the GUI
        elif self.selected_piece is not None:
            if self.send_move(self.selected_piece, position):
                self.selected_piece = None
                self.gui.update_board(self.logic.board)
                self.gui.deselect_all()
                gameover_score = self.logic.game_over()
                if gameover_score > 0:  # If game is over
                    self.gameover_lock = True  # Lock the game
                    self.gui.display_game_over(gameover_score)

    def change_board_parameters(self, board_type, size):
        validation = self.logic.validate_board_parameters(board_type, size)
        # Change gui size to match logic
        self.gui.update_parameters(board_type, validation["size"])
        if validation["new_game"]:
            self.new_game(validation["board_type"], validation["size"])

    def get_board_type_data(self):
        return self.logic.valid_sizes

    def send_move(self, from_pos, to_pos):
        if self.logic.make_move(from_pos, to_pos):
            self.gui.update_board(self.logic.board)
            return True
        else:
            return False

if __name__ == "__main__":
    controller = PegSolitaireController()
