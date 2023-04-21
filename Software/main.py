from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
import os
from PyQt5.QtGui import QFont

from WindowManager import WindowManager


def main():
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = WindowManager()

    # start the app
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
