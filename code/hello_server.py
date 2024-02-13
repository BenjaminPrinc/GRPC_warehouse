import grpc
from concurrent import futures
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class HelloService(pb2_grpc.HelloServicer):

    def __init__(self, *args, **kwargs):
        print('Server Running')
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HelloServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()