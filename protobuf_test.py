import protobuf.protocols_pb2
import socket
import time

if __name__ == '__main__':
    capture_command = protobuf.protocols_pb2.CaptureImageCommand()
    capture_command.width = 1280
    capture_command.height = 720
    capture_command.format = protobuf.protocols_pb2.ImageFormat.RAW8

    data_packet = protobuf.protocols_pb2.DataPacket()
    data_packet.capture_image_command.CopyFrom(capture_command)

    # 序列化消息
    serialized_command = data_packet.SerializeToString()
    print("Serialized CaptureImageCommand:", serialized_command)

    # 反序列化消息
    new_data_packet = protobuf.protocols_pb2.DataPacket()
    new_data_packet.ParseFromString(serialized_command)

    # 获取反序列化的 CaptureImageCommand
    new_capture_command = new_data_packet.capture_image_command
    print("Deserialized CaptureImageCommand:")
    print(f"Width: {new_capture_command.width}")
    print(f"Height: {new_capture_command.height}")
    print(f"Format: {new_capture_command.format}")

    server_address = ('192.168.31.39', 8090)  # 服务器的地址和端口

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    try:
        # 发送序列化的消息
        sock.sendall(serialized_command)
    finally:
        sock.close()
    print("Message sent successfully")
