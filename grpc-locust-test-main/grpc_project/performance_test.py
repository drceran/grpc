import asyncio
import grpc
import device_manager_pb2
import device_manager_pb2_grpc

# Modify the get_bandwidth function to run the gRPC call in a separate thread
def get_bandwidth(client, device_id):
    request = device_manager_pb2.DeviceRequest(device_id=device_id)
    response = client.CheckBandwidth(request)  # Change this to CheckBandwidth
    print(f"Device {device_id} has bandwidth: {response.message}")  # Updated to reflect response structure
    return response

async def run():
    channel = grpc.insecure_channel('localhost:50051')
    client = device_manager_pb2_grpc.DeviceManagerStub(channel)

    # Perform concurrent requests by running in separate threads
    tasks = []
    for i in range(10):  # 10 simultaneous requests
        tasks.append(asyncio.to_thread(get_bandwidth, client, f"device{i}"))
    
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(run())
