from flask import Flask, render_template, request, redirect
from database import init_db, get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    conn = get_db_connection()
    issues = conn.execute("SELECT * FROM issues").fetchall()

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

        conn = get_db_connection()
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