from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QSpinBox, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from ui.ui_main import Ui_MainWindow
from windows.window_connection_tcp import *
from .tcp_client_thread import TcpClientThread
from .window_calibration_raw import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建并显示连接窗口
        self.connect_window = None
        self.calibration_raw_windows = None
        self.tcp_thread = None
        self.algorithmListWidget.currentRowChanged.connect(self.display_para_page)

        self.show_connection_window()  # 首次打开显示连接窗口

        # 设置菜单connect
        self.actionconnect_board.triggered.connect(self.show_connection_window)
        self.actiondisconnect_board.triggered.connect(self.disconnect_tcp)

        # 设置菜单calibration raw
        self.actionraw.triggered.connect(self.show_calibration_window)
        # 设置log viewer
        self.clearLogButton.clicked.connect(self.logTextBrowser.clear)

        # BLC界面的滑动条与输入框联动
        self.manualOffsetBSpinBox.valueChanged.connect(self.manualOffsetBHorizontalSlider.setValue)
        self.manualOffsetGbSpinBox.valueChanged.connect(self.manualOffsetGbHorizontalSlider.setValue)
        self.manualOffsetGrSpinBox.valueChanged.connect(self.manualOffsetGrHorizontalSlider.setValue)
        self.manualOffsetRSpinBox.valueChanged.connect(self.manualOffsetRHorizontalSlider.setValue)

    def show_connection_window(self):
        if self.connect_window is None or not self.connect_window.isVisible():
            self.connect_window = ConnectionWindow(self)
            self.connect_window.connection_info_signal.connect(self.handle_connection_info)
            self.connect_window.show()
        else:
            self.connect_window.raise_()

    def show_calibration_window(self):
        if self.calibration_raw_windows is None or not self.calibration_raw_windows.isVisible():
            self.calibration_raw_windows = CalibrationWindow(self)
            self.calibration_raw_windows.show()
            self.calibration_raw_windows.log_info_signal.connect(self.display_message)
        else:
            self.calibration_raw_windows.raise_()

    @pyqtSlot(str, str)
    def handle_connection_info(self, ip, port):
        print(f"ip addr: {ip}, port: {port}")
        self.logTextBrowser.append(f"ip addr: {ip}, port: {port}")
        self.tcp_thread = TcpClientThread(ip, port)
        self.tcp_thread.message_received.connect(self.display_message)
        self.tcp_thread.connection_error.connect(self.handle_connection_error)
        self.tcp_thread.start()

    @pyqtSlot(str)
    def display_message(self, message):
        print(f"Receive: {message}")
        self.logTextBrowser.append(f"Receive: {message}")

    @pyqtSlot(int)
    def display_para_page(self, index):
        # 切换到对应的页面
        self.parameterStackedWidget.setCurrentIndex(index)

    def handle_connection_error(self, error):
        print(f"Connect Error: {error}")
        self.logTextBrowser.append(f"Connect Error: {error}")
        self.cleanup()

    def disconnect_tcp(self):
        print("Disconnecting TCP")
        self.logTextBrowser.append("Disconnecting TCP")
        self.cleanup()

    def closeEvent(self, event):
        self.cleanup()
        event.accept()

    def cleanup(self):
        if self.tcp_thread is not None:
            self.tcp_thread.stop()
            self.tcp_thread = None
