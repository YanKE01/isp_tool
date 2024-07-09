from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import pyqtSignal
import ui.ui_capture
import ui.ui_main
import requests
import numpy as np
import cv2
from PyQt5.QtGui import QImage, QPixmap
import protobuf.protocols_pb2


class CaptureImageWindow(QMainWindow, ui.ui_capture.Ui_MainWindow):
    capture_image_signal = pyqtSignal(bytes)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.captureImagePushButton.clicked.connect(self.onCaptureButtonClicked)

    def onCaptureButtonClicked(self):
        try:
            capture_command = protobuf.protocols_pb2.CaptureImageCommand()
            capture_command.width = 1920
            capture_command.height = 1080

            if self.captureFormatComboBox.currentIndex() == 0:
                capture_command.format = protobuf.protocols_pb2.ImageFormat.BGGR_RAW8
            elif self.captureFormatComboBox.currentIndex() == 1:
                capture_command.format = protobuf.protocols_pb2.ImageFormat.BGGR_RAW10
            data_packet = protobuf.protocols_pb2.DataPacket()
            data_packet.capture_image_command.CopyFrom(capture_command)
            serialized_command = data_packet.SerializeToString()

            print(f"Serialized Command Length: {len(serialized_command)}")  # Debugging info

            self.capture_image_signal.emit(serialized_command)
            print("Signal emitted successfully")  # Debugging info
        except Exception as e:
            print(f"Exception: {e}")  # Print any exceptions for debugging
