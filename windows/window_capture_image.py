from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem, QMainWindow
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QPointF, QByteArray
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
            data_packet = protobuf.protocols_pb2.DataPacket()
            data_packet.capture_image_command.CopyFrom(capture_command)
            serialized_command = data_packet.SerializeToString()

            self.capture_image_signal.emit(serialized_command)
        except Exception as e:
            print(f"Exception: {e}")  # Print any exceptions for debugging

    @pyqtSlot(protobuf.protocols_pb2.ImageResponse)
    def decodeImageResponse(self, image_response):
        print("----------------decodeImageResponse start--------------------\n")
        print(f"Status: {image_response.status}")
        print(f"Message: {image_response.message}")
        print(f"Width: {image_response.width}")
        print(f"Height: {image_response.height}")
        print(f"Format: {image_response.format}")

        if image_response.format == protobuf.protocols_pb2.ImageFormat.BGGR_RAW8:
            image_array = np.frombuffer(image_response.image_data, dtype="uint8").reshape(image_response.height,
                                                                                          image_response.width, 1)
            self.cameraInfoLabel.setText("{}x{},BGGR_RAW8".format(image_response.width, image_response.height))
        elif image_response.format == protobuf.protocols_pb2.ImageFormat.BGGR_RAW10:
            image_array = np.frombuffer(image_response.image_data, dtype="uint16").reshape(image_response.height,
                                                                                           image_response.width, 1)
            self.cameraInfoLabel.setText("{}x{},BGGR_RAW10".format(image_response.width, image_response.height))

        rgb_img = cv2.cvtColor(image_array, cv2.COLOR_BAYER_BGGR2RGB)
        rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)

        height = rgb_img.shape[1]
        width = rgb_img.shape[0]

        frame = QImage(rgb_img, height, width, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.captureImageGraphicsView.setScene(scene)
        self.captureImageGraphicsView.fitInView(item, 1)
        self.captureImageGraphicsView.show()

        print("----------------decodeImageResponse end--------------------\n")

    def closeEvent(self, event):
        self.captureImageGraphicsView.setScene(None)
        self.cameraInfoLabel.setText("")
        event.accept()  # Accept the event to close the window
