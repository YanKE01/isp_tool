from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QSpinBox, QVBoxLayout, QTableWidgetItem, \
    QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QGraphicsItem, QMainWindow, QHeaderView, QLineEdit
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QPointF
from datetime import datetime
import ui.ui_main
import windows.window_connection_tcp
import windows.tcp_client_thread
from tuning.ccm_parameter import *
from utils.utils import *
import protobuf.protocols_pb2
from windows.gamma_plot_widget import PlotWidget
import windows.window_capture_image


class MainWindow(QMainWindow, ui.ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tcp_connection_window = None
        self.capture_image_window = None
        self.tcp_thread = None
        self.gamma_plot_widget = None
        self.gamma_point_num = 16
        self.points = None
        self.utils = Utils()
        self.ccm_parameter = CCMParameter()
        self.showTcpConnectionWindow()
        self.singalSlotInit()
        self.widgetInit()

    def widgetInit(self):
        self.ispParameterstackedWidget.setCurrentIndex(0)

        # ccm Form Size Adaptation
        header = self.ccmParamTable.horizontalHeader()
        for col in range(self.ccmParamTable.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)
        vertical_header = self.ccmParamTable.verticalHeader()
        for row in range(self.ccmParamTable.rowCount()):
            vertical_header.setSectionResizeMode(row, QHeaderView.Stretch)

        # gamma plot
        self.gammaPointNumberConfirmButton.clicked.connect(self.generate_points)
        self.gamma_plot_widget = PlotWidget(x_range=(0, 255), y_range=(0, 255))
        self.horizontalLayout_2.addWidget(self.gamma_plot_widget)
        self.gammaPonitsNumberlineEdit.setText(str(self.gamma_point_num))

    def generate_points(self):
        try:
            self.gamma_point_num = int(self.gammaPonitsNumberlineEdit.text())
            width = self.gamma_plot_widget.width()
            height = self.gamma_plot_widget.height()

            self.points = [
                QPointF(i * (width - 1) / (self.gamma_point_num - 1),
                        height - (height / (self.gamma_point_num + 1)) * (i + 1))
                for i in range(self.gamma_point_num)
            ]
            self.gamma_plot_widget.setPoints(self.points)
        except ValueError:
            pass

    def showTcpConnectionWindow(self):
        if self.tcp_connection_window is None:
            self.tcp_connection_window = windows.window_connection_tcp.ConnectionWindow(self)
            self.tcp_connection_window.connection_info_signal.connect(self.hanleTcpConnectWindowsInfo)
        if not self.tcp_connection_window.isVisible():
            self.tcp_connection_window.show()
        else:
            self.tcp_connection_window.raise_()

    def showCaptureImageWindow(self):
        if self.capture_image_window is None:
            self.capture_image_window = windows.window_capture_image.CaptureImageWindow(self)
            self.capture_image_window.capture_image_signal.connect(self.handleCaptureImage)
            if self.tcp_thread:
                self.tcp_thread.packet_image_received.connect(self.capture_image_window.decodeImageResponse)
        if not self.capture_image_window.isVisible():
            self.capture_image_window.show()
        else:
            self.capture_image_window.raise_()

    def singalSlotInit(self):
        self.actionconnect_board.triggered.connect(
            self.showTcpConnectionWindow)  # Press Connect Board in the menu bar to open the tcp connection window
        self.ispListWidget.currentRowChanged.connect(self.handleIspListChange)
        self.actiondisconnect_board.triggered.connect(self.cleanTcpConnection)
        self.writeParameterButton.clicked.connect(self.singleParameterWrite)
        self.actionimage.triggered.connect(self.showCaptureImageWindow)
        self.searchButton.clicked.connect(self.handleSearchButton)
        self.readParameterButton.clicked.connect(self.singleParameterRead)

    def cleanTcpConnection(self):
        if self.tcp_thread is not None:
            self.tcp_thread.stop()
            self.tcp_thread = None

    def closeEvent(self, event):
        self.cleanTcpConnection()
        event.accept()

    def singleParameterWrite(self):
        print("single parameter write,current page:{}".format(self.ispParameterstackedWidget.currentIndex()))
        if self.ispParameterstackedWidget.currentIndex() == 0:
            print(self.gamma_plot_widget.getRealPoints())
            if len(self.gamma_plot_widget.getRealPoints()) > 0:
                gamma_parameters = protobuf.protocols_pb2.GammaParameters()
                gamma_parameters.gamma.extend(self.gamma_plot_widget.getRealPoints())
                gamma_parameters.enabled = True
                write_command = protobuf.protocols_pb2.WriteISPParametersCommand()
                write_command.gamma.CopyFrom(gamma_parameters)
                data_packet = protobuf.protocols_pb2.DataPacket()
                data_packet.write_isp_parameters_command.CopyFrom(write_command)
                serialized_command = data_packet.SerializeToString()
                if self.tcp_thread:
                    self.tcp_thread.sendMessage(serialized_command)
        elif self.ispParameterstackedWidget.currentIndex() == 1:
            # Handling of CCM separate writes
            if self.tcp_thread:
                ccm_parameter_protobuf = protobuf.protocols_pb2.CCMParameters()
                ccm_parameter_protobuf.ccm.extend(self.ccm_parameter.loadFromTable(self.ccmParamTable))
                ccm_parameter_protobuf.enabled = True
                write_command = protobuf.protocols_pb2.WriteISPParametersCommand()
                write_command.ccm.CopyFrom(ccm_parameter_protobuf)
                data_packet = protobuf.protocols_pb2.DataPacket()
                data_packet.write_isp_parameters_command.CopyFrom(write_command)
                serialized_command = data_packet.SerializeToString()
                if self.tcp_thread:
                    self.tcp_thread.sendMessage(serialized_command)

    def singleParameterRead(self):
        print("single parameter read")
        if self.ispParameterstackedWidget.currentIndex() == 0:
            pass
        elif self.ispParameterstackedWidget.currentIndex() == 1:
            # Read ccm parameters
            read_command = protobuf.protocols_pb2.ReadISPParametersCommand()
            read_command.parameter_type = protobuf.protocols_pb2.ISPParameterType.CCM
            data_packet = protobuf.protocols_pb2.DataPacket()
            data_packet.read_isp_parameters_command.CopyFrom(read_command)
            serialized_read_command = data_packet.SerializeToString()
            if self.tcp_thread:
                self.tcp_thread.sendMessage(serialized_read_command)

    @pyqtSlot(str, str)
    def hanleTcpConnectWindowsInfo(self, ip_addr, ip_port):
        message = f"Board address:{ip_addr}:{ip_port}"
        formatted_message = self.utils.format_message(message)
        self.systemLogTextEdit.append(formatted_message)
        self.tcp_thread = windows.tcp_client_thread.TcpClientThread(ip_addr, ip_port)
        self.tcp_thread.connection_error.connect(self.handleTcpConnectionError)
        self.tcp_thread.connection_success.connect(self.handleTcpConnectSuccess)
        self.tcp_thread.start()

    @pyqtSlot(str)
    def displaySystemLog(self, message):
        formatted_message = self.utils.format_message(message)
        self.systemLogTextEdit.append(formatted_message)

    @pyqtSlot(str)
    def handleTcpConnectionError(self, error):
        formatted_message = self.utils.format_message(error)
        self.systemLogTextEdit.append(formatted_message)
        self.cleanTcpConnection()
        self.connectStatusLabel.setStyleSheet("background-color: rgb(255, 0, 0);")

    @pyqtSlot()
    def handleTcpConnectSuccess(self):
        formatted_message = self.utils.format_message("Connected board")
        self.connectStatusLabel.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.systemLogTextEdit.append(formatted_message)

    @pyqtSlot(int)
    def handleIspListChange(self, index):
        self.ispParameterstackedWidget.setCurrentIndex(index)

    @pyqtSlot(bytes)
    def handleCaptureImage(self, command):
        formatted_message = self.utils.format_message("Capture image")
        self.systemLogTextEdit.append(formatted_message)
        if self.tcp_thread:
            self.tcp_thread.sendMessage(command)
        pass

    def handleSearchButton(self):
        print("search:{}".format(self.searchLineEdit.text()))
