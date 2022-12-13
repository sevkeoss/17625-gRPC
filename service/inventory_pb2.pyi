from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishingYear", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTION: Book.Genre
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    GENRE_UNSPECIFIED: Book.Genre
    ISBN_FIELD_NUMBER: _ClassVar[int]
    MYSTERY: Book.Genre
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    SCIENCE_FICTION: Book.Genre
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.Genre
    isbn: str
    publishingYear: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNumber", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    book: Book
    inventoryNumber: int
    status: InventoryItem.Status
    def __init__(self, inventoryNumber: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ...) -> None: ...
