import grpc
from concurrent import futures
import complex_service_pb2 as pb2
import complex_service_pb2_grpc as pb2_grpc
import logging


logger = logging.getLogger(__name__)



class ComplexService(pb2_grpc.ComplexServiceServicer):  # Correct class name based on generated code
    def ComplexMethod(self, request, context):
        logger.info("request id {request.id} is received.")
        return request

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ComplexServiceServicer_to_server(ComplexService(), server)  # Register the service
    server.add_insecure_port('[::]:50051')
    
    print("Server is running and listening on port 50051...")  # Print message to indicate server is running
    server.start()
    server.wait_for_termination()




if __name__ == "__main__":
    serve()


