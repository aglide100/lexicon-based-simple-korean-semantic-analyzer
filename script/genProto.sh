#!/bin/bash

#python3 -m grpc_tools.protoc -I ./pb --python_out=./pb --grpc_python_out=./pb analyzer.proto

cd ./pb

python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. analyzer.proto

python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. manager.proto

cd ..