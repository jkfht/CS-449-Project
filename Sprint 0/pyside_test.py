""" Test for PySide6 GUI elements """

import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QLabel, QButtonGroup, \
    QCheckBox, QRadioButton, QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt

class GUILibDemo(QMainWindow):
    """ GUI test widget window class """
    def __init__(self):
        """ Initializes the window and adds widgets """
        super().__init__()

        main_widget = QWidget()
        self.resize(300, 200)
        self.setCentralWidget(main_widget)
        self.layout = QGridLayout(main_widget)

        self.layout.addWidget(QLabel("GUI Library Test"), 1, 1, 1,-1,
                              Qt.Alignment.AlignHCenter)
        self.layout.addWidget(QLabel("Check Box:"), 2, 1)
        self.layout.addWidget(QCheckBox("Check this out"), 2, 3)

        self.layout.addWidget(QLabel("Radios:"), 3, 1)
        radios = QButtonGroup()

        for i in range(2):
            for j in range(2):
                if j == 0:
                    rad_text = "Radio Gaga"
                else:
                    rad_text = "Radio GooGoo"
                rad = QRadioButton(rad_text)
                radios.addButton(rad, i*2 + j)
                self.layout.addWidget(rad, i + 3, j + 2)
        for i in range(self.layout.rowCount()):
            self.layout.setRowStretch(i+1, 1)
        for i in range(self.layout.columnCount()):
            self.layout.setColumnStretch(i+1, 1)

    def paintEvent(self, event): #pylint: disable=invalid-name,unused-argument
        """ Paints the divider line element """
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(self.size().width()*0.1,
                              self.size().height()/4,
                              self.size().width()*0.9,
                              self.size().height()/4)
        painter.end()

# Run the application
app = QApplication(sys.argv)
window = GUILibDemo()
window.show()
sys.exit(app.exec())
