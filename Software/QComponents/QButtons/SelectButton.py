from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox


class SelectButton(QComboBox):
    deviceSelected = pyqtSignal(str)
    def __init__(self, items, stylesheet):
        super().__init__()
        for item in items:
            self.addItem(item)
        self.setFixedSize(300, 50)
        self.setStyleSheet(stylesheet)
        self.currentIndexChanged.connect(self.emitDeviceSelected)

    def emitDeviceSelected(self, index):
        self.deviceSelected.emit(self.itemText(index))