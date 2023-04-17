from PyQt5.QtWidgets import QComboBox


class SelectButton(QComboBox):
    def __init__(self, items):
        super().__init__()
        for item in items:
            self.addItem(item)