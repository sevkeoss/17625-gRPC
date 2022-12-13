from concurrent import futures
import logging

import grpc

import inventory_service_pb2
import inventory_service_pb2_grpc
import db

# The Inventory Service definition.
class Inventory(inventory_service_pb2_grpc.InventoryServicer):

    # This function accepts a CreateBookRequest object. It gets the book contained within 
    # that object and adds it to the dictionary of books.

    # If the isbn number exists, the book is not added/replaced.
    # Returns a CreateBookResponse object
    def CreateBook(self, request, context) -> inventory_service_pb2.CreateBookResponse:
        status = False
        new_book = request.book

        missing = None
        if not new_book.isbn:
            missing = "isbn"
        elif not new_book.title:
            missing = "title"
        elif not new_book.author:
            missing = "author"
        elif not new_book.genre:
            missing = "genre"
        elif new_book.publishingYear <= 0:
            missing = "publishingYear"

        if missing is not None:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("Missing/invalid field: {}".format(missing))
            raise ValueError("Missing/invalid field: {}".format(missing))

        # Check if book already exists
        if new_book.isbn not in db.books:
            db.books[new_book.isbn] = new_book
            status = True
        else:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("isbn '{}' already exists".format(new_book.isbn))

        return inventory_service_pb2.CreateBookResponse(success=status)

    # This function accepts a GetBookResponse object. It gets the isbn contained within
    # that object and tries to find the book from the current dictionary.

    # If the isbn number exists, the book is returned. Otherwise, an empty response is returned.
    # Returns a GetBookResponse object.
    def GetBook(self, request, context) -> inventory_service_pb2.GetBookResponse:
        resp_book = None

        if not request.isbn:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("Missing isbn field")
            raise ValueError("Missing isbn field")

        # Check if book exists
        if request.isbn in db.books:
            resp_book = db.books[request.isbn]
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("isbn '{}' not found".format(request.isbn))

        return inventory_service_pb2.GetBookResponse(book=resp_book)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()