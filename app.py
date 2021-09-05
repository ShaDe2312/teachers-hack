from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__ )

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login" , methods=["GET" , "POST"])
@app.route('/')
def loginHandler():
    if request.method=="GET":
        return render_template('login.html')
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"