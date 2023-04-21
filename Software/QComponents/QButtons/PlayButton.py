# Import required PyQt5 libraries
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QPushButton

# Import custom classes
from Software.Managers.RecorderManager import RecorderManager
from Software.States.ButtonState import ButtonState


class PlayButton(QPushButton):
    """
    PlayButton is the class of the play button that records the voice,
    have three states as : INACTIVE with "Record text", PLAYING with "STOP" text, FINALIZING with "RETRY" text and Analyze button
    """
    def __init__(self):
        super().__init__()
        self.state = ButtonState.INACTIVE
        self.setText(self.state.value)
        self.setFixedSize(100, 100)
        self.setStyleSheet("border-radius : 50px; border: 3 px solid white; background-color: red;color: white;")
        self.clicked.connect(self.click)
        self.recorder_manager = RecorderManager()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle_timeout)
        self.recorder_manager.durationChanged.connect(self.handle_duration_changed)

    def handle_timeout(self):
        print("timer timeout")
        self.timer.stop()
        self.recorder_manager.stop()
        self.window().timer_label.hide()
        self.change_state(ButtonState.FINALIZED)
        self.window().analyze_button.show()
        self.recorder_manager = RecorderManager()

    def click(self):
        if self.state == ButtonState.PLAYING:
            self.timer.stop()
            self.change_state(ButtonState.FINALIZED)
            self.recorder_manager.stop()
            self.recorder_manager = RecorderManager()
            self.window().timer_label.hide()
            self.window().analyze_button.show()
        elif self.state == ButtonState.FINALIZED or self.state == ButtonState.INACTIVE:
            self.change_state(ButtonState.PLAYING)
            self.recorder_manager.setAudioInput(self.window().audio_combo_box.currentText())
            self.recorder_manager.record()
            self.recorder_manager.durationChanged.connect(self.handle_duration_changed)
            self.window().timer_label.setText("Time: 0")
            self.window().timer_label.show()
            self.window().analyze_button.hide()
            self.timer.start(10000)
    def change_state(self, buttonstate):
        self.setText(buttonstate.value)
        self.state = buttonstate

    def handle_duration_changed(self, progress):
        self.window().timer_label.setText("Time: " + str(progress // 1000))
