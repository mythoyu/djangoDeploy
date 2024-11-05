#!/bin/bash

# Update pip
echo "Updating pip..."
python3.12 pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
pip install -r requirements.txt
# Make migrations
echo "Making migrations..."

python3.12 manage.py migrate    


# Collect staticfiles
# python3.12 manage.py collectstatic

echo "Build process completed!"


