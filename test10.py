import sys
import cv2, imutils, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

from_class = uic.loadUiType('./interface/test10.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyQt5 - Test10')

        self.pixmap = QPixmap()
        self.btnOpen.clicked.connect(self.openFile)

        self.btnCamera.clicked.connect(self.connectCamera)

        self.camera = Camera(self)
        self.isCameraOn = False
        self.camera.daemon = True
        self.count = 0

        self.camera.update.connect(self.updateCamera)

    def openFile(self):
        file = QFileDialog.getOpenFileName(filter='Image (*.*)')
        if file[0]:
            image = cv2.imread(file[0])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h, w, c = image.shape
            qImage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qImage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)

    def connectCamera(self):
        if self.isCameraOn:
            self.btnCamera.setText('Camera On')
            self.cameraStop()
        else:
            self.btnCamera.setText('Camera Off')
            self.cameraStart()
        
        self.isCameraOn = not self.isCameraOn
    
    def updateCamera(self):
        ret, image = self.video.read()
        if ret:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            h, w, c = image.shape
            qImage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qImage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        self.count += 1
        
    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        
        self.video = cv2.VideoCapture(0)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0

        self.video.release()

class Camera(QThread):
    update = pyqtSignal()

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True

    def run(self):
        count = 0
        while self.running:
            self.update.emit()
            time.sleep(0.1)
    
    def stop(self):
        self.running = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())

