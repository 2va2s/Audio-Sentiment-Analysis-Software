import os
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

from Software.States.ButtonState import ButtonState

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class RecorderManager(QAudioRecorder):
    def __init__(self):
        super().__init__()
        self.setAudioInput(self.audioInputs()[0])
        settings = QAudioEncoderSettings()
        settings.setCodec("audio/pcm")
        settings.setSampleRate(8000)
        settings.setBitRate(128000)
        settings.setChannelCount(-1)
        settings.setQuality(QMultimedia.NormalQuality)
        settings.setEncodingMode(QMultimedia.ConstantBitRateEncoding)
        self.setEncodingSettings(settings, QVideoEncoderSettings(), "audio/x-wav")
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        self.filename = os.path.join(CURRENT_DIR, os.path.realpath("./Records/" + dt_string))
        self.test_file = QUrl.fromLocalFile(self.filename)
        self.setOutputLocation(QUrl.fromLocalFile(self.filename))