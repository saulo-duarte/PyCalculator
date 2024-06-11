from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, DEFAULT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.configSytle()

    def configSytle(self):
        margins = [DEFAULT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        