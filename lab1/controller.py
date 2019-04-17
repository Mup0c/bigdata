import image_model
from parser_json import Parser
from image_model import *
import threading
from PyQt5.QtGui import * # QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

class AnimatorApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("mainWindow", "BIGDATA ANIMATOR 3000"))
        self.resize(1000, 663)
        self.btnBrowse = QtWidgets.QPushButton(self)
        self.btnBrowse.setGeometry(QtCore.QRect(270, 550, 241, 71))
        self.btnBrowse.setObjectName("btnBrowse")
        self.btnStart = QtWidgets.QPushButton(self)
        self.btnStart.setGeometry(QtCore.QRect(10, 550, 241, 71))
        self.btnStart.setObjectName("btnStart")
        self.graphicsView = QtWidgets.QFrame(self)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 501, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.btnBrowse.setText(_translate("mainWindow", "Browse"))
        self.btnStart.setText(_translate("mainWindow", "Start"))
        QtCore.QMetaObject.connectSlotsByName(self)
        self.btnBrowse.clicked.connect(self.browse_file)
        self.btnStart.clicked.connect(self.start_animation)
        self.filename = ""
        self.graphicsView.paintEvent = self.paint
        self.painter = QPainter(self.graphicsView)
        self.pixmap = None



    def browse_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open data file", "~", "JSON files (*.json)")[0]
        if filename:
            self.filename = filename
            print(filename)
            if not self.filename:
                print("No file selected")
                return
            self.parser = Parser(self.filename)

    def start_animation(self):
        if not self.filename:
            print("No file selected")
            return
        self.parsendraw()

    def parsendraw(self):
        print("begin")

        frame = self.parser.parse()
        print("parsed")
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, frame.w, frame.h))
        self.image = QImage(frame.w, frame.h, QImage.Format_RGB32)
        x = 0
        y = 0
        for i in range(len(frame.pixels)):
            self.image.setPixelColor(y, x, QColor(*frame.pixels[i]))
            if ((i + 1) % frame.h == 0):
                x = 0
                y += 1
            else:
                x += 1
        print("drawn")
        self.pixmap = QPixmap(self.image)
        threading.Timer(0.001, self.parsendraw).start()

    def paint(self, event):
        self.painter.begin(self.graphicsView)
        if not self.pixmap == None:
            self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.end()
        self.update()


            #self.current_pixmap = QPixmap(self.new_image)


