'''Contains the GameGUI class for the Peg Solitaire game.'''

from functools import partial
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QButtonGroup, QRadioButton, QComboBox

class GameGUI(QWidget):
    '''Class to handle the GUI of the Peg Solitaire game'''
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.board_type = None
        self.size = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Peg Solitaire")
        self.setGeometry(100, 100, 300, 400)
        self.layout = QGridLayout()

        # Left bar contains board type and size selects
        left_bar = QVBoxLayout()

        # Board types as radio select
        left_bar.addWidget(QLabel("Boards:"))
        self.board_type_select = QButtonGroup()
        ind = 0
        for board_type in self.controller.get_board_type_data().keys():
            rad = QRadioButton(board_type)
            rad.clicked.connect(partial(self.update_board_type, board_type))
            self.board_type_select.addButton(rad, ind)
            left_bar.addWidget(rad)
            ind += 1
        self.board_type_select.buttons()[0].setChecked(True)
        self.board_type = str(self.board_type_select.buttons()[0].text())

        # Size select as combo box
        left_bar.addWidget(QLabel("Size:"))
        self.size_select = QComboBox()
        self.size_select.addItems(map(str, self.controller.get_board_type_data()[self.board_type]))
        self.size_select.activated.connect(self.update_size)
        self.size_select.setCurrentIndex(1)
        self.size = int(self.size_select.currentText())
        left_bar.addWidget(self.size_select)

        self.layout.addLayout(left_bar, 0, 0)

        # Game board in the center
        self.board = QWidget()
        self.board.setLayout(QGridLayout())
        self.layout.addWidget(self.board,0,1)

        # Right contains new game button and game over data
        right_bar = QVBoxLayout()

        # New game button
        new_game_button = QPushButton("New Game")
        new_game_button.clicked.connect(self.new_game)
        right_bar.addWidget(new_game_button)

        # Game over bar
        self.game_over_bar = QLabel("")
        right_bar.addWidget(self.game_over_bar)
        self.layout.addLayout(right_bar,0,2)

        self.setLayout(self.layout)

    def new_game(self):
        self.controller.new_game(self.board_type, self.size)
        self.game_over_bar.setText("")

    def update_board(self, board):
        new_board = QGridLayout()
        for pos in board.keys():
            btn = QPushButton(str(board[pos]))
            btn.clicked.connect(partial(self.click_position, pos))
            new_board.addWidget(btn,pos[0],pos[1])

        old_board = QWidget()
        old_board.setLayout(self.board.layout())
        old_board.hide()
        old_board.deleteLater()
        self.board.setLayout(new_board)

    def get_board(self):
        board_representation = {}
        grid = self.board.layout()
        for i in range(grid.rowCount()):
            for j in range(grid.columnCount()):
                if grid.itemAtPosition(i,j) is not None:
                    board_representation[(i,j)] = grid.itemAtPosition(i,j).widget().text()
        return board_representation

    def update_board_type(self, board_type):
        new_type = str(board_type)
        if self.board_type != new_type:
            self.board_type = new_type
            self.controller.change_board_parameters(self.board_type, self.size)

    def update_size(self):
        new_size = int(self.size_select.currentText())
        if self.size != new_size:
            self.size = new_size
            self.controller.change_board_parameters(self.board_type, self.size)

    def update_parameters(self, board_type, size):
        self.board_type = board_type
        for button in self.board_type_select.buttons():
            if button.text() == board_type:
                button.setChecked(True)
                break
        self.size = size
        while self.size_select.count() > 0:
            self.size_select.removeItem(0)
        self.size_select.addItems(map(str, self.controller.get_board_type_data()[self.board_type]))
        self.size_select.setCurrentIndex(self.size_select.findText(str(size)))

    def click_position(self, position):
        self.controller.click_position(position)

    def select(self, position):
        pass

    def deselect_all(self):
        pass

    def display_game_over(self, score):
        self.game_over_bar.setText("Game Over\nScore: " + str(score))
