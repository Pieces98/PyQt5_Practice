import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test3.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test3')

        self.pushButton.clicked.connect(self.addText)
        self.pushButton_2.clicked.connect(self.clearText)
        self.lineEdit.returnPressed.connect(self.addText)

    def addText(self):
        text = self.lineEdit.text()
        self.lineEdit.clear()
        self.textBrowser.append(text)

    def clearText(self):
        self.lineEdit.clear()
        self.textBrowser.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

