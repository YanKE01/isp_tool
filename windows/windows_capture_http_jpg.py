from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal, QUrl
import ui.ui_capture_http_jpg
import time


class CaptureHttpJpgWindow(QMainWindow, ui.ui_capture_http_jpg.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.httpJpgCapturePushButton.clicked.connect(self.show_jpg)

    def show_jpg(self):
        self.webEngineView.setHtml('')  # 清空内容
        if self.httpJpgPicRadioButton.isChecked():
            self.webEngineView.setUrl(QUrl('http://192.168.31.39/pic'))
            print("pic radio")
        elif self.httpJpgStreamRadioButton.isChecked():
            self.webEngineView.setUrl(QUrl('http://192.168.31.39/stream'))
            print("stream radio")

    def closeEvent(self, event):
        self.webEngineView.setHtml('')  # 清空内容
        self.webEngineView.deleteLater()
        event.accept()
        self.deleteLater()
