from flask import Flask 
from flask import render_template
from flask import request
from flask import flash
from flask.helpers import url_for
from werkzeug.utils import redirect
app = Flask(__name__ )

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login" , methods=["GET" , "POST"])
def loginHandler():
    if request.method == 'POST':
        # print(request.form['email'] , request.form['password'])
        # if request.form['email'] == 'test123@testmail.com' or request.form['password'] == 'admin':
        return ("<p>Successful login</p>")
    return render_template('login.html')
