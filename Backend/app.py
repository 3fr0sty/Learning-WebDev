from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__, static_folder="..", static_url_path="")

DATABASE = Path(__file__).parent / "website.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return app.send_static_file("HTML/index.html")

@app.route("/index.html")
def index():
    return app.send_static_file("HTML/index.html")

@app.route("/about.html")
def about():
    return app.send_static_file("HTML/about.html")

@app.route("/contact.html")
def contact():
    return app.send_static_file("HTML/contact.html")

@app.route("/login.html")
def loginPage():
    return app.send_static_file("HTML/login.html")

@app.route("/login.html",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username,password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return "LOGIN SUCCESSFUL"
    else:
        return "LOGIN FAILED"

@app.route("/signup.html")
def signupPage():
    return app.send_static_file("HTML/signup.html")

@app.route("/signup.html",methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name,password) VALUES (?,?)", (username,password))
        conn.commit()
        conn.close()
        return "Account created successfully"
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already in use"

if __name__== "__main__":
    init_db()
    app.run(debug=True)
