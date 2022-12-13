# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventory_service_pb2 as inventory__service__pb2


class InventoryStub(object):
    """The Inventory Service interface.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/Inventory/CreateBook',
                request_serializer=inventory__service__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=inventory__service__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/Inventory/GetBook',
                request_serializer=inventory__service__pb2.GetBookRequest.SerializeToString,
                response_deserializer=inventory__service__pb2.GetBookResponse.FromString,
                )


class InventoryServicer(object):
    """The Inventory Service interface.
    """

    def CreateBook(self, request, context):
        """A client-to-server RPC.

        Accepts a book with details and adds it to the list of books if it does not
        exist.

        Returns True if the book was added, otherwise an empty response for False.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """A simple RPC.

        Obtains the details of a given book.

        An empty response is returned if the book with the given isbn is not found.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=inventory__service__pb2.CreateBookRequest.FromString,
                    response_serializer=inventory__service__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=inventory__service__pb2.GetBookRequest.FromString,
                    response_serializer=inventory__service__pb2.GetBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Inventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inventory(object):
    """The Inventory Service interface.
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inventory/CreateBook',
            inventory__service__pb2.CreateBookRequest.SerializeToString,
            inventory__service__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inventory/GetBook',
            inventory__service__pb2.GetBookRequest.SerializeToString,
            inventory__service__pb2.GetBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
