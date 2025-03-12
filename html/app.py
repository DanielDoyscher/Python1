"""
Docstring for this Python module:
This module serves as a starting point for a simple Docker container.
"""

from flask import Flask, request # Importiere das request-Objekt

app = Flask(__name__)

@app.route('/')
def home():
    """Handles the root route and provides instructions."""
    return """
    Welcome to the Simple Calculator!
    Use the endpoints /add, /subtract, /multiply, and /divide with parameters a and b.
    Example: /add?a=5&b=3
    """

@app.route('/add')
def add():
    """Adds two numbers provided as query parameters."""
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
