from flask import Flask, render_template, request, url_for, session , redirect
from models import User
import requests
 

app = Flask(__name__)
url = 'http://localhost:3000/users'



@app.route('/register/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        #session['name'] = request.form.get('username')
        #session['password'] = request.form.get('password')a
        username = request.form.get('username')
        password = request.form.get('password')

        #cockie
        res = make_response('Setting a cockie')
        res.set_cockie('account', username, max_age=60*60*24*365*2)
        return res

        
        #session.commit()
        #session['logged_in'] = True
    
    return render_template("register.html")


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    if session.get('logged_in'):
        return render_template("reg.html")
    else:
        return render_template('index.html',
        nick = session.name,
        role = 'Ученик'
        )


if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = 'super_secret_key'
