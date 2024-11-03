import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from datetime import datetime

from_class = uic.loadUiType('./interface/practice1.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self, df):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - practice 1')

        self.df = df
        self.date_min = self.df.min(axis=0)['BIRTHDAY']
        self.date_max = self.df.max(axis=0)['BIRTHDAY']
        self.agency_list = set(self.df['AGENCY'])
        self.sex_list = set(self.df['SEX'])
        self.job_list = set()
        for jobs in self.df['JOB_TITLE']:
            for job in jobs.split(','):
                self.job_list.add(job.rstrip().lstrip())

        self.dateStart.setMinimumDate(QDate(self.date_min))
        self.dateStart.setDate(QDate(self.date_min))
        self.dateEnd.setMaximumDate(QDate(self.date_max))
        self.dateEnd.setDate(QDate(self.date_max))

        for s in sorted(self.sex_list):
            self.cBoxSex.addItem(s)
        for j in sorted(self.job_list):
            self.cBoxJob.addItem(j)
        for a in sorted(self.agency_list):
            self.cBoxAgency.addItem(a)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.btnSearch.clicked.connect(self.search)

    def search(self):
        dateFrom = self.dateStart.date().toPyDate()
        dateTo = self.dateEnd.date().toPyDate()
        if dateFrom>dateTo:
            QMessageBox.warning(self, 'QMessageBox - Warning', 'End date must be later than Start date', 
                                      QMessageBox.Yes, QMessageBox.Yes)
            return

        dateFrom = dateFrom.strftime('%Y-%m-%d')
        dateTo = dateTo.strftime('%Y-%m-%d')
        targetSex = self.cBoxSex.currentText()
        targetJob = self.cBoxJob.currentText()
        targetAgency = self.cBoxAgency.currentText()

        query_expr = f'("{dateFrom}" <= BIRTHDAY) and (BIRTHDAY <= "{dateTo}") and ("{targetSex}" == SEX) and (JOB_TITLE.str.contains("{targetJob}")) and ("{targetAgency}" == AGENCY)'
        result = self.df.query(query_expr)
        
        self.tableWidget.setRowCount(0)

        print(result)

        for idx in result.index:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.df['ID'][idx])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.df['NAME'][idx]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.df['BIRTHDAY'][idx].strftime('%Y-%m-%d')))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(self.df['AGE'][idx])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(self.df['SEX'][idx]))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(self.df['JOB_TITLE'][idx]))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(self.df['AGENCY'][idx]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    df = pd.read_excel('./data/sample_data1.xlsx')
    myWindows = WindowClass(df)

    myWindows.show()



    sys.exit(app.exec())

