import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/practice2.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - practice 2')

        self.pixMap = QPixmap()

        self.btnLoad.clicked.connect(self.loadImage)
        self.btnSave.clicked.connect(self.saveImage)

        self.hSlider.valueChanged.connect(self.changeScale)
        self.hSlider.setRange(1, self.labelPixMap.width())
        self.hSlider.setValue(self.labelPixMap.width())

        self.counter = 0
        self.fname = ''
    
    def loadImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname[0]:
            self.fname = fname[0]
            self.pixMap.load(self.fname)
            f = self.hSlider.value()/self.labelPixMap.width()
            self.pixMap = self.pixMap.scaledToWidth(int(f*self.labelPixMap.width()))
            self.labelPixMap.setPixmap(self.pixMap)

    def saveImage(self):
        if self.fname:
            path, ext = self.fname.split('.')
            saveFileName = path+'_'+str(self.counter)+'.'+ext
            self.counter += 1
            self.pixMap.save(saveFileName)
            

    def changeScale(self):
        if self.pixMap.size().width():
            f = self.hSlider.value()/self.labelPixMap.width()
            self.pixMap = self.pixMap.scaledToWidth(int(f*self.labelPixMap.width()))
            self.labelPixMap.setPixmap(self.pixMap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

