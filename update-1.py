"""
Docstring for this Python module:
This module serves as a starting point for a simple Docker container.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Handles the root route and returns a greeting."""
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
