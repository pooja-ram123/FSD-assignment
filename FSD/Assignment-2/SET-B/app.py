from flask import Flask, render_template, request
app= Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return "Login request received for" + username
    return render_template('Q1.HTML')
app.run(debug=True) 
     