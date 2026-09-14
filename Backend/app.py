from flask import Flask, request, jsonify, session
import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
load_dotenv()

# static_folder=".." lets Flask serve files from the project root (HTML/, CSS/, JS/, images/)
app = Flask(__name__, static_folder="..", static_url_path="")

app.secret_key = os.environ.get("SECRET_KEY")

# Absolute path to the DB file, so it works no matter what folder you run "python app.py" from
DATABASE = Path(__file__).parent / "website.db"

def init_db():
    # Creates the users table on startup if it doesn't already exist.
    # UNIQUE on name means SQLite will refuse a duplicate username (raises IntegrityError).
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
    conn.commit()
    conn.close()

# --- Static page routes: just hand back the matching HTML file ---

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

# --- Login: same URL as the page above, but only runs on POST (form submission) ---

@app.route("/login.html",methods=["POST"])
def login():
    # request.form pulls values by each <input>'s "name" attribute
    username = request.form.get("username")
    password = request.form.get("password")



    if not username or not password:
        return jsonify({"success": False, "message": "Please enter a username and password"}),400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # ?, ? placeholders keep raw user input out of the SQL string (prevents SQL injection)
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    user = cursor.fetchone()  # None if no matching row, otherwise a tuple of (id, name, password)
    conn.close()


    if user and check_password_hash(user[2],password):
        session["username"] = username
        return jsonify({"success": True, "message": "Welcome, " + user[1]}),200
    else:
        return jsonify({"success": False, "message": "Incorrect username or password"}),400

@app.route("/signup.html")
def signupPage():
    return app.send_static_file("HTML/signup.html")

@app.route("/whoami")
def whoami():
    username = session.get("username")
    return jsonify({"logged_in_as" : username})

# --- Signup: inserts a new user, and handles the case where the username is taken ---

@app.route("/signup.html",methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Username and password are required"}),400

    hashedPassword = generate_password_hash(password)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name,password) VALUES (?,?)", (username,hashedPassword))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Account created successfully, please log in"})
    except sqlite3.IntegrityError:
        # Raised when the UNIQUE constraint on "name" is violated (username already exists)
        conn.close()
        return jsonify({"success": False, "message": "Username already in use"}),409


@app.route("/signout")
def signOut():
    session.pop("username", None)
    return jsonify({"sign_out_success": True})

if __name__== "__main__":
    init_db()  # make sure the table exists before the server starts accepting requests
    app.run(debug=True)
