#!/usr/bin/env python3
#Start a flask framework#
from flask import Flask
app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_HBNB():
    #this is the index function#
    return"Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
