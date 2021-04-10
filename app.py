from flask import Flask, render_template, request, url_for, session , redirect
from models import User
import requests
 

app = Flask(__name__)
url = 'http://localhost:3000/users'

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    if session.get('logged_in'):
        return render_template("reg.html")
    else:
        return render_template('index.html')


@app.route('/register/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        new_user = User(name, password)
        session.add(new_user)
        requests.post(url, new_user.get_json())
        
        session.commit()
        session['logged_in'] = True
    
    return render_template("register.html")



if __name__ == '__main__':
    app.run()
    app.secret_key = 'super_secret_key'
