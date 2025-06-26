# config/settings.py
#
# This file handles application configuration and environment variables.
#
# Usage:
#   - Place your environment variables in a .env file at the project root.
#   - This script loads those variables and constructs the database URL.
#   - You can add more configuration variables as needed for your app.
#
# Example .env file:
#   DB_HOST=localhost
#   DB_PORT=3306
#   DB_USER=myuser
#   DB_PASSWORD=mypassword
#   DB_NAME=mydatabase
#
"""
This file loads environment variables and sets up configuration constants for the application.
Edit or extend as needed for your project.
"""

import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"