import unittest
from unittest.mock import Mock

from inventory_client import InventoryClient
from get_book_titles import get_book_titles

import inventory_pb2, inventory_service_pb2

class TestMockInventory(unittest.TestCase):
    
    def test_mock_get_book_titles(self):
        expected_titles = ["test title 1", "test title 2"]

        mock_client = Mock()
        mock_client.get_book.side_effect = [
            inventory_service_pb2.GetBookResponse(
                book=inventory_pb2.Book(
                    isbn='test isbn 1', title='test title 1', author='test author1 ', 
                    genre=inventory_pb2.Book.GENRE_UNSPECIFIED, publishingYear=0
                ))
            ,
            inventory_service_pb2.GetBookResponse(
                book=inventory_pb2.Book(
                    isbn='test isbn 2', title='test title 2', author='test author 2', 
                    genre=inventory_pb2.Book.GENRE_UNSPECIFIED, publishingYear=0
                ))
        ]

        test_isbns = ['test isbn 1', 'test isbn 2']
        titles = get_book_titles(mock_client, test_isbns)
        
        self.assertEqual(mock_client.get_book.call_count, 2)
        self.assertListEqual(titles, expected_titles)

class TestInventory(unittest.TestCase):

    def test_get_book_titles(self):
        expected_titles = ["Murder on the Orient Express", "1984"]

        client = InventoryClient('127.0.0.1', 50051)

        isbns = ["978-0062073501", "978-0451524935"]
        titles = get_book_titles(client,isbns)

        self.assertListEqual(titles, expected_titles)

if __name__ == '__main__':
    unittest.main()