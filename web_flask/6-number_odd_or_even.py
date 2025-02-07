#!/usr/bin/python3
"""
starting a web framework
"""
from flask import Flask
from flask import render_template
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


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python_text(text):
    """
    displays Python followed by text or default "is cool"
    """
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def check_number(n):
    """
    checks for integers
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number_template(n):
    """
    renders a template if  n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def render_oddEven_template(n):
    """
    renders template for odd or even number
    """
    if n % 2 == 0:
        choice = "even"
    else:
        choice = "odd"
    return render_template('6-number_odd_or_even.html', n=n, choice=choice)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
