from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QPushButton, QMessageBox

from Software.QComponents.AnalyzeResultBox import AnalyzeResultBox


class AnalyzeButton(QPushButton):
    def __init__(self):
        super().__init__()
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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_msgBox)
        self.timer.start(2000)

    def close_msgBox(self):
        self.msgBox.done(0)
        self.timer.stop()
        print("result : coucou")
        resultBox = AnalyzeResultBox("Happy", 0.54,0.46,99)
        result = resultBox.exec_()
        if result == QMessageBox.AcceptRole:
            print("OK clicked")
        elif result == QMessageBox.RejectRole:
            print("Cancel clicked")
