from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__, static_folder="..", static_url_path="")

DATABASE = Path(__file__).parent / "website.db"

@app.route("/")
def home():
    return app.send_static_file("HTML/index.html")

@app.route("/about.html")
def about():
    return app.send_static_file("HTML/about.html")

@app.route("/contact.html")
def contact():
    return app.send_static_file("HTML/contact.html")

if __name__== "__main__":
    app.run(debug=True)

