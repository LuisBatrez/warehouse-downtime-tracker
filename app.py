from flask import Flask, render_template, request, redirect
from database import init_db
import sqlite3


app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_name TEXT NOT NULL,
            issue_category TEXT NOT NULL,
            downtime_minutes INTEGER NOT NULL,
            shift TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM issues")
    issues = cursor.fetchall()

    conn.close()

    return render_template("index.html", issues=issues)


@app.route("/add", methods=["GET", "POST"])
def add_issue():

    if request.method == "POST":

        machine_name = request.form["machine_name"]
        issue_category = request.form["issue_category"]
        downtime_minutes = request.form["downtime_minutes"]
        shift = request.form["shift"]
        status = request.form["status"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO issues
            (machine_name, issue_category, downtime_minutes, shift, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            machine_name,
            issue_category,
            downtime_minutes,
            shift,
            status
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_issue.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)