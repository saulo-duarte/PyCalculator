from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')
        self.adjustFixedSize()

    def adjustFixedSize(self):
        self.setFixedSize(self.width() - 50, self.height()+20)
        self.adjustSize()

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)


    def makeMessageBox(self):
        return QMessageBox(self)