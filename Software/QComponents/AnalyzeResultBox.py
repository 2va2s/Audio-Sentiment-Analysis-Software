from PyQt5.QtWidgets import QMessageBox


class AnalyzeResultBox(QMessageBox):
    def __init__(self, emotion, neutral_purcent, angry_purcent, happy_purcent):
        super().__init__()
        self.setWindowTitle("Result of the analysis")
        self.setText("This record's emotion is : "+emotion)
        #self.setInformativeText("Choose audio experience name")
        self.setDetailedText(f'Neutral : {neutral_purcent}%, Angry : {angry_purcent}%, Happy : {happy_purcent}%')
        #self.setIcon(QMessageBox.Information)
        self.addButton("Save", QMessageBox.AcceptRole)
        self.addButton("Discard", QMessageBox.RejectRole)
        self.setDefaultButton(QMessageBox.Ok)
        self.setEscapeButton(QMessageBox.Cancel)
        self.setStyleSheet("QLabel{min-width: 600px;}")