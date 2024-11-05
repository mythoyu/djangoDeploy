#!/bin/bash

# Update pip
echo "Updating pip..."
python3.10 pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
pip install -r requirements.txt
# Make migrations
echo "Making migrations..."
# python3.10 manage.py makemigrations post --noinput
# python3.10 manage.py migrate --noinput
python3.10 manage.py migrate 


# Collect staticfiles
echo "Collect static..."
python3.10 manage.py collectstatic

echo "Build process completed!"

# build_files.sh


# make migrations
