import sys
import os
from pathlib import Path
path = Path(os.getcwd())

sys.path.insert(1, str(path.parent) + '/service')

import inventory_service_pb2, inventory_service_pb2_grpc

import grpc

class InventoryClient():
    def __init__(self, ip, port):
        channel = grpc.insecure_channel(ip + ':' + str(port))
        self.stub = inventory_service_pb2_grpc.InventoryStub(channel)

    def create_book(self, book):
        return self.stub.CreateBook(inventory_service_pb2.CreateBookRequest(book=book))

    def get_book(self, isbn):
        return self.stub.GetBook(inventory_service_pb2.GetBookRequest(isbn=isbn))
