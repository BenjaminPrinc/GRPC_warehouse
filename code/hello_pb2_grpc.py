# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_pb2 as hello__pb2


class HelloStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerResponse = channel.unary_unary(
                '/hello.Hello/GetServerResponse',
                request_serializer=hello__pb2.Message.SerializeToString,
                response_deserializer=hello__pb2.MessageResponse.FromString,
                )


class HelloServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerResponse(self, request, context):
        """A simple RPC.

        Obtains the MessageResponse at a given position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerResponse,
                    request_deserializer=hello__pb2.Message.FromString,
                    response_serializer=hello__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.Hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hello(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.Hello/GetServerResponse',
            hello__pb2.Message.SerializeToString,
            hello__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
