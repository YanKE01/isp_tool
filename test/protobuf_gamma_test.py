import protobuf.protocols_pb2
import socket

# 创建并设置GammaParameters
gamma_parameters = protobuf.protocols_pb2.GammaParameters()
gamma_parameters.gamma.extend([0, 22, 62, 83, 101, 118, 134, 150, 164, 178, 192, 205, 218, 231, 243, 255])
gamma_parameters.enabled = True

# 创建WriteISPParametersCommand并设置GammaParameters
write_command = protobuf.protocols_pb2.WriteISPParametersCommand()
write_command.gamma.CopyFrom(gamma_parameters)

# 创建DataPacket并设置WriteISPParametersCommand
data_packet = protobuf.protocols_pb2.DataPacket()
data_packet.write_isp_parameters_command.CopyFrom(write_command)

# 序列化消息
serialized_command = data_packet.SerializeToString()
print(serialized_command)

# 服务器的地址和端口
server_address = ('192.168.31.39', 8090)

# 创建套接字并连接到服务器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
try:
    # 发送序列化的消息
    sock.sendall(serialized_command)
finally:
    sock.close()
print("Message sent successfully")

# 解析收到的数据
data_packet = protobuf.protocols_pb2.DataPacket()
data_packet.ParseFromString(serialized_command)

# 检查消息中包含的具体消息类型并解析
if data_packet.HasField("write_isp_parameters_command"):
    write_command = data_packet.write_isp_parameters_command
    if write_command.HasField("gamma"):
        gamma_parameters = write_command.gamma
        print(f"Gamma Enabled: {gamma_parameters.enabled}")
        gamma_values = gamma_parameters.gamma
        print("Gamma Parameters:")
        for value in gamma_values:
            print(value)
    else:
        print("No Gamma parameters found in the WriteISPParametersCommand message.")
else:
    print("No WriteISPParametersCommand found in the DataPacket.")
