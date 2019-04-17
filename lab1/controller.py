import image_model
from parser_json import Parser
from image_model import *
from PyQt5.QtCore import * # QTimer
from PyQt5.QtGui import * # QApplication
from PyQt5.QtOpenGL import * # QGLWidget
from OpenGL.GL import * # OpenGL functionality
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
        self.openGLWidget = OpenGLView(self)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.openGLWidget.setObjectName("openGLWidget")
        self.btnBrowse.setText(_translate("mainWindow", "Browse"))
        self.btnStart.setText(_translate("mainWindow", "Start"))
        QtCore.QMetaObject.connectSlotsByName(self)
        self.btnBrowse.clicked.connect(self.browse_file)
        self.btnStart.clicked.connect(self.start_animation)
        self.filename = ""



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

        self.parsendraw()
        # self.__timer = QTimer()
        # self.__timer.timeout.connect(self.parsendraw(self))
        # self.__timer.start(5000)

    def parsendraw(self):
        frame = self.parser.parse()
        self.openGLWidget.drawFrame(frame)


class OpenGLView(QGLWidget):
    def initializeGL(self):
        pass
        # set the RGBA values of the background
        #glClearColor(0.1, 0.2, 0.3, 1.0)
        # set a timer to redraw every 1/60th of a second
        #
        #self.__timer.timeout.connect(self.repaint)  # make it repaint when triggered
        #self.__timer.start(1000 / 60)  # make it trigger every 1000/60 milliseconds

    def resizeGL(self, width, height):
        # this tells openGL how many pixels it should be drawing into
        glViewport(0, 0, width, height)

    def paintGL(self):
        pass
        # empty the screen, setting only the background color
        # the depth_buffer_bit also clears the Z-buffer, which is used to make sure
        # objects that are behind other objects actually are not shown drawing
        # a faraway object later than a nearby object naively implies that it will
        # just fill in the pixels with itself, but if there is already an object there
        # the depth buffer will handle checking if it is closer or not automatically
        # print("draw")
        #
        #
        # glBegin(GL_POINTS)
        #
        # glColor3ub(255,255,255)
        # glVertex2d(0.7,0.7)
        # glVertex2d(0.5,0.5)
        # glVertex2d(0.6,0.6)
        #
        # glEnd()

        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # # the openGL window has coordinates from (-1,-1) to (1,1), so this fills in
        # # the top right corner with a rectangle. The default color is white.
        # glColor3ub(255, 0, 255)
        # #glRectf(0, 0, 1, 0.5)
        # glPointSize(10)
        # glBegin(GL_POINTS)
        # glColor3d(255, 0, 255)
        # glVertex2d(-1, -1)
        # glColor3d(0, 1, 0)
        # glVertex3d(-4, 4, 0)
        # glColor3d(0, 0, 1)
        # glVertex3d(-3.5, 4, 0)
        # glEnd()
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def drawFrame(self, frame):
        self.setGeometry(QtCore.QRect(0, 0, frame.w, frame.h))
        x = 1.0
        y = -1.0
        glPointSize(2)
        glBegin(GL_POINTS)
        for i in range(len(frame.pixels)):
            glColor3ub(*frame.pixels[i])
            glVertex2d(y, x)
            if (i != 0 and i % frame.w == 0):
                x = 1.0
                y += 2.0 / frame.h
            else:
                x -= 2 / frame.w
        glEnd()
        print("drawframe")
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glFlush()