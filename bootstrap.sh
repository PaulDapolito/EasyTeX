#!/bin/bash

echo "Bootstrapping EasyTeX"

echo "Installing virtualenv"
pip install virtualenv

echo "Creating venv"
virtualenv venv

# Activate virtual environment and install necessary packages
source venv/bin/activate
pip install pyparsing
pip install nose
