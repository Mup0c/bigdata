import mainWindow
import image_model
from image_model import rgb
from PyQt5 import QtWidgets
from parser_json import Parser
from image_model import *


class AnimatorApp(QtWidgets.QMainWindow, mainWindow.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_file)
        self.btnStart.clicked.connect(self.start_animation)
        self.filename = ""

    def browse_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open data file", "~", "JSON files (*.json)")[0]
        if filename:
            self.filename = filename
            print(filename)

    def start_animation(self):
        if not self.filename:
            print("No file selected")
            return
        parser = Parser(self.filename)
        frame = parser.parse()