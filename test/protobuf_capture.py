import protobuf.protocols_pb2 as protocols_pb2
import socket
import threading
import cv2
import numpy as np


def send_message(sock, message):
    try:
        sock.sendall(message)
        print("Message sent successfully")
    except Exception as e:
        print(f"Send error: {e}")


def receive_message(sock):
    try:
        # 使用一个缓冲区来接收所有的数据
        received_data = bytearray()
        while True:
            packet = sock.recv(4096)
            if not packet:
                break
            received_data.extend(packet)

        # 在这里你可以对 received_data 进行后续处理
        print(f"Total received data length: {len(received_data)}")
        data_packet = protocols_pb2.DataPacket()
        data_packet.ParseFromString(bytes(received_data))
        if data_packet.HasField("image_response"):
            image_response = data_packet.image_response
            print("Deserialized ImageResponse:")
            print(f"Status: {image_response.status}")
            print(f"Message: {image_response.message}")
            print(f"Image Data Length: {len(image_response.image_data)}")
            print(f"Width: {image_response.width}")
            print(f"Height: {image_response.height}")
            print(f"Format: {image_response.format}")
            # process image
            image_array = np.frombuffer(image_response.image_data, dtype="uint8").reshape(1080,
                                                                                         1920, 1)
            rgb_img = cv2.cvtColor(image_array, cv2.COLOR_BAYER_BGGR2RGB)
            cv2.imwrite("record.jpg", rgb_img)

    except Exception as e:
        print(f"Receive error: {e}")
    finally:
        sock.close()
        print("Connection closed")


if __name__ == '__main__':
    capture_command = protocols_pb2.CaptureImageCommand()
    capture_command.width = 1920
    capture_command.height = 1080
    capture_command.format = protocols_pb2.ImageFormat.RGB565

    data_packet = protocols_pb2.DataPacket()
    data_packet.capture_image_command.CopyFrom(capture_command)

    # 序列化消息
    serialized_command = data_packet.SerializeToString()
    print("Serialized CaptureImageCommand:", serialized_command)

    # 反序列化消息
    new_data_packet = protocols_pb2.DataPacket()
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

    # 创建发送消息的线程
    send_thread = threading.Thread(target=send_message, args=(sock, serialized_command))
    # 创建接收消息的线程
    receive_thread = threading.Thread(target=receive_message, args=(sock,))

    # 启动线程
    send_thread.start()
    receive_thread.start()

    # 等待发送线程完成
    send_thread.join()

    # 发送完成后关闭写部分但继续接收消息
    sock.shutdown(socket.SHUT_WR)

    # 等待接收线程完成
    receive_thread.join()

    sock.close()
