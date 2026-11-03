from flask import Flask
app= Flask (__name__)

@app.route("/home")
def home():
    return"Welcome to Home Page"

@app.route("/student")
def student():
    return"Welcome to Student Page"

@app.route("/faculty")
def faculty():
    return "Welcome to Faculty page"

if __name__== "__main__":
    app.run(debug=True)