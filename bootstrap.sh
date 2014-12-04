#!/bin/bash

echo "Bootstrapping EasyTeX"

# Delete previous virtual environment
if [ -d "/usr/local/venv" ]; then
  rm -rf /usr/local/venv
fi

echo "Installing virtualenv"
pip install virtualenv

echo "Creating venv"
virtualenv /usr/local/venv

# Activate virtual environment and install necessary packages
source /usr/local/venv/bin/activate
pip install pyparsing
pip install coverage
pip install nose
