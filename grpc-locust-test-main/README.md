# gRPC Locust Test  

A load testing setup for gRPC services using Locust, designed to measure the performance and scalability of gRPC-based applications.  

## Features  
- Simulate thousands of concurrent users to test gRPC services.  
- Collect performance metrics like response times, throughput, and error rates.  
- Easy integration with custom gRPC services.  

## Getting Started  

### Prerequisites  
- Python 3.8+  
- Locust (`pip install locust`)  
- gRPC libraries (`pip install grpcio grpcio-tools`)  

### Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/grpc-locust-test.git  
   cd grpc-locust-test  

### Install the dependencies
```pip install -r requirements.txt  

### Update complex_service.proto

```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. complex_service.proto  
###Start the Locust web interface:
```locust -f locust.py --web-port 9090  

Open the Locust interface in your browser at http://localhost:8089.

Configure the test parameters in the Locust interface:

Number of Users: Set the desired number of concurrent users.
Spawn Rate: Define how many users to spawn per second.
Test Duration: Specify the total test duration (e.g., 3 minutes).
Start the test and monitor the results in real-time, including:

Response Times: Measure the latency of gRPC requests.
Requests per Second: Track the throughput of the service.
Error Rates: Identify any failed or problematic requests.
Analyze the metrics and logs after the test to assess performance and scalability.
