import time

import grpc
import warehouse_pb2
import warehouse_pb2_grpc


def run():
    name = "client1"
    channel = grpc.insecure_channel('localhost:50051')
    stub = warehouse_pb2_grpc.WarehouseStub(channel)

    request = warehouse_pb2.PingRequest(clientID=name)
    response = stub.HealthCheck(request)
    print("Client received: " + response.status)

    request = warehouse_pb2.MessageResponse()

    # sending the request to the server
    response = stub.GetServerResponse(request)

    # printing the response
    print("Client received: " + "\n" + response.responseData)
    while True:
        request = warehouse_pb2.PingRequest(clientID=name)
        response = stub.HealthCheck(request)
        print("Client received: "+response.status+", at: "+response.timestamp)
        time.sleep(5)

if __name__ == '__main__':
    run()
