# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(522, 663)
        self.btnBrowse = QtWidgets.QPushButton(mainWindow)
        self.btnBrowse.setGeometry(QtCore.QRect(270, 550, 241, 71))
        self.btnBrowse.setObjectName("btnBrowse")
        self.btnStart = QtWidgets.QPushButton(mainWindow)
        self.btnStart.setGeometry(QtCore.QRect(10, 550, 241, 71))
        self.btnStart.setObjectName("btnStart")
        self.graphicsView = QtWidgets.QGraphicsView(mainWindow)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 501, 471))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "BIGDATA ANIMATOR 3000"))
        self.btnBrowse.setText(_translate("mainWindow", "Browse"))
        self.btnStart.setText(_translate("mainWindow", "Start"))


