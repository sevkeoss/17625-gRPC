#!/bin/sh

SRC_DIR="protos/"
DST_DIR="service/"

python3 -m grpc_tools.protoc -I=$SRC_DIR --python_out=$DST_DIR --pyi_out=$DST_DIR $SRC_DIR/inventory.proto

python3 -m grpc_tools.protoc -I=$SRC_DIR --python_out=$DST_DIR --pyi_out=$DST_DIR --grpc_python_out=$DST_DIR $SRC_DIR/inventory_service.proto
