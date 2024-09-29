#!/bin/bash

# Install dependencies
sudo apt install python3-pip python3-venv
pip install --upgrade pip

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
strace -f -t -e trace=file pylsp --ws --port 8082