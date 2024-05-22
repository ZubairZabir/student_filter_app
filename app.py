from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students", methods=["GET"])
def get_students():
    move_out_date = request.args.get("move_out_date")

    conn = get_db_connection()
    query = "SELECT * FROM students WHERE 1=1"
    params = []

    if move_out_date:
        query += " AND move_out_date = ?"
        params.append(move_out_date)

    students = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify([dict(row) for row in students])

if __name__ == "__main__":
    app.run(debug=True)
