import protobuf.protocols_pb2

if __name__ == '__main__':
    capture_command = protobuf.protocols_pb2.CaptureImageCommand()
    capture_command.width = 1920
    capture_command.height = 1080

    # 序列化消息
    serialized_command = capture_command.SerializeToString()
    print("Serialized CaptureImageCommand:", serialized_command)

    # 反序列化消息
    deserialized_command = protobuf.protocols_pb2.CaptureImageCommand()
    deserialized_command.ParseFromString(serialized_command)
    print("Width:", deserialized_command.width)
    print("Height:", deserialized_command.height)