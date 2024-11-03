import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test2.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test2')

        self.count = 0
        self.pushButton.clicked.connect(self.increase_counter)
        self.pushButton_2.clicked.connect(self.reset_counter)
        self.pushButton_3.clicked.connect(self.edit_text)

        self.lineEdit_2.textChanged.connect(self.change_text)

        self.label.setText(str(self.count))

    def increase_counter(self):
        self.count += 1
        self.label.setText(str(self.count))

    def reset_counter(self):
        self.count = 0
        self.label.setText(str(self.count))

    def edit_text(self):
        self.label.setText(self.lineEdit.text())

    def change_text(self):
        self.lineEdit_3.setText(self.lineEdit_2.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

