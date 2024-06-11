from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import is_number_or_dot, is_empty

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPointSize(MEDIUM_FONT_SIZE)
        font.setFamily('Segoe UI')
        font.setBold(True)
        self.setFont(font)

class ButtonsGrid(QGridLayout):
    def   __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMasks = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]

        for rowNumber, rowData in enumerate(self._gridMasks):
                for colNumber, buttonText in enumerate(rowData):
                    button = Button(buttonText)

                    if not is_number_or_dot(buttonText) and not is_empty(buttonText):
                        button.setProperty('cssClass', 'specialButton')

                    self.addWidget(button, rowNumber, colNumber)

    