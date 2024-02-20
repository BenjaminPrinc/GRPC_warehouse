# GRPC Warehouse

**Author**: Benjamin Princ

**Date**: 13.02.2024

- [GRPC Warehouse](#grpc-warehouse)
  - [Introduction](#introduction)
  - [Work (GKue)](#work-gkue)
    - [1. Installing python packages](#1-installing-python-packages)
    - [2. Defining the .proto file](#2-defining-the-proto-file)
    - [3. Client and Server](#3-client-and-server)
  - [Work (GKv)](#work-gkv)
    - [1. Create a new gradle Project](#1-create-a-new-gradle-project)
    - [2. Generating the grpc classes from the .proto file](#2-generating-the-grpc-classes-from-the-proto-file)
      - [2.1 Problem with generated classes](#21-problem-with-generated-classes)
    - [3. Implementing the method to answer the grpc request](#3-implementing-the-method-to-answer-the-grpc-request)
    - [4. Implementing the python client](#4-implementing-the-python-client)
  - [Sources](#sources)


## Introduction
A grpc demo should be implemented, which shows the communication between a server and client.

## Work (GKue)

### 1. Installing python packages
GRPC needs the packages **grpcio** and **grpcio-tools**, which can be installed with `pip install grpcio grpcio-tools`.

### 2. Defining the .proto file
You can say, that the proto file defines the grpc service. For example, which datatypes are used. After the proto file is finished, a command generate the stubs, which are essential for the client and server.

`python -m grpc_tools.protoc --proto_path=. ./<FileName>.proto --python_out=. --grpc_python_out=.`


### 3. Client and Server
* **Server:**
In my case, the [Server](code/gkue/hello_server.py) serves a service on the localhost port 50051 and also defines what happens when the client requests the server.

* **Client:**
The [Client](code/gkue/hello_client.py) is the client which requests the localhost port 50051 and sends a message to it.

In my case the Server then answers the client reponse whith a message, which contains the clients text and something else.

![Client Output](Client_output.png)


## Work (GKv)

### 1. Create a new gradle Project
For the grpc java implementation i created a new gradle project, which contains the old java class for creating random Products.
The .proto file declares the Warehouse and ProductData(which is part of the warehouse)

### 2. Generating the grpc classes from the .proto file
Google´s protobuf plugin is able to automatically generate the needed classes from the .proto file, when gradle builds the project.

#### 2.1 Problem with generated classes
At first i got a syntax error when i tried to access the generated classes. 
With the help of the stackoverflow thread (Source [3]), i found out, that you need to declare the generated path as source for the IDE:
```gradle
sourceSets {
    main {
        java {
            srcDirs 'build/generated/source/proto/main/grpc'
            srcDirs 'build/generated/source/proto/main/java'
        }
    }
}
```
*build.gradle*

### 3. Implementing the method to answer the grpc request 
My WarehouseImpl class is responsible for answering requests to the server.
When it gets a new request, it generates three randomProducts, fills out the WarehouseData.builder and adds the products to it.

In the main method a simple server on port 50051 gets created and the Impl class gets add as a service.

```java
public class Main {
    public static void main(String[] args) throws Exception {
        Server server = ServerBuilder.forPort(50051)
                .addService(new WarehouseImpl())
                .build()
                .start();

        System.out.println("Server started, listening on " + 50051);

        server.awaitTermination();
    }
}
```

### 4. Implementing the python client
For the python client, i simply copied the same proto file like for the server,
into my python project and entered the command:

`python -m grpc_tools.protoc --proto_path=. ./warehouse.proto --python_out=. --grpc_python_out=.`

```py
def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = warehouse_pb2_grpc.WarehouseStub(channel)

    request = warehouse_pb2.MessageResponse()

    response = stub.GetServerResponse(request)

    print("Client received: " + response.responseData)
    print(locale.getpreferredencoding())

if __name__ == '__main__':
    run()
```

## Sources
[1], *GRPC python*, https://www.velotio.com/engineering-blog/grpc-implementation-using-python

[2], *Java proto*, https://medium.com/@DivyaJaisawal/generate-java-code-from-proto-file-using-gradle-1fb9fe64e046

[3], *Import generated fiels*, https://stackoverflow.com/questions/44088009/import-protobuf-generated-classes-using-gradle-in-intellij


