from flask import flask

app = Flask(_name_)

@app.route("/")
def home():
    return("Hello_World, from flask!")