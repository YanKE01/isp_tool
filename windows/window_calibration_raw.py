from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSignal
import ui.ui_calibration
from PyQt5.QtCore import pyqtSignal


class CalibrationWindow(QMainWindow, ui.ui_calibration.Ui_MainWindow):
    log_info_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.actionopen_file.triggered.connect(self.openFileDialog)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Text Files (*.txt)',
                                                  options=options)
        if fileName:
            print(f'Selected file: {fileName}')
            self.log_info_signal.emit(f'Selected file: {fileName}')
