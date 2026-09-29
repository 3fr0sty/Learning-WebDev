import sqlite3 as sql

def init_db():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)")
    cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?,?)", ("harry2", "harryray20029@gmail.com"))
    conn.commit()
    conn.close()

init_db()
conn = sql.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)
conn.close()