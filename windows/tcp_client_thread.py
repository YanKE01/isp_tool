from PyQt5.QtCore import QThread, pyqtSignal
import socket

class TcpClientThread(QThread):
    message_received = pyqtSignal(str)
    connection_error = pyqtSignal(str)

    def __init__(self, ip, port, parent=None):
        super().__init__(parent)
        self.ip = ip
        self.port = port
        self.running = True
        self.sock = None

    def run(self):
        try:
            print(f"Trying to connect to {self.ip}:{self.port}")
            self.sock = socket.create_connection((self.ip, int(self.port)), timeout=10)
            self.sock.settimeout(5)  # 设置接收数据的超时时间
            print(f"Connected to {self.ip}:{self.port}")
            while self.running:
                try:
                    data = self.sock.recv(1024)
                    if data:
                        message = data.decode('utf-8')
                        self.message_received.emit(message)
                    else:
                        print("Connection closed by server")
                        break
                except socket.timeout:
                    # 超时未收到数据，继续等待
                    continue
                except Exception as e:
                    self.connection_error.emit(str(e))
                    break
        except Exception as e:
            self.connection_error.emit(str(e))
        finally:
            if self.sock:
                try:
                    self.sock.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass  # 套接字已经关闭
                self.sock.close()

    def stop(self):
        self.running = False
        if self.sock:
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass  # 套接字已经关闭
            self.sock.close()
        self.wait()
