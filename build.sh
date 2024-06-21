#!/usr/bin/env bash

# Upgrade pip to the latest version
pip install --upgrade pip

# Ensure Cython is installed before SpaCy
pip install Cython==0.29.21

# Install the remaining dependencies
pip install -r requirements.txt

# Download the SpaCy model
python -m spacy download en_core_web_sm