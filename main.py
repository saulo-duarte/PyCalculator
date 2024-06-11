import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    window.adjustFixedSize()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Diplay
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid

    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)
    
    # Informações
    info = Info('Hello World!')
    window.addWidgetToVLayout(info)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()