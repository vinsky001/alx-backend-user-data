#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, Abort, redirect, request


app = flask(__name__)
AUTH = Auth()


@app.route('/', method=['GET'], strict_slashes=False)
def root():
    """Return a dummy JSON payload"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
