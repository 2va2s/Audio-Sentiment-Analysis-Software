import os
import shutil

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
source_folder = CURRENT_DIR + "\\RAVDESS_data\\"
destination_folder = {"neutral": "010203", "angry": "05"}


def classifier1():
    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        for name, value in destination_folder.items():
            if file_name[6:8] in value:
                # copy only files
                print('copied', file_name)
                shutil.copy(source, CURRENT_DIR + "\\Audio_data\\Classification2\\" + name + "\\")
                break


classifier1()
