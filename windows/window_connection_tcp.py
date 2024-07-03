from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
import ui.ui_connection_tcp


class ConnectionWindow(QMainWindow, ui.ui_connection_tcp.Ui_MainWindow):
    connection_info_signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectTcpButton.clicked.connect(self.onConnectionButtonClicked)
        self.parent = parent

    def onConnectionButtonClicked(self):
        ip_address = self.ipAddrLineEdit.text()
        port_number = self.ipPortLineEdit.text()

        if not ip_address or not port_number:
            QMessageBox.warning(self, "Input Error", "Please enter a valid IP address and port number")
        else:
            self.connection_info_signal.emit(ip_address, port_number)
            self.close()
