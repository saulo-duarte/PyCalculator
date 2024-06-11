from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE

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
        ...