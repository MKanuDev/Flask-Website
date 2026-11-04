
from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Connect to the database
def get_db():
    conn = sqlite3.connect("messages.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create the database table
def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/admin")
def admin():
    conn = get_db()
    messages = conn.execute(
        "SELECT * FROM messages ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("admin.html", messages=messages)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    message = request.form.get("message")

    conn = get_db()
    conn.execute(
        "INSERT INTO messages (name, message, date) VALUES (?, ?, ?)",
        (name, message, str(datetime.now()))
    )
    conn.commit()
    conn.close()

    return "Message saved! Thank you & be blessed, " + name

create_table()

if __name__ == "__main__":
    app.run(debug=True)
