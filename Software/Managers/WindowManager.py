from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from Software.QComponents.QButtons.AnalyzeButton import AnalyzeButton
from Software.QComponents.QButtons.PlayButton import PlayButton
from Software.QComponents.QButtons.SelectButton import SelectButton
import pickle


class WindowManager(QMainWindow):
    """
    MainWindow
    """

    def __init__(self):
        super().__init__()
        with open('./mlp_classifier.pkl', 'rb') as pickle_in:
            self.model = pickle.load(pickle_in)
        # create a label for the title
        title_label = QLabel("JPWAV AI V0.0.1", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; padding-top: 20px;")

        # set window properties
        self.setGeometry(500, 250, 950, 540)
        self.setWindowTitle("JPWAV AI V0.0.1")
        self.setStyleSheet("background-color: #525252;")

        # create and add the play button
        self.timer_label = QLabel("Time: 0")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("color:white")
        self.timer_label.hide()
        self.button = PlayButton()
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.timer_label)
        h_layout.addStretch()

        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()
        h_layout2.addWidget(self.button)
        self.analyze_button = AnalyzeButton()
        h_layout2.addWidget(self.analyze_button)
        h_layout2.addStretch()
        self.analyze_button.hide()
        # create and add the QComboBox
        combo_box_layout = QHBoxLayout()
        devices = [device.deviceName() for device in QAudioDeviceInfo.availableDevices(QAudio.AudioInput)]
        # create the first combo box to display the available audio input devices
        self.audio_combo_box = SelectButton(devices, "background-color:white;color:black")
        self.audio_combo_box.device_selected.connect(self.change_recording_device)

        combo_box_layout.addWidget(self.audio_combo_box)

        # add the two layouts to a vertical layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(title_label)
        v_layout.addLayout(combo_box_layout)
        v_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout2)
        v_layout.setAlignment(Qt.AlignBottom)

        # set the layout as the central widget of the main window
        central_widget = QWidget(self)
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # show the window
        self.show()

    def change_recording_device(self, device):
        """
        Change Recording Device
        :param device:
        :return:
        """
        self.button.recorder_manager.setAudioInput(device)
