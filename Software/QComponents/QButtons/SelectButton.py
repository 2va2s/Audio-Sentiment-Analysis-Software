from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox


class SelectButton(QComboBox):
    """
    Define the constructor for the SelectButton class with all audiodevices from the computer of the user
    """
    device_selected = pyqtSignal(str)

    def __init__(self, items, stylesheet):
        super().__init__()
        for item in items:
            self.addItem(item)
        self.setFixedSize(300, 50)
        self.setStyleSheet(stylesheet)
        self.currentIndexChanged.connect(self.emit_device_selected)

    def emit_device_selected(self, index):
        """
        Change device_selected to the device selected's name
        :param index:
        :return:
        """
        self.device_selected.emit(self.itemText(index))
