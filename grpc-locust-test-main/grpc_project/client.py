import grpc
import complex_service_pb2
import complex_service_pb2_grpc
import time  # Import time for performance testing




def get_bandwidth(client):
    # Construct a complex request with nested and repeated fields
    request = complex_service_pb2.DeviceData(
        id="12345",
        info=complex_service_pb2.DeviceData.Info(
            checksum="abc123",
            device_count=10,
            source_count=5,
            service_group_count=3,
        ),
        equipment=[
            complex_service_pb2.DeviceData.Equipment(),
            complex_service_pb2.DeviceData.Equipment(),
        ],
        channelList=[
            complex_service_pb2.DeviceData.Channel(),
            complex_service_pb2.DeviceData.Channel(),
        ],
        destinations=[
            complex_service_pb2.DeviceData.Destination(),
            complex_service_pb2.DeviceData.Destination(),
        ],
        serviceGroups=[
            complex_service_pb2.DeviceData.ServiceGroup(),
            complex_service_pb2.DeviceData.ServiceGroup(),
        ],
        sourceEquipment=[
            complex_service_pb2.DeviceData.SourceEquipment(),
            complex_service_pb2.DeviceData.SourceEquipment(),
        ],
        devices=[
            complex_service_pb2.DeviceData.Device(
                vendor="VendorA",
                headend="Headend1",
                channels=[
                    complex_service_pb2.DeviceData.Device.Channel(
                        tsid="123",
                        annex="B",
                        qam_name="QAM-1",
                        base_port="8080",
                        frequency="550MHz",
                        port_step="10",
                        power_key="PK123",
                        interleaver="I128",
                        output_port="9090",
                        base_program="Program1",
                        media_cipher="AES256",
                        channel_width="6MHz",
                        max_bandwidth=1000.0,
                        program_count="50",
                        service_state="Active",
                        qam_group_name="Group1",
                        modulation_type="64-QAM",
                    ),
                    complex_service_pb2.DeviceData.Device.Channel(
                        tsid="124",
                        annex="A",
                        qam_name="QAM-2",
                        base_port="8081",
                        frequency="560MHz",
                        port_step="10",
                        power_key="PK124",
                        interleaver="I256",
                        output_port="9091",
                        base_program="Program2",
                        media_cipher="AES128",
                        channel_width="6MHz",
                        max_bandwidth=800.0,
                        program_count="30",
                        service_state="Inactive",
                        qam_group_name="Group2",
                        modulation_type="256-QAM",
                    ),
                ],
            ),
            complex_service_pb2.DeviceData.Device(
                vendor="VendorB",
                headend="Headend2",
                channels=[
                    complex_service_pb2.DeviceData.Device.Channel(
                        tsid="125",
                        annex="C",
                        qam_name="QAM-3",
                        base_port="8082",
                        frequency="570MHz",
                        port_step="20",
                        power_key="PK125",
                        interleaver="I64",
                        output_port="9092",
                        base_program="Program3",
                        media_cipher="RSA2048",
                        channel_width="8MHz",
                        max_bandwidth=1200.0,
                        program_count="40",
                        service_state="Active",
                        qam_group_name="Group3",
                        modulation_type="128-QAM",
                    ),
                ],
            ),
        ],
    )
    
    # Record start time
    start_time = time.time()
    
    # Make request
    response = client.ComplexMethod(request)
    
    # Record end time
    end_time = time.time()
    
    # Calculate and print elapsed time
    elapsed_time = end_time - start_time
    print("Request processed in", elapsed_time, "seconds")



# def get_bandwidth(client):
#     request = complex_service_pb2.DeviceData(id="1")#, info=complex_service_pb2.DeviceData.Info(checksum="abc"))
    
#     # Record start time
#     start_time = time.time()
    
#     # Make request
#     # grpc req
#     response = client.ComplexMethod(request)
    
#     # Record end time
#     end_time = time.time()
    
#     # Calculate and print elapsed time
#     elapsed_time = end_time - start_time
  
#     print("Request processed in", {elapsed_time}, "seconds")

def run():
    # Connect to the server
    channel = grpc.insecure_channel('localhost:50051')
    client = complex_service_pb2_grpc.ComplexServiceStub(channel)

    get_bandwidth(client)

if __name__ == '__main__':
    run()
