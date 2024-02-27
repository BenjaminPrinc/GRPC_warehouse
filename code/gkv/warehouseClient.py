import grpc
import warehouse_pb2
import warehouse_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = warehouse_pb2_grpc.WarehouseStub(channel)

    request = warehouse_pb2.MessageResponse()

    # sending the request to the server
    response = stub.GetServerResponse(request)

    # printing the response
    print("Client received: " + "\n" + response.responseData)


if __name__ == '__main__':
    run()
