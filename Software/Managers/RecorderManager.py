import os
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

from Software.States.ButtonState import ButtonState

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class RecorderManager(QAudioRecorder):
    def __init__(self, codec, sample_rates, bit_rate, channel_count, quality, encoding_mode, selected_container):
        super().__init__()
        self.setAudioInput(self.audioInputs()[0])
        settings = QAudioEncoderSettings()
        settings.setCodec(codec)
        settings.setSampleRate(sample_rates)
        settings.setBitRate(bit_rate)
        settings.setChannelCount(channel_count)
        settings.setQuality(quality)
        settings.setEncodingMode(encoding_mode)
        self.setEncodingSettings(settings, QVideoEncoderSettings(), selected_container)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(CURRENT_DIR, os.path.realpath("./Records/" + dt_string))
        print(filename)
        self.setOutputLocation(QUrl.fromLocalFile(filename))

        """
        json du resultat de l'analyse
        {
            "file":"2023-04-17-17-55-18",
            "result":"angry",
            "paramètres": {
                "chroma":"1",
            }
        }"""