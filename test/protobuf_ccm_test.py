import protobuf.protocols_pb2
import socket

ccm_parameters = protobuf.protocols_pb2.CCMParameters()
ccm_parameters.ccm.extend([0, -0.2, 0.15, -0.35, 1.47, 0.35, 0.35, -0.45, 11.5])
ccm_parameters.enabled = True

write_command = protobuf.protocols_pb2.WriteISPParametersCommand()
write_command.ccm.CopyFrom(ccm_parameters)

data_packet = protobuf.protocols_pb2.DataPacket()
data_packet.write_isp_parameters_command.CopyFrom(write_command)

serialized_command = data_packet.SerializeToString()
print(serialized_command)

server_address = ('192.168.31.39', 8090)  # 服务器的地址和端口

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
try:
    # 发送序列化的消息
    sock.sendall(serialized_command)
finally:
    sock.close()
print("Message sent successfully")

# decode
data_packet = protobuf.protocols_pb2.DataPacket()
data_packet.ParseFromString(serialized_command)

# 检查消息中包含的具体消息类型并解析
if data_packet.HasField("write_isp_parameters_command"):
    write_command = data_packet.write_isp_parameters_command
    if write_command.HasField("ccm"):
        ccm_parameters = write_command.ccm
        print(f"CCM Enabled: {ccm_parameters.enabled}")
        ccm_matrix = ccm_parameters.ccm
        print("CCM Parameters:")
        for i in range(3):
            print(ccm_matrix[i * 3:(i + 1) * 3])
    else:
        print("No CCM parameters found in the WriteISPParametersCommand message.")
else:
    print("No WriteISPParametersCommand found in the DataPacket.")
