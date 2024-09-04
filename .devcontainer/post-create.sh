#!/bin/bash

# Install server dependencies
cd server
curl -sSL https://install.python-poetry.org | python3 -
poetry install --no-root

# Install client dependencies
cd ../client
npm install

echo "Development environment setup complete!"