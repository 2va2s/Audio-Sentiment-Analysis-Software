from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import os

from Software.QComponents.QButtons.PlayButton import PlayButton
from Software.QComponents.QButtons.SelectButton import SelectButton


class WindowManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = None
        self.layout = QVBoxLayout()

        # set window properties
        self.setGeometry(500, 250, 950, 540)
        self.setWindowTitle("JPWAV AI V0.0.1")
        self.setStyleSheet("background-color: #525252;")

        # create and add the play button
        self.button = PlayButton()
        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()
        h_layout2.addWidget(self.button)
        h_layout2.addStretch()

        # create and add the QComboBox
        combo_box_layout = QHBoxLayout()
        devices = [device.deviceName() for device in QAudioDeviceInfo.availableDevices(QAudio.AudioInput)]
        # create the first combo box to display the available audio input devices
        combo_box_layout.addWidget(SelectButton(devices))
        combo_box_layout.addWidget(SelectButton(["Item 1", "Item 2", "Item 3"]))
        combo_box_layout.addWidget(SelectButton(["Item 1", "Item 2", "Item 3"]))
        combo_box_layout.addWidget(SelectButton(["Item 1", "Item 2", "Item 3"]))
        combo_box_layout.addWidget(SelectButton(["Item 1", "Item 2", "Item 3"]))
        combo_box_layout.addWidget(SelectButton(["Item 1", "Item 2", "Item 3"]))

        # add the two layouts to a vertical layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(combo_box_layout)
        v_layout.addStretch()
        v_layout.addLayout(h_layout2)
        v_layout.setAlignment(Qt.AlignBottom)

        # set the layout as the central widget of the main window
        central_widget = QWidget(self)
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # show the window
        self.show()
