from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QSpinBox, QVBoxLayout, QTableWidgetItem, \
    QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from ui.ui_main import Ui_MainWindow
from windows.window_connection_tcp import *
from .tcp_client_thread import TcpClientThread
from .window_calibration_raw import *
from .windows_capture_http_jpg import *
from PyQt5.QtCore import pyqtSignal, Qt, QPointF, QRectF
import sys
from data.data import *
from datetime import datetime
import protobuf.protocols_pb2
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis, QChartView
from PyQt5.QtGui import QPainter, QBrush, QPen
from windows.gamma_plot_widget import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建并显示连接窗口
        self.__main_window_ui_init()

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

    def show_capture_http_jpg_window(self):
        if self.capture_http_jpg_window is None or not self.capture_http_jpg_window.isVisable():
            self.capture_http_jpg_window = CaptureHttpJpgWindow(self)
            self.capture_http_jpg_window.show()
            self.capture_http_jpg_window.destroyed.connect(self.on_capture_http_jpg_window_destroyed)
        else:
            self.capture_http_jpg_window.raise_()

    def on_capture_http_jpg_window_destroyed(self):
        self.capture_http_jpg_window = None

    def single_parameter_write(self):
        print("single write click, current page:{}".format(self.parameterStackedWidget.currentIndex()))
        if self.parameterStackedWidget.currentIndex() == 3:
            # 设置CCM
            if self.tcp_thread:
                ccm_parameters = protobuf.protocols_pb2.CCMParameters()
                ccm_parameters.ccm.extend(self.ccm_table.load_from_table(self.ccmTableWidget))
                ccm_parameters.enabled = True
                write_command = protobuf.protocols_pb2.WriteISPParametersCommand()
                write_command.ccm.CopyFrom(ccm_parameters)
                data_packet = protobuf.protocols_pb2.DataPacket()
                data_packet.write_isp_parameters_command.CopyFrom(write_command)
                serialized_command = data_packet.SerializeToString()
                self.tcp_thread.send_user_message(serialized_command)

    def __main_window_ui_init(self):
        # BLC界面的滑动条与输入框联动
        self.manualOffsetBSpinBox.valueChanged.connect(self.manualOffsetBHorizontalSlider.setValue)
        self.manualOffsetGbSpinBox.valueChanged.connect(self.manualOffsetGbHorizontalSlider.setValue)
        self.manualOffsetGrSpinBox.valueChanged.connect(self.manualOffsetGrHorizontalSlider.setValue)
        self.manualOffsetRSpinBox.valueChanged.connect(self.manualOffsetRHorizontalSlider.setValue)
        self.manualOffsetBHorizontalSlider.valueChanged.connect(self.manualOffsetBSpinBox.setValue)
        self.manualOffsetGbHorizontalSlider.valueChanged.connect(self.manualOffsetGbSpinBox.setValue)
        self.manualOffsetGrHorizontalSlider.valueChanged.connect(self.manualOffsetGrSpinBox.setValue)
        self.manualOffsetRHorizontalSlider.valueChanged.connect(self.manualOffsetRSpinBox.setValue)
        self.connect_window = None
        self.calibration_raw_windows = None
        self.capture_http_jpg_window = None
        self.tcp_thread = None
        self.algorithmListWidget.currentRowChanged.connect(self.display_para_page)
        self.ccm_table = CcmTableData()
        self.show_connection_window()  # 首次打开显示连接窗口
        self.connectIndicatorLabel.setStyleSheet("")
        # 设置菜单connect
        self.actionconnect_board.triggered.connect(self.show_connection_window)
        self.actiondisconnect_board.triggered.connect(self.disconnect_tcp)
        # 设置菜单calibration raw
        self.actionraw.triggered.connect(self.show_calibration_window)
        # 设置菜单capture http jpg
        self.actionhttp_jpg.triggered.connect(self.show_capture_http_jpg_window)
        # 设置log viewer
        self.clearLogButton.clicked.connect(self.logTextBrowser.clear)
        # 设置单个参数写入回调
        self.writeParamPushButton.clicked.connect(self.single_parameter_write)

        # gamma
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter number of points")
        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.generate_points)

        self.plot_widget = PlotWidget(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.confirm_button)
        self.layout.addWidget(self.plot_widget)

        self.gammaContainer = QWidget(self)
        self.gammaContainer.setLayout(self.layout)
        self.horizontalLayout_13.addWidget(self.gammaContainer)

    def generate_points(self):
        try:
            num_points = int(self.input_field.text())
            width = self.plot_widget.width()
            height = self.plot_widget.height()
            self.points = [
                QPointF(i * (width - 1) / (num_points - 1), height - (height / (num_points + 1)) * (i + 1))
                for i in range(num_points)
            ]
            self.plot_widget.setPoints(self.points)
        except ValueError:
            pass

    @pyqtSlot(str, str)
    def handle_connection_info(self, ip, port):
        print(f"ip addr: {ip}, port: {port}")
        self.logTextBrowser.append(f"ip addr: {ip}, port: {port}")
        self.tcp_thread = TcpClientThread(ip, port)
        self.tcp_thread.message_received.connect(self.display_message)
        self.tcp_thread.connection_error.connect(self.handle_connection_error)
        self.tcp_thread.connection_success.connect(self.handle_connection_success)
        self.tcp_thread.start()

    @pyqtSlot(str)
    def display_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp}: {message}"
        print(formatted_message)
        self.logTextBrowser.append(formatted_message)

    @pyqtSlot(int)
    def display_para_page(self, index):
        # 切换到对应的页面
        self.parameterStackedWidget.setCurrentIndex(index)

    def handle_connection_error(self, error):
        print(f"Connect Error: {error}")
        self.logTextBrowser.append(f"Connect Error: {error}")
        self.cleanup()
        self.connectIndicatorLabel.setStyleSheet("")

    def handle_connection_success(self):
        print("tcp connection success")
        self.connectIndicatorLabel.setStyleSheet("image: url(:/background/connect_success.png);")

    def disconnect_tcp(self):
        print("Disconnecting TCP")
        self.logTextBrowser.append("Disconnecting TCP")
        self.cleanup()
        self.connectIndicatorLabel.setStyleSheet("")

    def closeEvent(self, event):
        self.cleanup()
        event.accept()

    def cleanup(self):
        if self.tcp_thread is not None:
            self.tcp_thread.stop()
            self.tcp_thread = None
