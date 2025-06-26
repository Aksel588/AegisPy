# core/router.py
#
# This file sets up the main routing and template rendering for your application using FastAPI and Jinja2.
#
# Usage:
#   - Define your route handlers here or import them from your controllers.
#   - Use the 'templates' object to render HTML templates with context data.
#   - You can add more routes or customize the routing logic as needed.
#
# Example:
#   @app.get('/about', response_class=HTMLResponse)
#   def about(request: Request):
#       return templates.TemplateResponse('about.html', {'request': request})
#
"""
This file initializes the FastAPI app, sets up Jinja2 template rendering, and defines the main routes.
Edit or extend as needed for your project's routing needs.
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Set up Jinja2 templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})