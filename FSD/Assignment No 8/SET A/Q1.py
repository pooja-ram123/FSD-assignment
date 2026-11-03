from flask import Flask
import psycopg2
app = Flask(__name__)
def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="college_db",
        user="postgres",
        password="root",
        port="5432")
@app.route('/')
def home():
    try:
        conn = connect_db()
        conn.close()
        return "Database Connected Successfully"
    except Exception as e:
        return f"Error: {e}"
@app.route('/create_table')
def table_create():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS college_db (
                student_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                course VARCHAR(100))""")
        conn.commit()
        cur.close()
        conn.close()
        return "college_db Table Created Successfully!"
    except Exception as e:
        return f"Error: {e}"
@app.route('/insert_record')
def insert_record():
    try:
        conn = connect_db()
        cur = conn.cursor()
        students = [
            ('Bhagyashri', 20, 'BSc IT'),
            ('Vaishu', 21, 'BSc IT'),
            ('Pooja', 20, 'BCA'),
            ('Mandar', 22, 'BSc CS'),
            ('Anita', 21, 'BCA')]
        cur.executemany("""
            INSERT INTO college_db
            (name, age, course)
            VALUES (%s, %s, %s)
        """, students)
        conn.commit()
        cur.close()
        conn.close()
        return "5 Student Records Inserted Successfully!"
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    app.run(debug=True)