import glob  # Library for finding files using patterns
import json  # Library for working with JSON data
import os  # Library for interacting with the operating system

import librosa  # Library for audio processing
import numpy as np  # Library for working with arrays
from PyQt5.QtCore import Qt  # Library for creating PyQt applications
from PyQt5.QtWidgets import QPushButton, QMessageBox, QFileDialog  # Library for creating PyQt applications

from Software.QComponents.AnalyzeResultBox import AnalyzeResultBox  # Importing a custom PyQt component
from Software.States.ButtonState import ButtonState  # Importing a custom PyQt component


class AnalyzeButton(QPushButton):  # Defining a custom PyQt button component
    def __init__(self):
        super().__init__()
        self.features = None  # Variable for storing audio features
        self.setFixedSize(145, 52)  # Setting button size
        self.setStyleSheet("border-radius : 26px; font-size:30px; background-color: #04A91E; color: white;")  # Setting button style
        self.setText("✓")  # Setting button text
        self.clicked.connect(self.click)  # Connecting button click event to click method

    def click(self):
        self.msg_box = QMessageBox()  # Creating a message box for displaying analysis progress
        self.msg_box.setStandardButtons(QMessageBox.NoButton)  # Removing standard buttons from message box
        self.msg_box.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)  # Setting window flags for message box
        self.msg_box.setText("Please wait for the analysis...")  # Setting text for message box
        self.msg_box.show()  # Displaying message box
        self.analyze()  # Calling the analyze method

    def analyze(self):
        folder_path = "./Records/"  # Path to folder containing audio files
        file_type = "/*wav"  # File type to look for
        files = glob.glob(folder_path + file_type)  # Finding audio files in folder
        self.last_file = max(files, key=os.path.getctime)  # Getting the latest audio file
        self.features = self.extract_feature(self.last_file)  # Extracting audio features from latest audio file
        predicted_vector = self.window().model.predict(self.features)  # Predicting the emotion using the audio features
        self.results = {"Predictions": predicted_vector.tolist()}  # Storing the predicted emotion results in a dictionary
        self.close_msg_box()  # Closing the progress message box

    def extract_feature(self, file_name):
        try:
            audio_data, sample_rate = librosa.load(file_name, res_type="kaiser_fast")  # Loading audio data from file
            mfccs = librosa.feature.mfcc(y=audio_data.flatten(), sr=sample_rate, n_mfcc=40)  # Extracting Mel-frequency cepstral coefficients (MFCCs) from audio data
            mfccs_scaled = np.mean(mfccs.T, axis=0)  # Scaling MFCCs and taking the mean

        except Exception as e:
            print("Error encountered while parsing file: ", file_name)  # Printing error message if file parsing fails
            print(e)
            return None

        return np.array([mfccs_scaled])  # Returning the scaled MFCCs as a NumPy array

    def close_msg_box(self):
        # Close the message box
        self.msg_box.done(0)

        # Create an instance of AnalyzeResultBox with the analysis results and button object
        result_box = AnalyzeResultBox(self.results, self.window().button)

        # Display the dialog and store the user's response in the 'result' variable
        result = result_box.exec_()

        # If the user clicked 'Save' button
        if result == QMessageBox.AcceptRole:
            # Open a file dialog to prompt the user for a file name and location to save the results
            filename, _ = QFileDialog.getSaveFileName(None, "Save Results", "", "JSON Files (*.json)")

            # If a valid file name was provided
            if filename:
                # Create a dictionary containing the analysis results and file information
                data = {
                    "happy_percent": result_box.happy_prob*100,
                    "angry_percent": result_box.angry_prob*100,
                    "neutral_percent": result_box.neutral_prob*100,
                    "emotion": result_box.emotion,
                    "record_file_path": self.last_file
                }

                # Write the dictionary to the specified file in JSON format
                with open(filename, "w") as f:
                    json.dump(data, f)

            # Change the state of the button object to 'inactive' and hide the dialog
            self.window().button.changeState(ButtonState.INACTIVE)
            self.hide()

        # If the user clicked 'Discard' button or closed the dialog
        elif result == QMessageBox.RejectRole:
            # Change the state of the button object to 'inactive' and hide the dialog
            self.window().button.changeState(ButtonState.INACTIVE)
            self.hide()
