import sys

from PyQt6.QtWidgets import *


class WordTrick(QWidget):
    def __init__(self):
        self.cnt = 0
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 100, 500, 100)
        self.setWindowTitle('Фокус со словами')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(100, 50)
        self.trick_button.move(190, 25)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
