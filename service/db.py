import inventory_pb2

book1 = inventory_pb2.Book(isbn="978-0062073501", title="Murder on the Orient Express",
  author="Agatha Christie", genre=inventory_pb2.Book.MYSTERY, publishingYear=2011)

book2 = inventory_pb2.Book(isbn="978-0451524935", title="1984",
  author="George Orwell", genre=inventory_pb2.Book.SCIENCE_FICTION, publishingYear=1961)


# Sample database of books.

# Contains a mapping of isbn -> book
books = dict()
books["978-0062073501"] = book1
books["978-0451524935"] = book2