import sys
from PyQt5 import QtWidgets
from controller import AnimatorApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AnimatorApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()