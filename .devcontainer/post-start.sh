#!/bin/bash

# Start FastAPI server
cd server
poetry run python main.py &

# Start Next.js client
cd ../client
npm run dev &

# Keep the script running
wait