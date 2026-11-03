from flask import Flask

app = Flask(__name__)

@app.route("/students")
def students():

    students = [
        ("Shree", 85),
        ("Pooja", 45),
        ("Vaishnavi", 75),
        ("Purva", 55),
        ("Nisha", 95)
    ]

    result = "<h2>Students Scorign more than 60 Marks</h2>"

    for name, marks in students:
        if marks >= 60:
            result += f"{name} - {marks} marks <br>"

    return result

if __name__ == "__main__":
    app.run(debug=True)
    


            