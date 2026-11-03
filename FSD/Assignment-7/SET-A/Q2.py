from flask import Flask,request,jsonify
app=Flask(__name__)
employee=[{
    "Name":"Radha",
    "Age":21
}]
@app.route('/employee',methods=['GET','POST'])
def display():
    return jsonify(employee)
@app.route('/addemployee',methods=['GET','POST'])
def addemployee():
    data=request.get_json()
    employee.append(data)
    return jsonify({
        "msg":"Employee added successfully!",
        "Employee":data
    })
app.run(debug=True)