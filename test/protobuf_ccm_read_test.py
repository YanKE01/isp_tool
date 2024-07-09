import protobuf.protocols_pb2 as protocols_pb2

# Step 1: Create a ReadISPParametersCommand for CCM
read_command = protocols_pb2.ReadISPParametersCommand()
read_command.parameter_type = protocols_pb2.ISPParameterType.CCM

data_packet = protocols_pb2.DataPacket()
data_packet.read_isp_parameters_command.CopyFrom(read_command)

# Serialize the command
serialized_read_command = data_packet.SerializeToString()

# Simulate receiving a response for the read command
# Create a mock response with current CCM parameters
response_packet = protocols_pb2.DataPacket()
isp_response = protocols_pb2.ISPParametersResponse()
isp_response.status = "success"
isp_response.message = "CCM parameters read successfully"
isp_response.parameter_type = protocols_pb2.ISPParameterType.CCM

current_ccm_parameters = protocols_pb2.CCMParameters()
current_ccm_parameters.enabled = True
current_ccm_parameters.ccm.extend([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0])
isp_response.parameters.ccm.CopyFrom(current_ccm_parameters)

response_packet.isp_parameters_response.CopyFrom(isp_response)
serialized_response = response_packet.SerializeToString()

# Deserialize the response
response_packet.ParseFromString(serialized_response)

# Check and parse CCM parameters
if response_packet.HasField("isp_parameters_response"):
    isp_response = response_packet.isp_parameters_response
    if isp_response.parameter_type == protocols_pb2.ISPParameterType.CCM:
        ccm_parameters = isp_response.parameters.ccm
        print(f"CCM Enabled: {ccm_parameters.enabled}")
        ccm_matrix = ccm_parameters.ccm
        print("Current CCM Parameters:")
        for i in range(3):
            print(ccm_matrix[i * 3:(i + 1) * 3])
    else:
        print("Received parameters are not CCM parameters.")
else:
    print("No ISPParametersResponse found in the DataPacket.")

# Step 2: Create a WriteISPParametersCommand with new CCM parameters
new_ccm_parameters = protocols_pb2.CCMParameters()
new_ccm_parameters.ccm.extend([0.1, -0.2, 0.3, -0.4, 1.5, 0.4, 0.3, -0.3, 1.2])
new_ccm_parameters.enabled = True

write_command = protocols_pb2.WriteISPParametersCommand()
write_command.ccm.CopyFrom(new_ccm_parameters)

data_packet = protocols_pb2.DataPacket()
data_packet.write_isp_parameters_command.CopyFrom(write_command)

# Serialize the command
serialized_write_command = data_packet.SerializeToString()

# Simulate receiving a response for the write command
# Create a mock response indicating the write was successful
write_response_packet = protocols_pb2.DataPacket()
isp_write_response = protocols_pb2.ISPParametersResponse()
isp_write_response.status = "success"
isp_write_response.message = "CCM parameters written successfully"
isp_write_response.parameter_type = protocols_pb2.ISPParameterType.CCM
isp_write_response.parameters.ccm.CopyFrom(new_ccm_parameters)

write_response_packet.isp_parameters_response.CopyFrom(isp_write_response)
serialized_write_response = write_response_packet.SerializeToString()

# Deserialize the write response
write_response_packet.ParseFromString(serialized_write_response)

# Check and confirm the write
if write_response_packet.HasField("isp_parameters_response"):
    isp_response = write_response_packet.isp_parameters_response
    if isp_response.parameter_type == protocols_pb2.ISPParameterType.CCM:
        ccm_parameters = isp_response.parameters.ccm
        print(f"CCM Enabled: {ccm_parameters.enabled}")
        ccm_matrix = ccm_parameters.ccm
        print("Written CCM Parameters:")
        for i in range(3):
            print(ccm_matrix[i * 3:(i + 1) * 3])
    else:
        print("Written parameters are not CCM parameters.")
else:
    print("No ISPParametersResponse found in the DataPacket.")

# Step 3: Read back the CCM parameters to confirm the write
# Reuse the previous read command
serialized_read_command = data_packet.SerializeToString()

# Simulate receiving a response for the read command
# Create a mock response with the newly written CCM parameters
confirm_read_packet = protocols_pb2.DataPacket()
confirm_isp_response = protocols_pb2.ISPParametersResponse()
confirm_isp_response.status = "success"
confirm_isp_response.message = "CCM parameters read successfully"
confirm_isp_response.parameter_type = protocols_pb2.ISPParameterType.CCM
confirm_isp_response.parameters.ccm.CopyFrom(new_ccm_parameters)

confirm_read_packet.isp_parameters_response.CopyFrom(confirm_isp_response)
serialized_confirm_response = confirm_read_packet.SerializeToString()

# Deserialize the confirm read response
confirm_read_packet.ParseFromString(serialized_confirm_response)

# Check and parse the confirmed CCM parameters
if confirm_read_packet.HasField("isp_parameters_response"):
    isp_response = confirm_read_packet.isp_parameters_response
    if isp_response.parameter_type == protocols_pb2.ISPParameterType.CCM:
        ccm_parameters = isp_response.parameters.ccm
        print(f"CCM Enabled: {ccm_parameters.enabled}")
        ccm_matrix = ccm_parameters.ccm
        print("Confirmed CCM Parameters:")
        for i in range(3):
            print(ccm_matrix[i * 3:(i + 1) * 3])
    else:
        print("Received parameters are not CCM parameters.")
else:
    print("No ISPParametersResponse found in the DataPacket.")
