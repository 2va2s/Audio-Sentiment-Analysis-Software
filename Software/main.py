from PyQt5.QtWidgets import *
import sys

from Software.Managers.WindowManager import WindowManager


def main():
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = WindowManager()

    # start the app
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
