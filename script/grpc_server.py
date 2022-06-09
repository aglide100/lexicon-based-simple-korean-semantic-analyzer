from concurrent import futures
import grpc
from Servicer import AnalyzerServicer
import analyzer_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    analyzer_pb2_grpc.add_AnalyzerServicer_to_server(AnalyzerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("Start GRPC server!")
    serve()

