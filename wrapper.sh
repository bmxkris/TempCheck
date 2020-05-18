#!/bin/bash

cd /app
python3 -m http.server &
python 15_dht11.py 

