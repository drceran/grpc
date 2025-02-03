from locust import User, task, between
import grpc
import complex_service_pb2
import complex_service_pb2_grpc
import random

class GPRCTestUser(User):
    # Set the wait time between requests
    wait_time = between(1, 2)  # Random wait time between requests

    @task
    def test_grpc_request(self):
        # Generate a random device ID
        device_id = f"device{random.randint(1, 100)}"  # Random device ID between device1 and device100
        
        # Connect to the gRPC server
        channel = grpc.insecure_channel('localhost:50051')
        client = complex_service_pb2_grpc.ComplexServiceStub(channel)

        # Perform a gRPC request with the random device ID
        request = complex_service_pb2.DeviceData(id=str(device_id))
        try:
            response = client.ComplexMethod(request)  # Ensure this matches the correct RPC method name
            # Log the response
            print(f"Response for device ID {response.id}: {response.message}")
        except grpc.RpcError as e:
            print(f"gRPC request failed: {e}")
