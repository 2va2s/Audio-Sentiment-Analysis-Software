from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtMultimedia import QMultimedia
from PyQt5.QtWidgets import QPushButton, QLabel

from Software.Managers.RecorderManager import RecorderManager
from Software.States.ButtonState import ButtonState

class PlayButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.state = ButtonState.INACTIVE
        self.setText(self.state.value)
        self.setFixedSize(100, 100)
        self.setStyleSheet("border-radius : 50px; border: 3 px solid white; background-color: red;color: white;")
        self.clicked.connect(self.click)
        self.recorder_manager = RecorderManager(
            "audio/pcm",
            2,
            128000,
            -1,
            QMultimedia.NormalQuality,
            QMultimedia.ConstantBitRateEncoding,
            "audio/x-wav")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle_timeout)
        self.recorder_manager.durationChanged.connect(self.handle_durationChanged)

    def handle_timeout(self):
        print("timer timeout")
        self.timer.stop()
        self.recorder_manager.stop()
        self.window().timer_label.hide()
        self.changeState(ButtonState.FINALIZED)
        self.window().analyze_button.show()

    def click(self):
        if self.state == ButtonState.PLAYING:
            print("stop")
            self.timer.stop()
            self.changeState(ButtonState.FINALIZED)
            self.recorder_manager.stop()
            self.recorder_manager = RecorderManager(
                "audio/pcm",
                2,
                128000,
                -1,
                QMultimedia.NormalQuality,
                QMultimedia.ConstantBitRateEncoding,
                "audio/x-wav")
            self.window().timer_label.hide()
            self.window().analyze_button.show()
        elif self.state == ButtonState.FINALIZED:
            print("retry")
            self.changeState(ButtonState.PLAYING)
            self.recorder_manager.setAudioInput(self.window().audio_combo_box.currentText())
            print(self.recorder_manager.audioInput())
            self.recorder_manager.record()
            self.recorder_manager.durationChanged.connect(self.handle_durationChanged)
            self.window().timer_label.setText("Time: 0")
            self.window().timer_label.show()
            self.window().analyze_button.hide()
            self.timer.start(10000)
        else:
            print("playing")
            self.changeState(ButtonState.PLAYING)
            print(self.recorder_manager.audioInput())
            self.recorder_manager.record()
            self.window().timer_label.show()
            self.window().analyze_button.hide()
            self.timer.start(10000)

    def changeState(self, buttonstate):
        self.setText(buttonstate.value)
        self.state = buttonstate

    def handle_durationChanged(self, progress):
        self.window().timer_label.setText("Time: " + str(progress // 1000))
