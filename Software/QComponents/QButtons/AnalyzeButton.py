import json

import librosa
import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QPushButton, QMessageBox

from Software.QComponents.AnalyzeResultBox import AnalyzeResultBox


class AnalyzeButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.features = None
        self.setFixedSize(145, 52)
        self.setStyleSheet("border-radius : 26px; font-size:30px; background-color: #04A91E; color: white;")
        self.setText("✓")
        self.clicked.connect(self.click)

    def click(self):
        print("appel model")
        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.NoButton)
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        msgBox.setText("Please wait for the analysis...")
        self.msgBox = msgBox  # Store the message box as an instance variable
        self.msgBox.show()
        self.analyze()
    def analyze(self):
        self.features = self.extract_feature("./Records/2023-04-21-13-19-39.wav")
        predicted_vector = self.window().model.predict(self.features)
        self.results = {"Predictions": predicted_vector.tolist()}
        self.close_msgBox()

    def extract_feature(self, file_name):
        try:
            audio_data, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
            mfccs = librosa.feature.mfcc(y=audio_data.flatten(), sr=sample_rate, n_mfcc=40)
            mfccsscaled = np.mean(mfccs.T, axis=0)

        except Exception as e:
            print("Error encountered while parsing file: ", file_name)
            print(e)
            return None, None

        return np.array([mfccsscaled])
    def close_msgBox(self):
        self.msgBox.done(0)
        print("result : coucou")
        resultBox = AnalyzeResultBox(self.results)
        result = resultBox.exec_()
        if result == QMessageBox.AcceptRole:
            print("OK clicked")
        elif result == QMessageBox.RejectRole:
            print("Cancel clicked")
