from PyQt5.QtWidgets import QMessageBox


class AnalyzeResultBox(QMessageBox):
    def __init__(self, results, button):
        """
        Initiate AnalyzeResultBox with results of Emotion Analysis of the voice record
        :param results:
        :param button:
        """
        super().__init__()
        self.results = results
        self.play_button = button

        # Extract probabilities for different emotions from the results dictionary
        self.happy_prob, self.angry_prob, self.neutral_prob = self.results["Predictions"][0]

        # Determine the emotion with the highest probability using the parse_emotion method
        self.emotion = self.parse_emotion()

        # Set the window title and message text for the message box
        self.setWindowTitle("Result of the analysis")
        self.setText("This record's emotion is : " + self.emotion)

        # Set the detailed message text to show the probability for each emotion
        self.setDetailedText(
            f'Neutral : {self.neutral_prob * 100}%, Angry : {self.angry_prob * 100}%, Happy : {self.happy_prob * 100}%')

        # Add two buttons to the message box: "Save" and "Discard"
        self.addButton("Save", QMessageBox.AcceptRole)
        self.addButton("Discard", QMessageBox.RejectRole)

        # Set the default button to be "OK" and the escape button to be "Cancel"
        self.setDefaultButton(QMessageBox.Ok)
        self.setEscapeButton(QMessageBox.Cancel)

        # Set the style sheet to adjust the minimum width of the label
        self.setStyleSheet("QLabel{min-width: 600px;}")

    # Define a method to determine the emotion with the highest probability
    def parse_emotion(self):
        if self.happy_prob > self.angry_prob and self.happy_prob > self.neutral_prob:
            return "Happy"
        elif self.angry_prob > self.neutral_prob:
            return "Angry"
        else:
            return "Neutral"
