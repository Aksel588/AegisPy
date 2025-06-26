# main.py
#
# This is the entry point for running your Aegispy application.
# It imports the FastAPI app from your router and starts the server using Uvicorn.
#
# Usage:
#   python main.py
#
# This will start the development server at http://127.0.0.1:8000
#
# You can change the host and port as needed.
#
"""
Main entry point for the Aegispy application.
Run this file to start the FastAPI server with Uvicorn.
"""

from core.router import app  # could be FastAPI or custom app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)