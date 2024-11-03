import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test5.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test5')

        self.btnName.clicked.connect(self.inputName)
        self.btnSeason.clicked.connect(self.selectSeason)
        self.btnColor.clicked.connect(self.changeColor)
        self.btnFont.clicked.connect(self.changeFont)
        self.btnFile.clicked.connect(self.selectFile)
        self.lineEdit.returnPressed.connect(self.checkInput)

    def inputName(self):
        text, ok = QInputDialog.getText(self, 'QInputDialog - Name', 'User Name: ')

        if ok and text:
            self.textEdit.append(text)

    def selectSeason(self):
        items = ['Spring', 'Summer', 'Fall', 'Winter']
        item, ok = QInputDialog.getItem(self, 'QInputDialog - Season', 'Season: ', items, 0, False)
        if ok and item:
            self.textEdit.append(item)

    def changeColor(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.textEdit.append(f"Color {color.getRgb()}")
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)
    
    def changeFont(self):
        font , ok = QFontDialog.getFont()

        if ok and font:
            info = QFontInfo(font)
            self.textEdit.append(info.family()+info.styleName())
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)

    def selectFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        print(fname)

        if fname[0]:
            with open(fname[0], 'r') as fr:
                data = fr.read()
                self.textEdit.setText(data)

    def checkInput(self):
        text = self.lineEdit.text()
        if text.isdigit():
            self.textEdit.setText(text)
            self.lineEdit.clear()
        else:
            ret = QMessageBox.warning(self, 'QMessageBox - question', 'Are you sure to print', 
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.textEdit.setText(text)
                self.lineEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

