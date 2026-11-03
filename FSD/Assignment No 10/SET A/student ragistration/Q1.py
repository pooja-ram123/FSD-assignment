
from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)


def db_connect():
    return psycopg2.connect(
        dbname="college_db",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )


def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students1 (
            student_id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course VARCHAR(100) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()


@app.route("/", methods=["GET", "POST"])
def register():
    msg = ""

    if request.method == "POST":
        sid = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()
        course = request.form.get("course", "").strip()

        if not sid or not name or not course:
            msg = "Please fill in all fields."

        elif not sid.isdigit():
            msg = "Student ID must be a number."

        else:
            con = None
            cur = None

            try:
                con = db_connect()
                cur = con.cursor()

                cur.execute("""
                    INSERT INTO students1
                    (student_id, name, course)
                    VALUES (%s, %s, %s)
                """, (int(sid), name, course))

                con.commit()
                msg = "Student registered successfully!"

            except psycopg2.IntegrityError:
                if con:
                    con.rollback()
                msg = "Student ID already exists!"

            except psycopg2.Error as e:
                if con:
                    con.rollback()

                print("Database error:", e)
                msg = "Database error. Please check the terminal."

            finally:
                if cur:
                    cur.close()
                if con:
                    con.close()

    return render_template("index.html", msg=msg)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
