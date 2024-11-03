import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test4.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test4')

        self.btn_add.clicked.connect(self.addText)
        self.btn_font_1.clicked.connect(lambda : self.setFont('Gulim'))
        self.btn_font_2.clicked.connect(lambda : self.setFont('D2Coding'))

        self.btn_text_color_1.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.btn_text_color_2.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.btn_text_color_3.clicked.connect(lambda: self.setTextColor(0, 0, 255))

        self.btn_setsize.clicked.connect(self.setTextSize)

    def addText(self):
        text = self.input_text.toPlainText()
        self.input_text.clear()
        self.output_text.append(text)

    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.output_text.setFont(font)

    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)

        # method 1 - blocked text
        # self.output_text.setTextColor(color)

        # method 2 - all text
        self.output_text.selectAll()
        self.output_text.setTextColor(color)
        self.output_text.moveCursor(QTextCursor.End)

    def setTextSize(self):
        size = int(self.input_fontsize.text())
        self.output_text.selectAll()
        self.output_text.setFontPointSize(size)
        self.output_text.moveCursor(QTextCursor.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

