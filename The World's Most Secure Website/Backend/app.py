from flask import Flask, request, jsonify, session
import sqlite3
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
app = Flask(__name__, static_folder=project_root, static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("HTML/index.html")


@app.route("/index.html")
def index_file():
    return app.send_static_file("HTML/index.html")


@app.route("/api/hello")
def hello():
    return jsonify({
        "message" : "flask is working!"
    })

app.run()