#!/bin/bash

cd ./services

python3 backend.py & uvicorn api:app --host 0.0.0.0 --port 8080