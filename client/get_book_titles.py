from inventory_client import InventoryClient

def get_book_titles(client, isbns):
    titles = list()

    for isbn in isbns:
        response = client.get_book(isbn)
        titles.append(response.book.title)
    
    return titles


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 50051
    client = InventoryClient(ip, port)

    isbns = ["978-0062073501", "978-0451524935"]
    print(get_book_titles(client, isbns))