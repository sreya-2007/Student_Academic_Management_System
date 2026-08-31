from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import date

app = Flask(__name__)
app.secret_key = "student-academic-demo-key"
DB = "academic.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT,
        teacher TEXT
    );
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER NOT NULL,
        total_classes INTEGER DEFAULT 0,
        attended_classes INTEGER DEFAULT 0,
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    );
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        subject TEXT,
        due_date TEXT,
        status TEXT DEFAULT 'Pending'
    );
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        exam TEXT,
        marks REAL,
        total REAL
    );
    """)
    conn.commit()
    conn.close()

@app.route("/")
def dashboard():
    conn = get_db()
    subjects = conn.execute("SELECT * FROM subjects ORDER BY name").fetchall()
    assignments = conn.execute(
        "SELECT * FROM assignments ORDER BY due_date LIMIT 5"
    ).fetchall()
    marks = conn.execute("SELECT * FROM marks ORDER BY id DESC LIMIT 5").fetchall()
    att_rows = conn.execute("""
        SELECT s.name, a.total_classes, a.attended_classes
        FROM attendance a JOIN subjects s ON s.id=a.subject_id
        ORDER BY s.name
    """).fetchall()
    conn.close()

    total = sum(r["total_classes"] for r in att_rows)
    attended = sum(r["attended_classes"] for r in att_rows)
    attendance_pct = round(attended * 100 / total, 1) if total else 0

    return render_template("dashboard.html",
        subjects=subjects, assignments=assignments, marks=marks,
        attendance=att_rows, attendance_pct=attendance_pct)

@app.route("/subjects", methods=["GET", "POST"])
def subjects():
    conn = get_db()
    if request.method == "POST":
        name = request.form["name"].strip()
        code = request.form["code"].strip()
        teacher = request.form["teacher"].strip()
        if name:
            conn.execute("INSERT INTO subjects(name, code, teacher) VALUES(?,?,?)",
                         (name, code, teacher))
            conn.commit()
            flash("Subject added successfully.")
        return redirect(url_for("subjects"))
    rows = conn.execute("SELECT * FROM subjects ORDER BY name").fetchall()
    conn.close()
    return render_template("subjects.html", subjects=rows)

@app.post("/subjects/delete/<int:id>")
def delete_subject(id):
    conn = get_db()
    conn.execute("DELETE FROM attendance WHERE subject_id=?", (id,))
    conn.execute("DELETE FROM subjects WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("Subject deleted.")
    return redirect(url_for("subjects"))

@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    conn = get_db()
    if request.method == "POST":
        subject_id = request.form["subject_id"]
        total = int(request.form["total_classes"])
        attended = int(request.form["attended_classes"])
        if attended <= total and total >= 0 and attended >= 0:
            existing = conn.execute(
                "SELECT id FROM attendance WHERE subject_id=?", (subject_id,)
            ).fetchone()
            if existing:
                conn.execute("""UPDATE attendance
                    SET total_classes=?, attended_classes=? WHERE subject_id=?""",
                    (total, attended, subject_id))
            else:
                conn.execute("""INSERT INTO attendance
                    (subject_id,total_classes,attended_classes) VALUES(?,?,?)""",
                    (subject_id, total, attended))
            conn.commit()
            flash("Attendance updated.")
        else:
            flash("Attended classes cannot be greater than total classes.")
        return redirect(url_for("attendance"))
    subjects = conn.execute("SELECT * FROM subjects ORDER BY name").fetchall()
    rows = conn.execute("""
        SELECT a.id, s.name, a.total_classes, a.attended_classes
        FROM attendance a JOIN subjects s ON s.id=a.subject_id
        ORDER BY s.name
    """).fetchall()
    conn.close()
    return render_template("attendance.html", subjects=subjects, attendance=rows)

@app.route("/assignments", methods=["GET", "POST"])
def assignments():
    conn = get_db()
    if request.method == "POST":
        title = request.form["title"].strip()
        subject = request.form["subject"].strip()
        due_date = request.form["due_date"]
        if title:
            conn.execute("""INSERT INTO assignments(title,subject,due_date,status)
                            VALUES(?,?,?,'Pending')""", (title, subject, due_date))
            conn.commit()
            flash("Assignment added.")
        return redirect(url_for("assignments"))
    rows = conn.execute("SELECT * FROM assignments ORDER BY due_date").fetchall()
    conn.close()
    return render_template("assignments.html", assignments=rows)

@app.post("/assignments/toggle/<int:id>")
def toggle_assignment(id):
    conn = get_db()
    row = conn.execute("SELECT status FROM assignments WHERE id=?", (id,)).fetchone()
    if row:
        new_status = "Completed" if row["status"] == "Pending" else "Pending"
        conn.execute("UPDATE assignments SET status=? WHERE id=?", (new_status, id))
        conn.commit()
    conn.close()
    return redirect(url_for("assignments"))

@app.post("/assignments/delete/<int:id>")
def delete_assignment(id):
    conn = get_db()
    conn.execute("DELETE FROM assignments WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("assignments"))

@app.route("/marks", methods=["GET", "POST"])
def marks():
    conn = get_db()
    if request.method == "POST":
        subject = request.form["subject"].strip()
        exam = request.form["exam"].strip()
        marks_value = float(request.form["marks"])
        total = float(request.form["total"])
        if subject and total > 0 and 0 <= marks_value <= total:
            conn.execute("INSERT INTO marks(subject,exam,marks,total) VALUES(?,?,?,?)",
                         (subject, exam, marks_value, total))
            conn.commit()
            flash("Marks added.")
        return redirect(url_for("marks"))
    rows = conn.execute("SELECT * FROM marks ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("marks.html", marks=rows)

@app.post("/marks/delete/<int:id>")
def delete_mark(id):
    conn = get_db()
    conn.execute("DELETE FROM marks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("marks"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
