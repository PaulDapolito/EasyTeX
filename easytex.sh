#!/bin/bash

echo "Running EasyTeX!"

# Usage: ./easytex easytex_file_name
source /usr/local/EasyTeX/venv/bin/activate
python easytex.py $1

echo "EasyTeX completed computation!"
