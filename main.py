from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys
import os
from PyQt5.QtGui import QFont

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(app.exec())


def on_tick_record():
    message = QMessageBox()
    message.setText("Processing...")
    message.exec_()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.recorder = QAudioRecorder()
        self.selected_audio_input = self.recorder.audioInput()

        # setting geometry
        self.setGeometry(500, 250, 950, 540)



        self.setWindowTitle("JPWAV AI V0.0.1")

        self.setStyleSheet("background-color: #525252;")

        self.layout.addWidget(self.UiButton())
        self.layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.layout)

        # showing all the widgets
        self.show()

    # method for widgets
    def UiButton(self):
        # creating a push button
        button = QPushButton("RECORD", self)

        # setting geometry of button
        button.setGeometry(200, 150, 100, 100)

        # setting radius and border
        button.setStyleSheet("border-radius : 50; border: 3 px solid white; background-color: red;color: white;")

        # adding action to a button
        button.clicked.connect(self.on_record_click)

        return button

    def on_record_click(self):
        print("Audio Inputs:")
        for i, audio_input in enumerate(self.recorder.audioInputs()):
            print(f"{i}. {audio_input}")

        self.recorder.setAudioInput(self.selected_audio_input[1])

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
                QTimer.singleShot(1 * 1000, QCoreApplication.quit)

        self.recorder.durationChanged.connect(handle_durationChanged)
        self.recorder.statusChanged.connect(handle_statusChanged)

        def handle_timeout():
            self.recorder.stop()

        QTimer.singleShot(10 * 1000, handle_timeout)

        self.recorder.record()


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


