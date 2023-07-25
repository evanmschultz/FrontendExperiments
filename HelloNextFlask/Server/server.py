from flask import Flask, jsonify, Response
from typing import Dict, Any

from flask_cors import CORS

# Instantiate a Flask instance named app
app = Flask(__name__)

# Instantiate a CORS instance
CORS(app)


@app.route("/api/home", methods=["GET"])
def hello() -> Response:
    """
    Root Route

    This is the root route which will return a welcome message.

    Methods:
        GET

    Returns:
        dict: A welcome message in JSON format.
    """
    data: Dict[str, Any] = {
        "title": "Hello Next Flask!",
        "list": ["Welcome to my first ", "NextJS ", "project using a ", "Flask API."],
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
