import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test9.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test9')

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.spinBoxValue.setText(str(self.spinBox.value()))
        self.sliderValue.setText(str(self.hSlider.value()))

        self.btnApply.clicked.connect(self.apply)

        self.spinBox.valueChanged.connect(self.refreshSpinBoxLabel)
        self.hSlider.valueChanged.connect(self.refreshSliderLabel)

        self.hSlider.setRange(min, max)
        self.hSlider.setSingleStep(step)

        self.pixMap = QPixmap()
        self.pixMap.load('./data/sample.jpg')
        
        # self.labelPixMap.resize(self.pixMap.width(), self.pixMap.height())
        self.pixMap = self.pixMap.scaled(self.labelPixMap.width(), self.labelPixMap.height())
        self.labelPixMap.setPixmap(self.pixMap)

    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()
        
        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.hSlider.setRange(int(min), int(max))
        self.hSlider.setSingleStep(int(step))
    
    def refreshSpinBoxLabel(self):
        self.spinBoxValue.setText(str(self.spinBox.value()))
        self.sliderValue.setText(str(self.spinBox.value()))
        self.hSlider.setValue(self.spinBox.value())

    def refreshSliderLabel(self):
        self.sliderValue.setText(str(self.hSlider.value()))
        self.spinBoxValue.setText(str(self.hSlider.value()))
        self.spinBox.setValue(self.hSlider.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

