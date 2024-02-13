import grpc
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class HelloClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.HelloStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the server
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = HelloClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')