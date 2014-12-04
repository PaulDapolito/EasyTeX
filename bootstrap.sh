#!/bin/bash

echo "Bootstrapping EasyTeX"

# Delete previous virtual environment
if [ -d "/usr/local/EasyTeX/venv" ]; then
  rm -rf /usr/local/EasyTeX/venv
fi

echo "Installing virtualenv"
pip install virtualenv

echo "Creating venv"
virtualenv /usr/local/EasyTeX/venv

# Activate virtual environment and install necessary packages
source /usr/local/EasyTeX/venv/bin/activate
pip install pyparsing
pip install coverage
pip install nose
pip install tex
