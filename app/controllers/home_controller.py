# aegispy/core/router.py
#
# This file defines a simple controller system for your framework.
# It demonstrates how to register routes and controllers in a minimal way.
#
# Usage:
#   - Use the @route decorator to register a function as a route handler.
#   - The function will be mapped to the given path and return an HTML response.
#   - All registered routes are stored in the 'routes' dictionary.

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
# Dictionary to keep track of registered routes and their handler functions
routes = {}

def route(path):
    """
    Decorator to register a function as a route handler for the given path.
    Args:
        path (str): The URL path to register (e.g., '/about').
    Returns:
        decorator: A decorator that registers the function with FastAPI and stores it in 'routes'.
    Example:
        @route('/')
        def home(request):
            return '<h1>Hello, World!</h1>'
    """
    def decorator(func):
        # Register the function as a GET endpoint with FastAPI
        app.get(path, response_class=HTMLResponse)(func)
        # Store the function in the routes dictionary for reference
        routes[path] = func
        return func
    return decorator