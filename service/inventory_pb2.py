# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"\xb5\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x05genre\x18\x04 \x01(\x0e\x32\x0b.Book.Genre\x12\x16\n\x0epublishingYear\x18\x05 \x01(\r\"L\n\x05Genre\x12\x15\n\x11GENRE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\n\n\x06\x41\x43TION\x10\x02\x12\x0b\n\x07MYSTERY\x10\x03\"\x97\x01\n\rInventoryItem\x12\x17\n\x0finventoryNumber\x18\x01 \x01(\r\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12%\n\x06status\x18\x03 \x01(\x0e\x32\x15.InventoryItem.Status\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x0b\n\tinventoryb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=20
  _BOOK._serialized_end=201
  _BOOK_GENRE._serialized_start=125
  _BOOK_GENRE._serialized_end=201
  _INVENTORYITEM._serialized_start=204
  _INVENTORYITEM._serialized_end=355
  _INVENTORYITEM_STATUS._serialized_start=308
  _INVENTORYITEM_STATUS._serialized_end=342
# @@protoc_insertion_point(module_scope)
