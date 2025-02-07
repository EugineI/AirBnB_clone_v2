#!/usr/bin/python3
"""
Start a flask framework
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    this is the index function
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def name_HBNB():
    """
    returns HBNB from foute /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    returns C + test value
    """
    new_text = text.replace("_", " ")
    return f"C {new_text}"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
