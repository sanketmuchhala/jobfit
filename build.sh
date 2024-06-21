#!/usr/bin/env bash

# Ensure Cython is installed
pip install Cython==0.29.21

# Install the remaining dependencies
pip install -r requirements.txt

# Download the SpaCy model
python -m spacy download en_core_web_sm
