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


def on_tick_record():
    message = QMessageBox()
    message.setText("Processing...")
    message.exec_()

if __name__ == '__main__':
    main()


def oldmain():
    app = QApplication([])
    window = QWidget()

    ## label = QLabel(window)
    ## label.setText("Welcome to JPWAV IA")
    ## label.setFont(QFont("Arial", 16))
    ## label.move(350, 100)

    layout = QVBoxLayout()

    label = QLabel("Welcome to JPWAV AI")
    record_button = QPushButton("Record")
    validate_recorded_audio_button = QPushButton("\\/")

    record_button.clicked.connect()
    validate_recorded_audio_button.clicked.connect(on_tick_record)

    layout.addWidget(label)
    layout.addWidget(record_button)
    layout.addWidget(validate_recorded_audio_button)

    window.setLayout(layout)

    window.show()
    app.exec_()


