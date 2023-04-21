from PyQt5.QtWidgets import QMessageBox


class AnalyzeResultBox(QMessageBox):
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.happy_purcent = self.results["Predictions"][0][0] * 100
        self.angry_purcent = self.results["Predictions"][0][1] * 100
        self.neutral_purcent = self.results["Predictions"][0][2] * 100
        self.emotion = self.parse_emotion()
        self.setWindowTitle("Result of the analysis")
        self.setText("This record's emotion is : "+self.emotion)
        #self.setInformativeText("Choose audio experience name")
        self.setDetailedText(f'Neutral : {self.neutral_purcent}%, Angry : {self.angry_purcent}%, Happy : {self.happy_purcent}%')
        #self.setIcon(QMessageBox.Information)
        self.addButton("Save", QMessageBox.AcceptRole)
        self.addButton("Discard", QMessageBox.RejectRole)
        self.setDefaultButton(QMessageBox.Ok)
        self.setEscapeButton(QMessageBox.Cancel)
        self.setStyleSheet("QLabel{min-width: 600px;}")

    def parse_emotion(self):
        if self.results["Predictions"][0][0] > self.results["Predictions"][0][1] and self.results["Predictions"][0][0] > self.results["Predictions"][0][2]:
            return "Happy"
        elif self.results["Predictions"][0][1] > self.results["Predictions"][0][2] and self.results["Predictions"][0][1] > self.results["Predictions"][0][0]:
            return "Angry"
        else:
            return "Neutral"