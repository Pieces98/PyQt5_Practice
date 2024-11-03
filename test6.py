import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test6.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test6')

        for year in range(1900, 2050+1):
            self.cBoxYear.addItem(str(year))
        
        for month in range(1, 12+1): 
            self.cBoxMonth.addItem(str(month))
        
        for date in range(1, 31+1):
            self.cBoxDay.addItem(str(date))
        
        self.cBoxYear.setCurrentText(str(1990))
        self.cBoxDay.currentIndexChanged.connect(self.printBirthday)

        self.calendarWidget.clicked.connect(self.selectDate)

    def printBirthday(self):
        year, month, day = self.cBoxYear.currentText(), self.cBoxMonth.currentText(), self.cBoxDay.currentText()
        self.lineEdit.setText(f'{int(year)}-{int(month):02d}-{int(day):02d}')

    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        self.cBoxYear.setCurrentText(date.toString('yyyy'))
        self.cBoxMonth.setCurrentText(date.toString('MM'))
        self.cBoxDay.setCurrentText(date.toString('dd'))
        self.printBirthday()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

