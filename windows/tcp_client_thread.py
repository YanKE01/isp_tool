from PyQt5.QtCore import QThread, pyqtSignal
import socket
import struct
import protobuf.protocols_pb2

class TcpClientThread(QThread):
    message_received = pyqtSignal(str)
    connection_error = pyqtSignal(str)
    connection_success = pyqtSignal()
    packet_image_received = pyqtSignal(protobuf.protocols_pb2.ImageResponse)

    def __init__(self, ip, port, parent=None):
        super().__init__(parent)
        self.ip = ip
        self.port = port
        self.running = True
        self.sock = None
        self.buffer = b''

    def run(self):
        try:
            print(f"Trying to connect to {self.ip}:{self.port}")
            self.sock = socket.create_connection((self.ip, int(self.port)), timeout=1000)
            print(f"Connected to {self.ip}:{self.port}")
            self.connection_success.emit()
            while self.running:
                try:
                    data = self.sock.recv(4096)
                    if data:
                        self.buffer += data
                        while len(self.buffer) >= 4:
                            packet_size = struct.unpack('!I', self.buffer[:4])[0]
                            if len(self.buffer) >= packet_size + 4:
                                packet_data = self.buffer[4:4 + packet_size]
                                self.buffer = self.buffer[4 + packet_size:]
                                print("Finished")
                                # decode image
                                data_packet = protobuf.protocols_pb2.DataPacket()
                                data_packet.ParseFromString(packet_data)

                                if data_packet.HasField("image_response"):
                                    print("data packet:image_response")
                                    image_response = data_packet.image_response
                                    self.packet_image_received.emit(image_response)
                                self.buffer = b''
                            else:
                                break
                    else:
                        print("Connection closed by server")
                        break
                except socket.timeout:
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

    def sendMessage(self, message: str):
        if self.sock:
            try:
                self.sock.sendall(message)
                print(f"Sent: {message}")
            except Exception as e:
                self.connection_error.emit(str(e))

    def stop(self):
        self.running = False
        if self.sock:
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass  # 套接字已经关闭
            self.sock.close()
        self.wait()
