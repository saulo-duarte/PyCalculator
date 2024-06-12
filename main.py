import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from styles import setupTheme
from buttons import Button, ButtonsGrid
from info import Info

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    window.adjustFixedSize()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Diplay
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid

    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)
    

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()