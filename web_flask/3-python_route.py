#!/usr/bin/python3
"""
starting a web framework
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    index route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def name_HBNB():
    """
    displays HBNB in a new route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C_text(text):
    """
    displays c followed by text
    """
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/", defaults={"text":"is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python_text(text):
    """
    displays Python followed by text or default "is cool"
    """
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
