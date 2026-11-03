from flask import Flask

app = Flask(__name__)

@app.route("/")
def employee_list():

    employees = [
        ("sonawane Bhagyashri", "IT", 45000),
        ("Ram Pooja", "HR", 40000),
        ("Saisha Shinde", "Finance", 50000),
        ("Purva Belhekar", "Marketing", 42000),
        ("Ghavte Vaishanavi", "IT", 55000)
    ]

    employee_details = ""

    for name, department, salary in employees:
        employee_details += f"""
        <p>
            Name: {name}<br>
            Department: {department}<br>
            Salary: ₹{salary}
        </p>
        <hr>
        """

    return f"""
    <h2>List of Employees</h2>
    {employee_details}
    """

if __name__ == "__main__":
    app.run(debug=True)