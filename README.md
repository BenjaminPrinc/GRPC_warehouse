# GRPC Warehouse

**Author**: Benjamin Princ

**Date**: 13.02.2024

- [GRPC Warehouse](#grpc-warehouse)
  - [Introduction](#introduction)
  - [Work](#work)
    - [1. Installing python packages](#1-installing-python-packages)
    - [2. Defining the .proto file](#2-defining-the-proto-file)
    - [3. Client and Server](#3-client-and-server)
  - [Sources](#sources)


## Introduction
A grpc demo should be implemented, which shows the communication between a server and client.

## Work

### 1. Installing python packages
GRPC needs the packages **grpcio** and **grpcio-tools**, which can be installed with `pip install grpcio grpcio-tools`.

### 2. Defining the .proto file
You can say, that the proto file defines the grpc service. For example, which datatypes are used. After the proto file is finished, a command generate the stubs, which are essential for the client and server.

`python -m <FileName>.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.`


### 3. Client and Server
* **Server:**
In my case, the [Server](code/hello_server.py) serves a service on the localhost port 50051 and also defines what happens when the client requests the server.

* **Client:**
The [Client](code/hello_client.py) is the client which requests the localhost port 50051 and sends a message to it.

In my case the Server then answers the client reponse whith a message, which contains the clients text and something else.

![Client Output](Client_output.png)


## Sources
[1], *GRPC python*, https://www.velotio.com/engineering-blog/grpc-implementation-using-python

