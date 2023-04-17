from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QMultimedia
from PyQt5.QtWidgets import QPushButton

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
        self.timer.setInterval(1000)  # interval of 1 second
        self.timer.timeout.connect(self.handle_timeout)

    def handle_timeout(self):
        print("timer timeout")
        self.timer.stop()
        self.recorder_manager.stop()
        self.changeState(ButtonState.FINALIZED)
    def click(self):
        if self.state == ButtonState.PLAYING:
            print("stop")
            self.timer.stop()
            self.changeState(ButtonState.FINALIZED)
            self.recorder_manager.stop()
        else:
            print("playing or retry")
            self.changeState(ButtonState.PLAYING)
            self.recorder_manager.record()
            self.timer.start(10000)

    def changeState(self, buttonstate):
        self.setText(buttonstate.value)
        self.state = buttonstate

