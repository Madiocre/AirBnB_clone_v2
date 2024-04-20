#!/usr/bin/python3
""" This script starts a Flask Web App """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello():
    return "Hello, World!"
