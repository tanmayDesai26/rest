# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lab6_pb2 as lab6__pb2


class Lab6Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DoAdd = channel.unary_unary(
                '/lab6.Lab6/DoAdd',
                request_serializer=lab6__pb2.addMsg.SerializeToString,
                response_deserializer=lab6__pb2.addReply.FromString,
                )
        self.DotProduct = channel.unary_unary(
                '/lab6.Lab6/DotProduct',
                request_serializer=lab6__pb2.dotProductMsg.SerializeToString,
                response_deserializer=lab6__pb2.dotProductReply.FromString,
                )
        self.RawImage = channel.unary_unary(
                '/lab6.Lab6/RawImage',
                request_serializer=lab6__pb2.rawImageMsg.SerializeToString,
                response_deserializer=lab6__pb2.imageReply.FromString,
                )
        self.JsonImage = channel.unary_unary(
                '/lab6.Lab6/JsonImage',
                request_serializer=lab6__pb2.jsonImageMsg.SerializeToString,
                response_deserializer=lab6__pb2.imageReply.FromString,
                )


class Lab6Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def DoAdd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DotProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JsonImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Lab6Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DoAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.DoAdd,
                    request_deserializer=lab6__pb2.addMsg.FromString,
                    response_serializer=lab6__pb2.addReply.SerializeToString,
            ),
            'DotProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DotProduct,
                    request_deserializer=lab6__pb2.dotProductMsg.FromString,
                    response_serializer=lab6__pb2.dotProductReply.SerializeToString,
            ),
            'RawImage': grpc.unary_unary_rpc_method_handler(
                    servicer.RawImage,
                    request_deserializer=lab6__pb2.rawImageMsg.FromString,
                    response_serializer=lab6__pb2.imageReply.SerializeToString,
            ),
            'JsonImage': grpc.unary_unary_rpc_method_handler(
                    servicer.JsonImage,
                    request_deserializer=lab6__pb2.jsonImageMsg.FromString,
                    response_serializer=lab6__pb2.imageReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lab6.Lab6', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lab6(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DoAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab6.Lab6/DoAdd',
            lab6__pb2.addMsg.SerializeToString,
            lab6__pb2.addReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DotProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab6.Lab6/DotProduct',
            lab6__pb2.dotProductMsg.SerializeToString,
            lab6__pb2.dotProductReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RawImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab6.Lab6/RawImage',
            lab6__pb2.rawImageMsg.SerializeToString,
            lab6__pb2.imageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JsonImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lab6.Lab6/JsonImage',
            lab6__pb2.jsonImageMsg.SerializeToString,
            lab6__pb2.imageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
