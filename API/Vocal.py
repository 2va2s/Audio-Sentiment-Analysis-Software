from pydantic import BaseModel
import json
import numpy as np


class Vocal(BaseModel):
    features: list[list[float]]

    # def process_mfccs(self, mfccs):
        # perform some processing on the MFCCs
        # for example, you could calculate the mean or standard deviation of each MFCC coefficient across all frames
        # mfccs_mean = np.mean(mfccs, axis=1)
        # mfccs_std = np.std(mfccs, axis=1)

        # create a dictionary containing the processed MFCCs
        # mfccs_dict = {"mfccs_mean": mfccs_mean.tolist(), "mfccs_std": mfccs_std.tolist()}

        # convert the dictionary to a JSON string
        # mfccs_json = json.dumps(mfccs_dict)

        # return the JSON string
        # return mfccs_json

