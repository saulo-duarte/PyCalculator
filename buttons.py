from PySide6.QtWidgets import QPushButton, QGridLayout
from info import Info
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import is_number_or_dot, is_empty, isValidNumber
from display import Display
from math import pow
from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', 
                 window: 'MainWindow',*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]
        self.info = info
        self.display = display
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Digite sua conta'
        self._equation = self._equationInitialValue
        self._left = None
        self._right = None
        self._operator = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
        
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)
                
                if not is_number_or_dot(buttonText) and not is_empty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                
                self.addWidget(button, rowNumber, colNumber)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clearDisplay)

        if text == '<':
            self._connectButtonClicked(button, self._makeSlot(self.display.backspace))
        
        if text in ['+', '-', '*', '/', '^']:
            self._connectButtonClicked(button, self._makeSlot(self._operatorClicked, button))

        if text == '=':
            self._connectButtonClicked(button, self._makeSlot(self._eq))



    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot  

    @Slot()
    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
    
    @Slot()
    def _clearDisplay(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and displayText is None:
            return
        
        if self._left is None:
        
            try:  
                self._left = float(displayText)
            except ValueError:
                self._showError("Operação inválida!")
                return
            
        self._operator = buttonText
        self.equation = f'{self._left} {self._operator} ??'

    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            self._showError("Operação inválida!")
            return
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 'error'
        
        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = pow(self._left, self._right)
            elif self.equation and isinstance(self._left, float):
                result = eval(self.equation)
        
        except ZeroDivisionError:
            self._showError("voce não pode dividir por zero!")
            return
        
        except OverflowError:
            self._showError("O resultado é grande demais para ser exibido!")
            return

        
        self.display.setText(str(result))
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

    def _showError(self, text):
        self._clearDisplay()
        msgBox = self.window.makeMessageBox()
        msgBox.setText(text)
        msgBox.setWindowTitle('Erro')
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()