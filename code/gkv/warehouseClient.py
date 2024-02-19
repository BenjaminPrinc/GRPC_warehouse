import grpc
import warehouse_pb2
import warehouse_pb2_grpc
import locale

def run():
    # Erstellen Sie einen gRPC-Kanal und einen Stub.
    channel = grpc.insecure_channel('localhost:50051')
    stub = warehouse_pb2_grpc.WarehouseStub(channel)

    # Erstellen Sie eine einfache Anfrage.
    request = warehouse_pb2.MessageResponse()

    # Senden Sie die Anfrage und empfangen Sie die Antwort.
    response = stub.GetServerResponse(request)

    # Drucken Sie die Antwort.
    print("Client received: " + response.responseData)
    print(locale.getpreferredencoding())

if __name__ == '__main__':
    run()
