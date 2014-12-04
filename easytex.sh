#!/bin/bash

echo "Running EasyTeX!"

# Usage: ./easytex easytex_file_name
source /usr/local/venv/bin/activate
source/easytex.py $1

echo "EasyTeX completed computation!"
