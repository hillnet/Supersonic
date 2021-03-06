from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from python.Constants import *


class TextBox(QLineEdit):
    def __init__(self, frame, name, q_rect):
        super().__init__(frame)
        self.setEnabled(False)
        self.setGeometry(q_rect)
        font = QFont()
        font.setFamily(FONT)
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        self.setReadOnly(False)
        self.setClearButtonEnabled(False)
        self.setObjectName(name)
