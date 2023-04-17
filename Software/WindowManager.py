from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import os

from Software.QComponents.QButtons.PlayButton import PlayButton

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
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.button)
        h_layout.addStretch()
        v_layout = QVBoxLayout()
        v_layout.addStretch()
        v_layout.addLayout(h_layout)
        v_layout.setAlignment(Qt.AlignBottom)

        # set the layout as the central widget of the main window
        central_widget = QWidget(self)
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

        # show the window
        self.show()
    def UiButton(self):
        # creating a push button
        button = QPushButton("RECORD", self)

        # setting geometry of button
        button.setGeometry(425, 425, 100, 100)

        # setting radius and border
        button.setStyleSheet("border-radius : 50; border: 3 px solid white; background-color: red;color: white;")

        # adding action to a button
        button.clicked.connect(self.on_record_click)
        self.button = button
        return button

    def on_record_click(self):
        if self.recorder.state() == QMediaRecorder.State.RecordingState:
            self.recorder.stop()
            self.button.setText("RECORD")  # change button text back to "RECORD"
        else:
            print("Audio Inputs:")
            # ...
            self.recorder.record()
            self.button.setText("STOP")  # change button text to "STOP"
        for i, audio_input in enumerate(self.recorder.audioInputs()):
            print(f"{i}. {audio_input}")

        self.recorder.setAudioInput(self.selected_audio_input[0])

        settings = QAudioEncoderSettings()

        selected_codec = "audio/pcm"
        print("Codecs:")
        for i, codec in enumerate(self.recorder.supportedAudioCodecs()):
            print(f"{i}. {codec}, ")
        print(f"selected codec:{selected_codec}")
        settings.setCodec(selected_codec)

        selected_sample_rate = 2
        print("Sample rates:")
        sample_rates, continuous = self.recorder.supportedAudioSampleRates()
        for i, sample_rate in enumerate(sample_rates):
            print(f"{i}. {sample_rate}")
        settings.setSampleRate(selected_sample_rate)

        bit_rate = 128000  # other values: 32000, 64000,96000, 128000
        settings.setBitRate(bit_rate)
        channels = -1  # other values: 1, 2, 4
        settings.setChannelCount(channels)
        settings.setQuality(QMultimedia.NormalQuality)
        settings.setEncodingMode(QMultimedia.ConstantBitRateEncoding)

        print("Containers")
        selected_container = "audio/x-wav"
        for i, container in enumerate(self.recorder.supportedContainers()):
            print(f"{i}. {container}")

        self.recorder.setEncodingSettings(
            settings, QVideoEncoderSettings(), selected_container
        )

        filename = os.path.join(CURRENT_DIR, "test.mp3")
        self.recorder.setOutputLocation(QUrl.fromLocalFile(filename))

        def handle_durationChanged(progress):
            print(f"progress: {progress / 1000} seg")

        def handle_statusChanged(status):
            if status == QMediaRecorder.FinalizingStatus:
                print("Recording finalized")
        self.recorder.durationChanged.connect(handle_durationChanged)
        self.recorder.statusChanged.connect(handle_statusChanged)

        def handle_timeout():
            self.recorder.stop()
            self.button.setText("RECORD")
        QTimer.singleShot(10 * 1000, handle_timeout)

