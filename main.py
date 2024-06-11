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

    
    # Diplay
    display = Display()
    window.add_widget(display)

    # Grid

    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    button1 = Button('Click me 0!')
    buttonsGrid.addWidget(button1, 0, 0)

    button2 = Button('Click me 1!')
    buttonsGrid.addWidget(button2, 0, 1)

    # Botão

    button = Button('Click me 2!')
    window.add_widget(button)
    
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Informações
    info = Info('Hello World!')
    window.add_widget(info)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()